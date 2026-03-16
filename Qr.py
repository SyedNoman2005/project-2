import qrcode

url = ("enter text or url here")

img = qrcode.make(url)

img.save("qrcode.png")
print("qrcode created successfully")