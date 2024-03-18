#pip install pdf2docx

#import Pdf2docx

import os
import time
import platform
from pdf2docx import Converter

# --Cut here--8<-------------------------------------------------------------------
# Main Page

# Define colors
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    GREY = '\033[90m'

# Check the operating system
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                        {Color.GREY +'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                            ▬ PDF to Word Converter ▬            
      
    This program converts a PDF file to Word, keeping the images, structure and 
    format of the original file.
    
    To work, insert the full path and the name of the original file, for example:
         {Color.BLUE + 'C:/Documents/article.pdf'+ Color.RESET}
    And then the path and name of the destination file, if you left blank, it will 
    process with the same folder and name as the original file, with Word format.
    
    {Color.RED + 'Warning:  ' + Color.RESET}● Check the result, it varies a lot depending on the PDF format
                and its structure. 
              ● This program is not an OCR , so it cannot read scanned PDF images. 
    
    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.1' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
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

print(f"""\n
                                                    Ver: 1.1
        |\       ╔═════════════════════════╗ 
        |⁜\      ║   Convert PDF 2 Word    ║ ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
        |Morta   ║      with images        ║ ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║  
        |Nauta   ╚═════════════════════════╝ 
                                                                """) 


#pdf_file = 'C:\\Users\\miguelangel.depablo\\Documents\\CODIGO\\Python\\ComoEntrenarIA.pdf'
pdf_file = input("\n        ♦   Enter the full path and name of the PDF file: ")#'C:\\Users\\miguelangel.depablo\\Documents\\CODIGO\\Python\\ComoEntrenarIA.pdf'
#docx_file = 'C:\\Users\\miguelangel.depablo\\Documents\\CODIGO\\Python\\ombre.docx'
print(f"""\n               {Color.GREY + '(Leave empty to use the same name and folder)'+Color.RESET}""" )
docx_file = input("        ♦   Enter the full path and name of the DESTINATION WORD file: ")#'C:\\Users\\miguelangel.depablo\\Documents\\CODIGO\\Python\\ombre.docx'

print(f"\n\nConverting PDF to Word... 🤖 \n")
# Check if an output file name was provided
if not docx_file:
    # In case no output file name was provided, reuse the PDF file name for the Word file
    docx_file = pdf_file.replace(".pdf", ".docx")

# COnversion of PDF to Word  
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

input("\nPulse Enter para salir...")