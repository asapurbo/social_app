from PIL import Image, ImageOps
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

def image_fit(image, target_size):
    im = Image.open(image)
    size = target_size

    im = ImageOps.fit(im, size)

    img_io = BytesIO()
    im.save(img_io, format='PNG')
    img_io.seek(0)

    datetime_obj = str(datetime.now().timestamp() * 1000)

    profile_pic_file = InMemoryUploadedFile(
        img_io, None, f'demo_{datetime_obj}.png', 'image/jpeg', img_io.tell(), None
            )

    return profile_pic_file
