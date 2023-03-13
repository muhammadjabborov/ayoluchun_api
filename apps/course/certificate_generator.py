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


def generate_qrcode(first_name, course):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2,
    )
    qr.add_data(f"full name: {first_name}\ncourse: {course}\nwebsite: {WEBSITE}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'qrcode.png'))
    return os.path.join(BASE_DIR, 'media', 'certificate', 'default_certificate', 'qrcode.png')


def certificate_generate(user, course):
    text_y_position = 1300
    img = Image.open(CERTIFICATE, mode='r')
    image_width = img.width
    image_height = img.height
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size=150)
    qrcode_file = generate_qrcode(user.full_name, course.title)
    img2 = Image.open(qrcode_file, mode='r')
    qrcode_x = 880
    qrcode_y = 1900
    text_width = draw.textlength(user.full_name, font=font)
    draw.text(
        (1700, text_y_position-300), course.title, font=ImageFont.truetype(FONT, size=120), fill="#000000"
    )
    draw.text(
        ((image_width + 1370 - text_width - (image_width - 3200)) / 2, text_y_position), user.full_name, font=font, fill="#0e89c4"
    )
    draw.text(
        (1550, text_y_position+200), course.text_for_certificate, font=ImageFont.truetype(FONT, size=120), fill="#000000"
    )

    img.paste(img2, (qrcode_x, qrcode_y))
    if exists(os.path.join(CER_DIR, 'media', 'certificate')) == False:
        os.makedirs(os.path.join(CER_DIR, 'media', 'certificate'))
    file_name = f"{user.full_name}.jpg"
    save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
    if exists(save_img_path):
        while True:
            file_name = f"{user.full_name}{generate_name()}.jpg"
            save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
            if exists(save_img_path):
                continue
            else:
                break
    img.save(save_img_path)

    return os.path.join('certificate', file_name)
