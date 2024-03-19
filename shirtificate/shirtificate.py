from fpdf import FPDF
from fpdf.enums import Align, XPos, YPos

# Getting user input
name = input("Name: ").strip()

# Creating a pdf file
pdf = FPDF(format=(210, 297))

# Adding a page
pdf.add_page()

# Setting the font
pdf.set_font('helvetica', 'B', 30)

# Creating a cell to write the text
pdf.cell(120, 20, "CS50 Shirtificate", align="C", center=True, new_x=XPos.CENTER, new_y=YPos.LAST)

# Inserting image
pdf.image("shirtificate.png", x=Align.C, y=40, w=180)

# Setting font and color for the image text 
pdf.set_font('helvetica', 'B', 22)
pdf.set_text_color(r=255, g=255, b=255)

# Inserting text
pdf.cell(h=(297/2),text=f"{name} took CS50", align=Align.C, center=True)

# Saving the pdf
pdf.output("shirtificate.pdf")