from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO

def personalize_pdf(template_path, output_path, email):
    reader = PdfReader(template_path)
    writer = PdfWriter()

    for page in reader.pages:
        packet = BytesIO()
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        c = canvas.Canvas(packet, pagesize=(width, height))
        c.setFont("Helvetica", 8)

        # Wasserzeichen z.B. 10 mm vom linken Rand, 15 mm vom unteren Rand
        c.drawString(10 * 2.83, 15 * 2.83, f"{email} – nur zur persönlichen Nutzung, keine Weitergabe")
        c.save()
        packet.seek(0)

        watermark_pdf = PdfReader(packet)
        watermark_page = watermark_pdf.pages[0]

        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

