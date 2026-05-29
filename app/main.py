from app.services.extraction_service import(
    process_invoice
)

from app.services.information_storage_service import(
    save_information
)

def main():

    image_path = (
        "app/sample_data/test4.jpg"
    )

    result = process_invoice(image_path)

    # save into database
    save_information(result)

    print(result)
    print("Invoice Saved Successfully")

if __name__ == "__main__":
    main()