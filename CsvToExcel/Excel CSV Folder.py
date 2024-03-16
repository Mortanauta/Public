import os
import pandas as pd
import time
import platform

# --Cut here--8<-------------------------------------------------------------------
# Main page

# Define colors
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BOLD = '\33[1m'
    GREY = '\033[90m'
    UNDERLINE = '\33[4m'
    

# Check the operating system
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                      {Color.GREY + 'By Mortanauta' + Color.RESET}
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
                        
                          ▬ CSV <=> XLSX CONVERTER ▬            
      
    This code allows converting all files from a specified folder
    from CSV to XLSX (and vice versa).

    It validates that the folder exists, indicates the number of converted files, 
    and the time it took for the conversion.
           
    {Color.BOLD}{Color.BLUE + 'NOTE:' + Color.RESET} It does not change the file format.
    
    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.10' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}

   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
# Print operating system check
input(f"""
    CHECKING THE OPERATING SYSTEM
     └ Detected operating system: {OS} {OS_version}

      Press Enter to continue...""")   

# Clear the screen
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Cut here--8<-------------------------------------------------------------------
# Main Program
print(f"""\n                             CSV <-> XLSX CONVERTER                          V:1.1\n

    |\\        ╔══════════════════════════════════════════════╗        
    |⁜\\       ║     ⸎     CSV <-> XLSX CONVERTER             ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║   Convert CSV files to XLSX and vice versa   ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
    |Nauta    ╚══════════════════════════════════════════════╝   \n 
            Conversion is performed on {Color.BOLD}{Color.RED}{Color.UNDERLINE + 'ALL' + Color.RESET} files in the folder.   \n     """)

# Convert CSV files to Excel XLSX
def csv_to_xlsx(folder_path, output_folder):
    converted_files = 0
    start_time = time.time()

    print("\nConverting files:")
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            file_name = os.path.splitext(file)[0] + ".xlsx"
            output_path = os.path.join(output_folder, file_name) if output_folder else os.path.join(folder_path, file_name)

            df = pd.read_csv(file_path)
            df.to_excel(output_path, index=False)
            
            converted_files += 1
            print(f"- Converting: {file}")

    elapsed_time = round(time.time() - start_time, 2)
    print(f"\n    ---CONVERSION COMPLETED!--- 😎")
    print(f"    ► Files converted: {converted_files}")
    print(f"    ► Processing time: {elapsed_time} seconds")
    input("\n     (Press Enter to exit...)")

# Convert Excel XLS/XLSX files to CSV
def xlsx_to_csv(folder_path, output_folder):
    converted_files = 0
    start_time = time.time()

    print("\nConverting files:")
    for file in os.listdir(folder_path):
        if file.endswith(".xls") or file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)
            file_name = os.path.splitext(file)[0] + ".csv"
            output_path = os.path.join(output_folder, file_name) if output_folder else os.path.join(folder_path, file_name)

            df = pd.read_excel(file_path)
            df.to_csv(output_path, index=False)
            
            converted_files += 1
            print(f"- Converting: {file}")

    elapsed_time = round(time.time() - start_time, 2)
    print(f"\n    ---CONVERSION COMPLETED!--- 😎 ")
    print(f"    ► Files converted: {converted_files}")
    print(f"    ► Processing time: {elapsed_time} seconds")
    input("\n     (Press Enter to exit...)")

# Main program
def validate_folder(path):
    return os.path.isdir(path)

if __name__ == "__main__":
    source_folder = input("      ► Source folder path: ")

    while not validate_folder(source_folder):
        print("      ERROR: The source folder path is not valid.")
        source_folder = input("      ► Source folder path: ")

    output_folder = input("""      ► Output folder path 
        (Empty, the same path as the source folder will be used): """)

    if not output_folder:
        output_folder = source_folder
    else:
        while not validate_folder(output_folder):
            print("      ERROR: The output folder path is not valid.")
            output_folder = input("""      ► Output folder path 
        (Empty, the same path as the source folder will be used): """)
    
    print("""
        1. Convert CSV files to Excel XLSX
        2. Convert Excel XLS/XLSX files to CSV
    """)

    option = input("    Select an option (1/2): ")

    if option == '1':
        csv_to_xlsx(source_folder, output_folder)
    elif option == '2':
        xlsx_to_csv(source_folder, output_folder)
