from app.services.gemini_service import (
    extract_invoice_data
)

from app.services.parser_service import (
    clean_invoice_data
)

from app.services.calculation_service import (
    calculate_invoice
)

def process_invoice(image_path: str):

    raw_response = extract_invoice_data(image_path)

    structured_data = clean_invoice_data(
        raw_response
    )

    # calculate invoice totals and generate invoice number
    final_invoice = calculate_invoice(structured_data)
    
    return final_invoice