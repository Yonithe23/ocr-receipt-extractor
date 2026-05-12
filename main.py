from src.ocr.extract_text import extract_receipt_text

image_path = "data/raw/receipt.jpg"

text = extract_receipt_text(image_path)

print(text)