from app.services.extraction_service import(
    process_invoice
)

from app.services.information_storage_service import(
    save_information
)

from app.services.invoice_generation_service import (
    generate_invoice_from_object, generate_invoice
)

def main():

    image_path = (
        "app/sample_data/test4.jpg"
    )

    result = process_invoice(image_path)

    # save into database
    invoice = save_information(result)

    # pdf_path = generate_invoice_from_object(invoice)
    pdf_path = generate_invoice(
        invoice.invoice_number
    )

    print(result)
    
    print("Invoice Saved Successfully")

    print(
        f"PDF Generated: {pdf_path}"
    )

if __name__ == "__main__":
    main()