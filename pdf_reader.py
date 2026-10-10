
from pathlib import Path
from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    page_texts = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            page_texts.append(text)

    document_text = "\n".join(page_texts)

    return document_text



from pathlib import Path
from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    page_texts = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            page_texts.append(text)

    document_text = "\n".join(page_texts)

    return document_text


if __name__ == "__main__":
    data_folder = Path("data")
    pdf_files = list(data_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the data folder.")

    else:
        for pdf_path in pdf_files:
            print(f"\nReading: {pdf_path.name}")

            text = read_pdf(str(pdf_path))

            print(text)
            print(f"Total characters: {len(text)}")
            print("-" * 50)
