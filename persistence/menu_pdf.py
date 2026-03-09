# importamos la clase FPDF
from fpdf import FPDF

# Instanciamos FPDF
pdf = FPDF()

# Definimos la función
"""
La función recibe cuatro argumentos:
text: texto o contenido del documento.
font_size: tamaño de letras.
title_pdf: titulo del PDF.
doc_name: nombre del archivo.
"""
def generador_pdf(text, font_size, title_pdf, doc_name):
    # Agregamos una pagina en blanco.
    pdf.add_page()

    # Definimos el titulo del documento
    pdf.set_title(title_pdf)

    # Definimos el tipo de fuente y el tamaño
    pdf.set_font("Arial", size=font_size)

    # Agregamos una celda con sus coordenadas (100, 20)
    # Y dfinimos el texto
    pdf.cell(100, 20, txt=text)

    # Generamos la salida del documento.
    pdf.output(doc_name)

# Llamamos a la función con sus respectivos argumentos
generador_pdf("Menú", 50, "Documento de Geek´s Acamdey", "prueba.pdf")