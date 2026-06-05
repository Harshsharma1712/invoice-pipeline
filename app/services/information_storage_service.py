from app.database.db import SessionLocal
from app.models import (
    Information,
    InformationItem
)
from app.utils.date_parser import (
    parse_invoice_date
)

def save_information(data: dict):

    db = SessionLocal()

    try:
        invoice = Information(

            invoice_number=data.get(
                "invoice_number"
            ),

            customer_name=data.get(
                "customer_name"
            ),

            invoice_date=parse_invoice_date(
                data.get("invoice_date")
            ),

            total_boxes=data.get(
                "total_boxes"
            ),

            total_pcs=data.get(
                "total_pcs"
            ),

            subtotal=data.get(
                "subtotal"
            ),

            discount_percentage=data.get(
                "discount_percentage"
            ),

            discount_amount=data.get(
                "discount_amount"
            ),

            total=data.get(
                "total"
            ),

            cgst_percentage=data.get(
                "cgst_percentage"
            ),

            cgst_amount=data.get(
                "cgst_amount"
            ),

            sgst_percentage=data.get(
                "sgst_percentage"
            ),

            sgst_amount=data.get(
                "sgst_amount"
            ),

            grand_total=data.get(
                "grand_total"
            )
        )

        # Add invoice items
        for item in data.get("items", []):

            invoice_item = InformationItem(

                particulars=item.get(
                    "particulars"
                ),

                size=item.get(
                    "size"
                ),

                hsn_code=item.get(
                    "hsn_code"
                ),

                quantity=item.get(
                    "quantity"
                ),

                quantity_unit=item.get(
                    "quantity_unit"
                ),

                rate=item.get(
                    "rate"
                ),

                item_total=item.get(
                    "item_total"
                )
            )

            invoice.items.append(
                invoice_item
            )

        db.add(invoice)

        db.commit()

        db.refresh(invoice)

        return invoice

    except Exception as e:

        db.rollback()

        raise e

    finally:

        db.close()
