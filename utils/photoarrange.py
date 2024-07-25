import os
from PIL import Image
from datetime import datetime
import shutil
import logging

# 이미지 파일 확장자
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']

def get_image_date_taken(image_path):
    """ 이미지 파일의 촬영 일시를 추출하는 함수 """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                # EXIF 정보에서 촬영 일시 추출
                date_taken = exif_data.get(36867)
                if date_taken:
                    return datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error reading image metadata: {e}")
    return None

def organize_photos(source_dir, dst):
    """ 사진 정리 함수 """
    if not os.path.exists(source_dir):
        print("ERROR: Path not exists:", source_dir)
    if not os.path.exists(dst):
        dst = source_dir
        print("ERROR: Path not exists:", dst)
        print(">>> Process at default directory:", source_dir)

    idx = 0
    for filename in os.listdir(source_dir):
        if any(filename.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
            file_path = os.path.join(source_dir, filename)
            _, ext = os.path.splitext(file_path)
            date_taken = get_image_date_taken(file_path)
            if date_taken:
                year = date_taken.year
                month = date_taken.strftime('%B')
                target_dir = os.path.join(dst, str(year), month)
                os.makedirs(target_dir, exist_ok=True)
                # 새로운 파일 이름 지정
                new_filename = date_taken.strftime("%Y-%m-%d") + f"_{idx:04}" + ext
                # 로깅 설정
                logging.basicConfig(
                    filename=os.path.join(target_dir, 'file_log.log'), 
                    level=logging.INFO, format='%(asctime)s - %(message)s'
                )
                try:
                    shutil.move(file_path, os.path.join(target_dir, new_filename))
                    print(f"Moved {filename} to {os.path.join(target_dir, new_filename)}")
                    logging.info(f"Moved {filename} to {os.path.join(target_dir, new_filename)}")
                except Exception as e:
                    print(f"Failed to move {filename}: {e}")
                    logging.error(f"Failed to move {filename}: {e}")
        idx += 1

    print("Photo organization completed.")

def test_module():
    print("\"photoarragement.py\" module has compiled without errors and is operational.")

def photoarrange(source_directory, dst):
    organize_photos(source_directory, dst)

if __name__ == "__main__":
    source_directory = input("Enter the path to the directory containing photos: ")
    organize_photos(source_directory)
    print("Photo organization completed.")