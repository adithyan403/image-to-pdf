from fpdf import FPDF
from PIL import Image
from io import BytesIO

def convert(ipath):
    image=Image.open(ipath).convert("RGB")
    pdf=FPDF()
    pdf.add_page()
    pdf.image(ipath,0,0,pdf.w,pdf.h)
    buffer=BytesIO()
    pdf.output(buffer,'F')
    contents=buffer.getvalue()
    return contents