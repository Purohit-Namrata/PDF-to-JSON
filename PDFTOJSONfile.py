import PyPDF2
import json
def load_pdf(file_path):
    with open(file_path,'rb') as file:
        pdf_reader=PyPDF2.PdfFileReader(file)
        return pdf_reader
    

def extract_text(pdf_reader):
    text=""
    num_pages=pdf_reader.numPages

    for page_num in range(num_pages):
        page=pdf_reader.getPage(page_num)
        text+=page.extractText()

    return text

def convert_to_json(text):
    data = {"content":text}
    json_data=json.dumps(data,indent=2)
    return json_data

def save_json(json_data,output_file):
    with open(output_file,'w') as json_file:
        json_file.write(json_data)
    print(f"JSON data saved to {output_file}")

def pdf_to_json(file_path,output_file):
    pdf_reader=load_pdf(file_path)
    text=extract_text(pdf_reader)
    json_data=convert_to_json(text)
    save_json(json_data,output_file)

if __name__=="__main__":
    input_pdf="C:/Users/BLAUPLUG/Documents/Python_programs/json/input.pdf"
    output_json="C:/Users/BLAUPLUG/Documents/Python_programs/json/output.json"
    pdf_to_json(input_pdf,output_json)


