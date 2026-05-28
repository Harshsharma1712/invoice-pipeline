import json

from app.utils.json_cleaner import (
    clean_json_response
)


def clean_invoice_data(raw_text: str):

    cleaned_text = clean_json_response(
        raw_text
    )

    data = json.loads(cleaned_text)

    def to_float(value):

        try:
            return float(value)
        except:
            return 0.0

    cleaned_items = []

    for item in data.get("items", []):

        cleaned_items.append({

            "particulars": str(
                item.get("particulars", "")
            ).strip(),

            "size": (
                str(item.get("size")).strip()
                if item.get("size")
                else None
            ),

            "hsn_code": (
                str(item.get("hsn_code")).strip()
                if item.get("hsn_code")
                else None
            ),

            "box_pcs": to_float(
                item.get("box_pcs")
            ),

            "rate": to_float(
                item.get("rate")
            ),

            "vatable_amount": to_float(
                item.get("vatable_amount")
            )
        })

    return {
        "customer_name": data.get(
            "customer_name"
        ),

        "invoice_name": data.get(
            "invoice_name"
        ),

        "items": cleaned_items
    }