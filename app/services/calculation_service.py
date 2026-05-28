from uuid import uuid4


TAX_PERCENTAGE = 5


def generate_invoice_number():

    return f"INV-{uuid4().hex[:8].upper()}"


def calculate_invoice(data: dict):

    items = data.get("items", [])

    total_boxes = 0
    subtotal = 0

    for item in items:

        total_boxes += float(
            item.get("box_pcs", 0)
        )

        subtotal += float(
            item.get("vatable_amount", 0)
        )

    tax_amount = (
        subtotal * TAX_PERCENTAGE
    ) / 100

    grand_total = subtotal + tax_amount

    final_invoice = {
        **data,

        "invoice_number": generate_invoice_number(),

        "total_boxes": round(total_boxes, 2),

        "subtotal": round(subtotal, 2),

        "tax_amount": round(tax_amount, 2),

        "grand_total": round(grand_total, 2)
    }

    return final_invoice