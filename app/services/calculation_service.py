from uuid import uuid4


DISCOUNT_PERCENTAGE = 4.76

CGST_PERCENTAGE = 2.5
SGST_PERCENTAGE = 2.5


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

        # Item total
        item_total = quantity * rate

        # Count quantity totals
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

    # -----------------------------
    # Discount Calculation
    # -----------------------------

    discount_amount = (
        subtotal * DISCOUNT_PERCENTAGE
    ) / 100

    total = subtotal - discount_amount

    # -----------------------------
    # GST Calculation
    # -----------------------------

    cgst_amount = (
        total * CGST_PERCENTAGE
    ) / 100

    sgst_amount = (
        total * SGST_PERCENTAGE
    ) / 100

    # -----------------------------
    # Grand Total
    # -----------------------------

    grand_total = (
        total +
        cgst_amount +
        sgst_amount
    )

    final_invoice = {

        "invoice_number": generate_invoice_number(),

        "customer_name": data.get(
            "customer_name"
        ),

        "invoice_date": data.get(
            "invoice_date"
        ),

        "items": calculated_items,

        "total_boxes": total_boxes,

        "total_pcs": total_pcs,

        "subtotal": round(
            subtotal,
            2
        ),

        "discount_percentage": DISCOUNT_PERCENTAGE,

        "discount_amount": round(
            discount_amount,
            2
        ),

        "total": round(
            total,
            2
        ),

        "cgst_percentage": CGST_PERCENTAGE,

        "cgst_amount": round(
            cgst_amount,
            2
        ),

        "sgst_percentage": SGST_PERCENTAGE,

        "sgst_amount": round(
            sgst_amount,
            2
        ),

        "grand_total": round(
            grand_total,
            2
        )
    }

    return final_invoice