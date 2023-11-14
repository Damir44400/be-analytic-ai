import os
import secrets

from app.config import env
from PIL import Image


async def save_media(file):
    filename_ext = file.filename.split(".")[-1].lower()

    if filename_ext in env.IMAGE_FORMATS:
        return await save_image(file, filename_ext)
    elif filename_ext in env.VIDEO_FORMATS:
        return await save_video(file, filename_ext)
    else:
        raise ValueError(f"Unsupported file format: {filename_ext}")


async def save_image(file, filename_ext):
    img_token_name = secrets.token_hex(10) + "." + filename_ext
    generated_image_name = os.path.join(env.IMAGE_PATH, img_token_name)
    img_content = await file.read()

    with open(generated_image_name, "wb") as img_file:
        img_file.write(img_content)

    resize_and_save_image(generated_image_name)
    return generated_image_name


async def save_video(file, filename_ext):
    video_token_name = secrets.token_hex(10) + "." + filename_ext
    generated_video_name = os.path.join(env.VIDEO_PATH, video_token_name)
    video_content = await file.read()

    with open(generated_video_name, "wb") as video_file:
        video_file.write(video_content)

    return generated_video_name


def resize_and_save_image(image_path, size=(200, 200)):
    img = Image.open(image_path)
    img = img.resize(size=size)
    img.save(image_path)
    img.close()
