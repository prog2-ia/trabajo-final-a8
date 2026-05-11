"""
Código para exportar menús semanales a formato PDF.

Genera un documento PDF con el menú completo incluyendo platos,
ingredientes y calorías para cada día.
"""


from pathlib import Path
from fpdf import FPDF
from models.weekly_menu import WeeklyMenu


def export_menu_to_pdf(menu, filename="menu.pdf"):
    """
    Exporta un menú semanal a un archivo PDF con detalles de platos e ingredientes.

    Args:
        menu (WeeklyMenu): Menú semanal a exportar
        filename (str): Nombre del archivo PDF a generar (default: "menu.pdf")

    Returns:
        None
    """

    # configurar documento PDF con tamaño de fuente base
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="MENÚ SEMANAL", ln=True, align="C")  # título del documento

    # iterar sobre cada día y sus platos
    for day, dish in menu.menu.items():
        # mostrar día y nombre del plato
        pdf.cell(200, 10, txt=f"{day}: {dish.name}", ln=True)
        # listar ingredientes con sus cantidades
        for ing in dish.ingredients:
            pdf.cell(200, 8, txt=f" - {ing.name} ({ing.quantity}g)", ln=True)

        # mostrar calorías totales del plato
        pdf.cell(200, 5, txt=f"Calorías: {dish.total_calories():.2f}", ln=True)
        pdf.ln(5)  # espaciado entre días

    pdf.output(filename)  # generar archivo PDF
