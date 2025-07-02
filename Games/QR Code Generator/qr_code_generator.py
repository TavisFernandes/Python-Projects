import qrcode

n = int(input('Enter the no of QR Codes you want to generate: '))

for i in range(3):
    data = input('Enter the text or URL: ').strip()
    filename = input('Enter the filename: ').strip()
    colour = input('Enter the colour of the qr code: ')
    bgcolour = input('Enter the background colour of the qr code: ')
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color=colour, back_color=bgcolour)
    image.save(filename)
    print(f'QR code saved as {filename}')