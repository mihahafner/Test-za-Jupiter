
import csv

def write_csv(filename):
    rows = [
        ["name", "age"],
        ["Alice", 30],
        ["Bob", 25],
        ["Charlie", 35]
    ]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"CSV file '{filename}' created.")
