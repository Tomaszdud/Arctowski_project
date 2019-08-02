from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(100,500, "Hello world")
c.showPage()
c.save()