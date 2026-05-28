from app.services.extraction_service import(
    process_invoice
)

def main():

    image_path = (
        "app/sample_data/test1.jpg"
    )

    result = process_invoice(image_path)

    print(result)

if __name__ == "__main__":
    main()