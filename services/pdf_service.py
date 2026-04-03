from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data, filepath):
    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Kitchen Recipes", styles['Title']))
    content.append(Spacer(1, 12))

    for recipe in data.get("recipes", []):
        content.append(Paragraph(recipe.get("title", "No Title"), styles['Heading2']))
        content.append(Spacer(1, 8))

        content.append(Paragraph(recipe.get("description", ""), styles['Normal']))
        content.append(Spacer(1, 8))

        for step in recipe.get("steps", []):
            content.append(Paragraph(f"• {step}", styles['Normal']))

        content.append(Spacer(1, 16))

    doc.build(content)