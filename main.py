import cv2
import cvzone
import os
from mtcnn.mtcnn import MTCNN
import numpy as np


def add_watermark(image, watermark_path):

    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    watermark_alpha = watermark[:, :, 3] / 255.0 * 0.3
    watermark[:, :, 3] = watermark_alpha * 255
    angle = 45
    watermark = cvzone.rotateImage(watermark, angle=angle)
    ih, iw = image.shape[:2]
    result = None
    for i in range(0, iw, 500):
        for j in range(0, ih, 300):
            result = cvzone.overlayPNG(image, watermark, [i, j])
    return result


def scale(watermark, scale_width):
    (watermark_height, watermark_width) = watermark.shape[:2]
    new_height = int(scale_width / watermark_width * watermark_height)
    return cv2.resize(watermark, (scale_width, new_height))


def blur_faces(image_path, output_path, output_error_path, watermark_path):
    image = cv2.imread(image_path)
    detector = MTCNN()
    faces = detector.detect_faces(image)

    if len(faces) == 0:
        print(f"No faces found in {image_path}. Skipping...")
        
        # Create the folder for unblurred photos if it doesn't exist
        if not os.path.exists(os.path.dirname(output_error_path)):
            os.makedirs(os.path.dirname(output_error_path))

        cv2.imwrite(output_error_path, image)
        return False

    for face in faces:
        x, y, width, height = face['box']
        face_region = image[y:y + height, x:x + width]
        face_region = cv2.GaussianBlur(face_region, (99, 99), 30)
        image[y:y + height, x:x + width] = face_region

    # Add watermark to the blurred image
    image_with_watermark = add_watermark(image, watermark_path)

    cv2.imwrite(output_path, image_with_watermark)
    print(f"Image saved to {output_path}")
    return True

def process_folder(input_folder, output_folder, output_error, watermark_path):
    processed = 0
    skipped = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        output_error_path = os.path.join(output_error, filename)

        if os.path.isdir(input_path):
            p, s = process_folder(input_path, output_path, output_error_path, watermark_path)
            processed += p
            skipped += s
        elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            if blur_faces(input_path, output_path, output_error_path, watermark_path):
                processed += 1
            else:
                skipped += 1

    print(f"Processed {processed} images, skipped {skipped} images.")
    return processed, skipped


if __name__ == "__main__":
    input_folder = "data/photo"
    output_folder = "blured_photos_with_watermark"
    output_error = "unblured_photos"
    watermark_path = "LOGO-GORIZONTAL1.png"

    process_folder(input_folder, output_folder, output_error, watermark_path)
