from fpdf import FPDF
from datetime import date

gender =input("Enter Mr/Ms :")
name=input("Enter Name :")
rollno=input("Enter RollNumber :")
batch=input("Enter Batch : ")
department=input("Enter Department :")
date=date.today()

pdf = FPDF(format=(300,200))
pdf.set_font('Arial', 'B', 12)
pdf.add_page()

# border of certificate
pdf.rect(x=5,y=5,w=290,h=190)

# header image
pdf.image('img.png',h=25,w=270,x=10,y=10)
pdf.cell(h=30, w=270, txt='',ln=5)

# title
pdf.cell(txt='',w=73,h=25,ln=0)
pdf.set_font('Arial','B', 20)
pdf.cell(txt="BONAFIDE CERTIFICATE",w=130,h=15,align='C',ln=1,border=1)

pdf.set_font('Arial','', 30)
pdf.cell(txt='',w=10,h=20,align='C',ln=1)
pdf.cell(txt='',w=50,h=20,align='C',ln=0)
pdf.cell(txt=f"This is to certify that {gender}. ",w=115,h=20,ln=0)

# bold text
pdf.set_font('Arial','B', 30)


pdf.cell(txt=f"{name}",w=50,h=20,ln=1)

# light text
pdf.set_font('Arial','', 30)


pdf.cell(txt='',w=20,h=20,align='C',ln=0)
pdf.cell(txt=f"Roll No. ",w=40,h=20,ln=0)
# bold text
pdf.set_font('Arial','B', 30)

pdf.cell(txt=f"{rollno}  ",w=55,h=20,ln=0)

# light text
pdf.set_font('Arial','', 30)

pdf.cell(txt="was a student of the",w=100,h=20,ln=0)

# bold text
pdf.set_font('Arial','B', 30)


pdf.cell(txt=f"{department}",w=30,h=20,ln=1)

# light text
pdf.set_font('Arial','', 30)


pdf.cell(txt='',w=40,h=20,align='C',ln=0)

pdf.cell(txt=f"Calss of this college during",w=130,h=20,ln=0)

# bold text
pdf.set_font('Arial','B', 30)

pdf.cell(txt=f"{batch} .",w=40,h=20,ln=1)

pdf.cell(w=10,h=15,txt='',ln=1)

# light text
pdf.set_font('Arial','', 30)

pdf.cell(txt=f'Date : {date}',w=100,h=15,ln=0)
pdf.cell(txt='',w=50,h=20,align='C',ln=0)
pdf.image('sign.png',w=100,h=20)

# Save the pdf with name .pdf
pdf.output("certificate.pdf")
