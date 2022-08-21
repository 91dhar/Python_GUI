import qrcode
from PIL import Image

img = qrcode.make('https://streamable.com/io6r80')

qrcode=qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

qrcode.add_data('https://streamable.com/io6r80')
qrcode.make(fit=True)
img=qrcode.make_image(fill_color='green',back_color='white')
img.save('TatumBuzzerBeater.png')
