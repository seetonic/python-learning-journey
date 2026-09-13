import qrcode

url = input(f"Enter the URL: ").strip()

#enter your correct file path
file_path = "16. QR code generator/qrimage.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Your QR Code was Generated!")