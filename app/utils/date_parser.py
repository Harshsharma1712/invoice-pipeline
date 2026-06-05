from datetime import datetime


def parse_invoice_date(
    date_string: str
):
    """
    Converts:
    29/05/2026

    into:

    datetime.date(2026, 5, 29)
    """

    if not date_string:
        return None

    return datetime.strptime(
        date_string.strip(),
        "%d/%m/%Y"
    ).date()