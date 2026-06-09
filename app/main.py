from app.services.extraction_service import(
    process_invoice
)

from app.services.information_storage_service import(
    save_information
)

from app.services.invoice_generation_service import (
    generate_invoice_from_object, generate_invoice
)

from app.services.generated_invoice_storage import (
    upload_invoice_pdf
)

from app.services.invoice_update_service import (
    save_pdf_metadata
)

def main():

    image_path = (
        "app/sample_data/test4.jpg"
    )

    result = process_invoice(image_path)

    print(result)

    # save into database
    invoice = save_information(result)

    print("Information saved in db.")

    # pdf_path = generate_invoice_from_object(invoice)
    pdf_path = generate_invoice(
        invoice.invoice_number
    )

    print(
        f"PDF Generated: {pdf_path}"
    )

    # save generated invoice into supabase storgae
    upload_result = upload_invoice_pdf(pdf_path, invoice.invoice_number)

    print(f"Generated Invoice stored successfully")

    # save pdf url and pdf storage path in information model
    save_pdf_metadata(
        invoice.id,
        upload_result["url"],
        upload_result["storage_path"]
    )

if __name__ == "__main__":
    main()