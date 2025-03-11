import qrcode

data= input("Enter the text to create qrcode:")

qr= qrcode.QRCode(version=1 , box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
qr_image= qr.make_image(fill="black", back_color="white")
qr_image.save("qrcode.png")
print("QR code generated successfully") 
