import PyPDF2

def merge_pdfs():
    num_pdfs = int(input("Enter the number of PDF files to merge: "))
    input_pdfs = []
    
    for i in range(num_pdfs):
        pdf_file = input(f"Enter the filename of PDF {i + 1}: ")
        input_pdfs.append(pdf_file)
    
    output_pdf = input("Enter the filename for the merged PDF: ")
    
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in input_pdfs:
        pdf_merger.append(pdf_file)

    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Merged PDFs into {output_pdf}')

if __name__ == "__main__":
    merge_pdfs()
