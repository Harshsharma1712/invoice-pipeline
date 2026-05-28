from uuid import uuid4


TAX_PERCENTAGE = 5


def generate_invoice_number():

    return f"INV-{uuid4().hex[:8].upper()}"


def safe_float(value):

    try:
        return float(value)
    except:
        return 0.0


def safe_int(value):

    try:
        return int(value)
    except:
        return 0


def calculate_invoice(data: dict):

    items = data.get("items", [])

    subtotal = 0

    total_boxes = 0
    total_pcs = 0

    calculated_items = []

    for item in items:

        quantity = safe_int(
            item.get("quantity")
        )

        rate = safe_float(
            item.get("rate")
        )

        quantity_unit = item.get(
            "quantity_unit"
        )

        # Calculate item amount
        item_total = quantity * rate

        # Count totals by unit
        if quantity_unit == "BOX":
            total_boxes += quantity

        elif quantity_unit == "PCS":
            total_pcs += quantity

        subtotal += item_total

        calculated_items.append({

            **item,

            "item_total": round(
                item_total,
                2
            )
        })

    tax_amount = (
        subtotal * TAX_PERCENTAGE
    ) / 100

    grand_total = subtotal + tax_amount

    final_invoice = {

        "invoice_number": generate_invoice_number(),

        "customer_name": data.get(
            "customer_name"
        ),

        "items": calculated_items,

        "total_boxes": total_boxes,

        "total_pcs": total_pcs,

        "subtotal": round(
            subtotal,
            2
        ),

        "tax_percentage": TAX_PERCENTAGE,

        "tax_amount": round(
            tax_amount,
            2
        ),

        "grand_total": round(
            grand_total,
            2
        )
    }

    return final_invoice