from pypdf import PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("Enter how many pdf you want to merger: "))

for i in range(0,n):
    name = input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()