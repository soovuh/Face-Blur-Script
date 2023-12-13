import cv2
import cvzone
import os
from mtcnn.mtcnn import MTCNN
import numpy as np

def add_watermark(input_path, output_path, output_error_path, watermark_path):
    image = cv2.imread(input_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    watermark_alpha = watermark[:, :, 3] / 255.0 * 0.3
    watermark[:, :, 3] = watermark_alpha * 255
    angle = 45
    watermark = cvzone.rotateImage(watermark, angle=angle)
    ih, iw = image.shape[:2]
    image_with_watermark = None
    for i in range(0, iw, 500):
        for j in range(0, ih, 300):
            image_with_watermark = cvzone.overlayPNG(image, watermark, [i, j])
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
            if add_watermark(input_path, output_path, output_error_path, watermark_path):
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