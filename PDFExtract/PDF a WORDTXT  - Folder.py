# Author: Mortanauta
# Version: 1.10
# Website: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

#Changelog:
#1.1 - Added timer and verbose for converted files 12/05/2023

#Required elements for program execution:
#pip install python-docx
#pip install PyPDF2


import os
from PyPDF2 import PdfReader
from docx import Document
import time
import platform

# --Cut here--8<-------------------------------------------------------------------
# Main Page

# Define colors
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    GREY = '\033[90m'

# Check the operating system
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                        {Color.GREY +'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                        ▬ PDF to Word/TXT Converter ▬            
      
    This code converts PDF files to text or Word quickly.

    It converts all PDF files found in the specified folder, 
    allowing the selection of the output format (TXT or DOCX).

    NOTE: The result may vary depending on the PDF encoding.    
             
    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.32' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

# Print operating system check
input(f"""
    CHECKING THE SYSTEM 
     └ Detected operating system: {OS} {OS_version}

      Press Enter to continue...""")   

# Clear the screen
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Cut here--8<-------------------------------------------------------------------
# Main Program

def pdf_to_text(pdf_path, output_path, format):
    if format == 1:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            text = ''
            for page_number in range(len(reader.pages)):
                text += reader.pages[page_number].extract_text()

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
    elif format == 2:
        doc = Document()
        with open(pdf_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            for page_number in range(len(reader.pages)):
                text = reader.pages[page_number].extract_text()
                doc.add_paragraph(text)

        doc.save(output_path)

if __name__ == "__main__":
    print(f"""\n
                                                                            Version 1.1

    |\        ╔══════════════════════════════════════════╗             
    |⁜\       ║    📚  PDF to Word/TXT Converter         ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║       Converts PDF files to text         ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║   
    |Nauta    ╚══════════════════════════════════════════╝   \n """)             

    # Ask the user for the folder path containing the PDF files
    pdf_folder = input("\n    ♦   Enter the path of the folder containing the PDF files: ")

    # Ask the user for the output folder path for the files
    text_folder = input("    ♦   Enter the path for the output folder\n        (if not entered, the same path as the PDF folder will be used): ")

    if not text_folder:
        text_folder = pdf_folder  # If no path is entered, use the same as the PDF folder

    # Ask the user for the output format
    while True:
        output_format = input("\n    ♦   Choose the output format (1 for TXT, 2 for DOCX): ")
        if output_format in ['1', '2']:
            break
        else:
            print("        Please enter 1 for TXT or 2 for DOCX.")

    # Counters for files and execution time
    converted_files = 0
    start_time = time.time()
    print("""
    Converting files:""")
    
    # Convert all PDF files to text in the output folder
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file)
            file_name = os.path.splitext(file)[0]

            if output_format == '1':
                output_path = os.path.join(text_folder, file_name + ".txt")
            elif output_format == '2':
                output_path = os.path.join(text_folder, file_name + ".docx")

            pdf_to_text(pdf_path, output_path, int(output_format))
            converted_files += 1
            print(f"- File converted: {file}")

    elapsed_time = round(time.time() - start_time, 2)

    print(f"\n    ---CONVERSION COMPLETED!--- :)")
    print(f"    ♦ Converted files: {converted_files}")
    print(f"    ♦ Processing time: {elapsed_time} seconds")
    input("\n     (Press Enter to exit...)")
