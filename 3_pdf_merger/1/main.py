from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["sample.pdf","sample_a.pdf","sample_b.pdf"]:
    merger.append(pdf)

merger.write("merged.pdf")