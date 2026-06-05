import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


OUTPUT_DIR = "app/generated_invoices"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


def generate_invoice_pdf(
    invoice
):
    pdf_path = os.path.join(
        OUTPUT_DIR,
        f"{invoice.invoice_number}.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    # --------------------
    # HEADER
    # --------------------

    elements.append(
        Paragraph(
            "TAX INVOICE",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    invoice_info = [
        [
            f"Invoice No: {invoice.invoice_number}",
            f"Date: {invoice.invoice_date.strftime('%d/%m/%Y')}"
        ],
        [
            f"Customer: {invoice.customer_name}",
            ""
        ]
    ]

    invoice_table = Table(
        invoice_info,
        colWidths=[250, 250]
    )

    elements.append(
        invoice_table
    )

    elements.append(
        Spacer(1, 20)
    )

    # --------------------
    # ITEMS TABLE
    # --------------------

    data = [
        [
            "Particular",
            "Size",
            "HSN",
            "Qty",
            "Rate",
            "Amount"
        ]
    ]

    for item in invoice.items:

        data.append(
            [
                item.particulars,
                item.size,
                item.hsn_code,
                f"{item.quantity}",
                f"{item.rate}",
                f"{item.item_total}"
            ]
        )

    item_table = Table(
        data,
        colWidths=[
            150,
            60,
            80,
            60,
            60,
            80
        ]
    )

    item_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                )
            ]
        )
    )

    elements.append(
        item_table
    )

    elements.append(
        Spacer(1, 20)
    )

    # --------------------
    # TOTALS
    # --------------------

    totals = [
        [
            "Subtotal",
            f"{invoice.subtotal:.2f}"
        ],
        [
            "Discount",
            f"{invoice.discount_amount:.2f}"
        ],
        [
            f"CGST ({invoice.cgst_percentage}%)",
            f"{invoice.cgst_amount:.2f}"
        ],
        [
            f"SGST ({invoice.sgst_percentage}%)",
            f"{invoice.sgst_amount:.2f}"
        ],
        [
            "Grand Total",
            f"{invoice.grand_total:.2f}"
        ]
    ]

    totals_table = Table(
        totals,
        colWidths=[200, 150]
    )

    totals_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                )
            ]
        )
    )

    elements.append(
        totals_table
    )

    doc.build(
        elements
    )

    return pdf_path