from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from io import BytesIO

def personalize_pdf(template_path, output_path, email):
    reader = PdfReader(template_path)
    writer = PdfWriter()

    for page in reader.pages:
        packet = BytesIO()
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        # Neues Wasserzeichen für jede Seite
        c = canvas.Canvas(packet, pagesize=(width, height))
        c.setFont("Helvetica", 8)
        c.drawString(30, 20, f"{email} – nur zur privaten Verwendung, nicht zur Weitergabe")
        c.save()
        packet.seek(0)

        # Wasserzeichen als PDF laden und einfügen
        watermark = PdfReader(packet).pages[0]
        page.merge_page(watermark)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
