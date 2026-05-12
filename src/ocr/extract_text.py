import easyocr


def extract_receipt_text(image_path: str):

    reader = easyocr.Reader(["en"])

    results = reader.readtext(image_path, detail=0)

    return results