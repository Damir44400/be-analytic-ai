import os
import secrets

from PIL import Image
from app.config import env


async def save_image(file, filename_ext):
    img_token_name = secrets.token_hex(10) + "." + filename_ext
    generated_image_name = os.path.join(env.IMAGE_PATH, img_token_name)
    img_content = await file.read()

    with open(generated_image_name, "wb") as img_file:
        img_file.write(img_content)

    resize_and_save_image(generated_image_name)
    return generated_image_name


def delete_file(filename: str):
    file_path = os.path.join(env.IMAGE_PATH, filename)
    if os.path.exists(file_path):
        os.remove(file_path)


def resize_and_save_image(image_path, size=(230, 340)):
    img = Image.open(image_path)
    img = img.resize(size=size)
    img.save(image_path)
    img.close()
