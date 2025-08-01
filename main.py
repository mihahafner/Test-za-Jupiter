from csv_writer import write_csv
from helper import welcome

def main():
    welcome("Jupyter User")
    write_csv("sample_output.csv")
    print("End of the process")
if __name__ == "__main__":
    main()
