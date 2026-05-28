def clean_json_response(text: str):

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()