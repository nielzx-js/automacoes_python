import pdfplumber

with pdfplumber.open("pags.pdf") as pdf:
    for pg in pdf.pages:
        texto = pg.extract_text()
        print(texto)