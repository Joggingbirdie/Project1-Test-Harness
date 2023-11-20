import argparse
import csv
import sys

def process_csv(file_path, columns):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            column_sums = {column: 0 for column in columns}

            for row in reader:
                for column in columns:
                    try:
                        column_sums[column] += float(row[column])
                    except (ValueError, KeyError):
                        print(f"Invalid value in column '{column}' in row {reader.line_num}", file=sys.stderr)

            for column, total in column_sums.items():
                print(f"Sum of {column}: {total}")

    except FileNotFoundError:
        print(f"csv_processor: {file_path}: No such file or directory", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CSV file processor")
    parser.add_argument('file', help='Input CSV file')
    parser.add_argument('columns', nargs='+', help='Columns to sum')

    options = parser.parse_args()

    process_csv(options.file, options.columns)

if __name__ == "__main__":
    main()
