import qrcode

qr = qrcode.QRCode(version=1, box_size=20, border=2)

qr.add_data('https://imajmin.netlify.app');

qr.make(fit=True)

img = qr.make_image(fill_color='dodgerblue', back_color='white')
img.save('myqrcode.png')