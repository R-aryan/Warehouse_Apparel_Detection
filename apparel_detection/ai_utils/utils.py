import base64


def decodeImage(imgstring, image_name, image_path):
    imgdata = base64.b64decode(imgstring)
    with open(image_path + image_name, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
