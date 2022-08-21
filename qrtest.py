import qrcode
from PIL import Image

img = qrcode.make('https://www.youtube.com/watch?v=bPUXpH5Sww4&ab_channel=NBA')

qrcode=qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

qrcode.add_data('https://www.youtube.com/watch?v=bPUXpH5Sww4&ab_channel=NBA')
qrcode.make(fit=True)
img=qrcode.make_image(fill_color='green',back_color='white')
img.save('TatumBuzzerBeater.png')