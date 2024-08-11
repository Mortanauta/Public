import pandas as pd
import os
import time
import platform

# Define colors
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREY = '\033[90m'

# Check the operating system
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                        {Color.GREY + 'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                            ▬ Excel Splitter ▬            
      
    This program splits an Excel file (xlsx) into smaller Excel files based on 
    the number of rows you specify.
    
    To run it, enter the full path and name of the original file,
    for example: {Color.BLUE + 'C:/Documents/excel.xlsx '+ Color.RESET}
    Then the destination path, if left blank, the files will be processed in the
    same path as the original file.
    
    {Color.RED + 'NOTE:  ' + Color.RESET} The header is an additional line, so if you request a split 
    of 200 lines, it will generate files of 201 lines (200 + header). 

    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.00' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

# Print operating system check
input(f"""
    CHECKING SYSTEM 
     └ Detected operating system: {OS} {OS_version}

      Press Enter to continue...""")   

# Clear the screen
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# Main Program

def split_excel_file():
    print(f"""\n                                    Excel Splitter                   {Color.GREY + "By Mortanauta" + Color.RESET}
                                                                            V:1.00\n
                                                                       
        {Color.GREEN + '|' + Color.RESET}\\        ╔═══════════════════════════════════════════╗        
        {Color.GREEN + '|⁜' + Color.RESET}\\       ║          Splits an Excel into files       ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
        {Color.GREEN + '|Morta' + Color.RESET}    ║     🔗   based on the number of lines     ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
        {Color.GREEN + '|Nauta' + Color.RESET}    ╚═══════════════════════════════════════════╝  \n """)

    
    # Request the name of the source file
    input_file = input("    ⭕ Path and file name (include .xlsx): ")
    
    # Request the output folder
    output_folder = input("    ⭕ Output folder (leave blank for mantain source folder): ")
    
    # If no output folder is provided, use the source folder
    if output_folder.strip() == "":
        output_folder = os.path.dirname(input_file)
    else:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    # Request the number of rows per file
    rows_per_file = int(input("\n    ⭕ Enter the number of rows per file: "))
    
    print(f"""\n
          {Color.CYAN + 'STARTING CONVERSION'+ Color.RESET} 
          {Color.RED  + '********************************' + Color.RESET }\n """)
    
    # Read the Excel file
    df = pd.read_excel(input_file)
    
    # Get the total number of rows
    total_rows = len(df)
    
    # Calculate the number of files to generate
    num_files = (total_rows // rows_per_file) + (1 if total_rows % rows_per_file != 0 else 0)
    
    # Get the base name of the file without the extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Counter for generated files
    files_created = 0
    
    # Split the DataFrame and save to new files
    for i in range(num_files):
        start_row = i * rows_per_file
        end_row = (i + 1) * rows_per_file
        split_df = df[start_row:end_row]
        
        # Generate the name of the new file
        new_file_name = f"{base_name}_{i + 1}.xlsx"
        full_output_path = os.path.join(output_folder, new_file_name)
        
        # Save the DataFrame to a new Excel file
        split_df.to_excel(full_output_path, index=False)
        
        # Increment the counter of created files
        files_created += 1
        print(f"        File generated: {full_output_path}")
    
    # Show the total number of files created
    print(f"""\n
          {Color.RED  + '********************************' + Color.RESET }
          {Color.CYAN + 'Total files created: ' + Color.RESET} {files_created} 
          
          {Color.CYAN + ' ⫷ Process completed 😎 ⫸ '+ Color.RESET}""")
        

if __name__ == "__main__":
    split_excel_file()
    
input("\n\nPress Enter to exit... ")
