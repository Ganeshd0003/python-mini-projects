# Use PNG format for QR codes because it is lossless and preserves sharp edges.
# Sharp edges are critical for accurate QR code scanning.

# JPG and JPEG are the same format (JPEG).
# They use lossy compression, which can introduce blur and artifacts,
# making them unsuitable for high-quality QR codes.

import qrcode

url = input("Enter the url :")
file_name = input("Enter the file name you want to save :")
file_name = file_name.strip().lower().replace(" ", "_")
img = qrcode.make(url)
img.save(f"{file_name}.png")


# A QR code can still be scanned even if up to about 30% of it is damaged, because it uses built-in error correction.
# That’s why QR codes work on scratched posters or crumpled paper, and why logos can be placed in the center without breaking them.
# QR codes are made of modules, and the more data you store, the denser those modules become