from fpdf import FPDF


def export_menu_to_pdf(menu, filename="menu.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="MENÚ SEMANAL", ln=True, align="C")

    for day, dish in menu.menu.items():
        pdf.cell(200, 10, txt=f"{day}: {dish.name}", ln=True)

        for ing in dish.ingredients:
            pdf.cell(200, 8, txt=f" - {ing.name} ({ing.quantity}g)", ln=True)

        pdf.cell(200, 5, txt=f"Calorías: {dish.total_calories():.2f}", ln=True)
        pdf.ln(5)

    pdf.output(filename)
