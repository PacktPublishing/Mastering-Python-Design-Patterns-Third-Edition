import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def lambda_handler(event, context):
    # Sample data from the purchase event
    data = [["Item", "Quantity", "Price"], ["Widget", 2, 25.00], ["Gizmo", 1, 15.00]]

    # Generate PDF
    pdf = SimpleDocTemplate("/tmp/receipt.pdf", pagesize=letter)

    # Add Table
    table = Table(data)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    elems = []
    elems.append(table)
    pdf.build(elems)

    # Here you can add code to upload the PDF to S3 or email it

    return {"statusCode": 200, "body": json.dumps("PDF receipt generated.")}
