import sys
import qrcode
import qrcode.image.svg

text = sys.argv[1]
filename = sys.argv[2]

qr = qrcode.QRCode(
    version=1,
    box_size=30,
    border=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L
)

qr.add_data(text)
qr.make(fit=True)


img = qr.make_image(
    fill='black',
    back_color='white',
    image_factory=qrcode.image.svg.SvgPathImage,
)

img.save(f'{filename}.svg')
