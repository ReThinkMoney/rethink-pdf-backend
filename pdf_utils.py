from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

def personalize_pdf(template_path, output_path, email):
    reader = PdfReader(template_path)
    writer = PdfWriter()

    watermark = BytesIO()
    c = canvas.Canvas(watermark, pagesize=A4)
    c.setFont("Helvetica", 8)
    c.drawString(30, 20, f"{email} – nur zur privaten Verwendung, nicht zur Weitergabe")
    c.save()
    watermark.seek(0)
    mark = PdfReader(watermark).pages[0]

    for page in reader.pages:
        page.merge_page(mark)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
