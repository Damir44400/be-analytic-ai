import os.path
import shutil


async def save_image(image):
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}
