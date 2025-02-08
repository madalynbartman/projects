import fitz  # PyMuPDF
import pandas as pd

def extract_text_from_pdf(file_path):
    pdf_document = fitz.open(file_path)
    text = ''
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def get_column_sum(text, column_index):
    lines = text.split('\n')
    values = []
    for line in lines:
        columns = line.split()
        if len(columns) > column_index:
            try:
                value = float(columns[column_index])
                values.append(value)
            except ValueError:
                continue
    return sum(values)

pdf_path = 'YourFile.pdf'
column_index = 2  # Change this to the index of the column you want to sum (0 for first column, 1 for second column, etc.)

text = extract_text_from_pdf(pdf_path)
column_sum = get_column_sum(text, column_index)

print(f'The sum of the values in column {column_index + 1} is: {column_sum}')
