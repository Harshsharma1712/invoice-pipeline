from app.services.invoice_generation_service import (
    generate_invoice
)


def main():

    invoice_number = "INV-A6808A2D"

    pdf_path = generate_invoice(
        invoice_number
    )

    print(
        f"Generated: {pdf_path}"
    )


if __name__ == "__main__":
    main()