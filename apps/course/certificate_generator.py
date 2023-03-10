from PIL import Image, ImageDraw, ImageFont
from config.settings import BASE_DIR
import os
import qrcode
from os.path import exists
import secrets
import string

WEBSITE = 'https://uic.group'
FONT = os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'MTCORSVA.TTF')

CERTIFICATE = os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'certificate.jpg')

CER_DIR = f'{BASE_DIR}/'


def generate_name():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(5))

    return password


def generate_qrcode(username, promocode):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2,
    )
    qr.add_data(f"username: {username}\npassword: {promocode}\nwebsite: {WEBSITE}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'qrcode.png'))
    return os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'qrcode.png')


def certificate_generate(student):
    text_y_position = 1300
    img = Image.open(CERTIFICATE, mode='r')
    image_width = img.width
    image_height = img.height
    # f = open(FONT, 'rb')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size=150)
    qrcode_file = generate_qrcode(student['username'], student['promo_code'])
    img2 = Image.open(qrcode_file, mode='r')
    qrcode_x = 880
    qrcode_y = 1900
    text_width = draw.textlength(student['full_name'], font=font)
    draw.text((
        (image_width + 1370 - text_width - (image_width - 3200)) / 2,
        text_y_position
    ),
        student['full_name'], font=font, fill="#0e89c4"
    )

    img.paste(img2, (qrcode_x, qrcode_y))
    if exists(os.path.join(CER_DIR, 'media', 'certificate')) == False:
        os.makedirs(os.path.join(CER_DIR, 'media', 'certificate'))
    file_name = f"{student['full_name']}.jpg"
    save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
    if exists(save_img_path):
        while True:
            file_name = f"{student['full_name']}{generate_name()}.jpg"
            save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
            if exists(save_img_path):
                continue
            else:
                break
    img.save(save_img_path)

    return os.path.join('certificate', file_name)


st = {
    "full_name": "Eshpulatov Azizjon",
    "promo_code": "UIC",
    "username": "Azizjon"
}

certificate_generate(student=st)
