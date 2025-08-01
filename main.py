from csv_writer import write_csv
from helper import welcome

def main():
    welcome("Jupyter User")
    write_csv("sample_output.csv")

if __name__ == "__main__":
    main()
#🐍 csv_writer.py