import PyPDF2
import json
import os

def load_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return pdf_reader
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the PDF: {e}")
        return None

def extract_text(pdf_reader):
    text = ""
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text() or ""  # Safeguard against None

    return text

def convert_to_json(text):
    data = {"content": text}
    json_data = json.dumps(data, indent=2)
    return json_data

def save_json(json_data, output_file):
    try:
        with open(output_file, 'w') as json_file:
            json_file.write(json_data)
        print(f"JSON data saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving the JSON file: {e}")

def pdf_to_json(input_filename, output_filename):
    input_path = os.path.join(os.getcwd(), input_filename)  # Combine current dir with input filename
    output_path = os.path.join(os.getcwd(), output_filename)  # Output path in current dir
    
    pdf_reader = load_pdf(input_path)
    if pdf_reader is not None:
        text = extract_text(pdf_reader)
        if text.strip():  # Check if text is not empty
            json_data = convert_to_json(text)
            save_json(json_data, output_path)
        else:
            print("Warning: No text extracted from the PDF.")

if __name__ == "__main__":
    input_pdf = "input.pdf"  # Input filename only
    output_json = "output.json"  # Output filename only
    pdf_to_json(input_pdf, output_json)
