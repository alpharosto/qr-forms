import qrcode

# URL to be encoded
url = "https://forms.gle/ew11DkSCG8ceFFd6A"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img_path = "qr_code.png"
img.save(img_path)

print(f"QR code saved as {img_path}")
