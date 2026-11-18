import pdfplumber
with pdfplumber.open("roteiro.pdf") as pdf:
    pg1 = pdf.pages[0]
    texto = pg1.extract_text()
    print(texto)
