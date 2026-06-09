from app.services.generated_invoice_storage import (
    upload_invoice_pdf
)

def test_upload():

    pdf_path = (
        "app/generated_invoices/INV-A4117FAA.pdf"
    )

    invoice_number = (
        "INV-A4117FAA"
    )

    result = upload_invoice_pdf(
        pdf_path,
        invoice_number
    )

    print("\nUPLOAD RESULT:")
    print(result)

    print("\nURL:")
    print(result["url"])


if __name__ == "__main__":
    test_upload()