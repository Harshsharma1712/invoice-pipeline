import json

from app.utils.json_cleaner import clean_json_response


def clean_invoice_data(raw_text: str):

    cleaned_text = clean_json_response(raw_text)

    data = json.loads(cleaned_text)

    def to_float(value):

        if value is None:
            return None

        try:
            return float(str(value).replace(",", "").strip())
        except:
            return None

    def to_int(value):

        if value is None:
            return None

        try:
            return int(float(str(value).strip()))
        except:
            return None

    def clean_text(value):

        if value is None:
            return None

        text = str(value).strip()

        return text if text else None

    cleaned_items = []

    for item in data.get("items", []):

        quantity_unit = clean_text(
            item.get("quantity_unit")
        )

        # Normalize quantity unit
        if quantity_unit:
            quantity_unit = quantity_unit.upper()

            if quantity_unit in ["BOX", "BOXES"]:
                quantity_unit = "BOX"

            elif quantity_unit in ["PCS", "PIECES", "PIECE"]:
                quantity_unit = "PCS"

            else:
                quantity_unit = None

        cleaned_items.append({

            "particulars": clean_text(
                item.get("particulars")
            ),

            "size": clean_text(
                item.get("size")
            ),

            "hsn_code": clean_text(
                item.get("hsn_code")
            ),

            "quantity": to_int(
                item.get("quantity")
            ),

            "quantity_unit": quantity_unit,

            "rate": to_float(
                item.get("rate")
            )
        })

    return {

        "customer_name": clean_text(
            data.get("customer_name")
        ),

        "invoice_date": clean_text(
        data.get("invoice_date")
        ),

        "items": cleaned_items
    }