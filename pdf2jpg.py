# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
# dowload from https://github.com/oschwartz10612/poppler-windows/releases/

images = convert_from_path('Photo.pdf',poppler_path=r"C:\Users\xx\xx\Release-23.11.0-0\poppler-23.11.0\Library\bin")

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')
