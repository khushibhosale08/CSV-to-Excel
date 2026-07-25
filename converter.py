import csv
import logging
import os
from datetime import datetime
from openpyxl import Workbook

# Configure logging
logging.basicConfig(
    filename="converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_value(value):
    """Replace missing values."""
    if value.strip() == "":
        return "Not Available"
    return value.strip()


def parse_date(date_text):
    """Convert DD-MM-YYYY to DD/MM/YYYY."""
    if date_text == "Not Available":
        return date_text

    try:
        date = datetime.strptime(date_text, "%d-%m-%Y")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        return "Invalid Date"


def convert_csv_to_excel(input_file, output_file):
    """Convert CSV file to Excel."""

    try:

        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{input_file} not found.")

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Employee Data"

        with open(input_file, "r", encoding="utf-8") as csv_file:

            reader = csv.reader(csv_file)

            for row_number, row in enumerate(reader):

                # Header
                if row_number == 0:

                    header = []

                    for column in row:

                        if column == "Name":
                            header.append("Full_Name")

                        elif column == "DOB":
                            header.append("Date_of_Birth")

                        else:
                            header.append(column)

                    sheet.append(header)
                    continue

                cleaned_row = []

                for index, value in enumerate(row):

                    value = clean_value(value)

                    if index == 1:
                        value = parse_date(value)

                    cleaned_row.append(value)

                sheet.append(cleaned_row)

        workbook.save(output_file)

        logging.info("Conversion Successful")

        print("\n========== CSV TO EXCEL CONVERTER ==========")
        print("Input File :", input_file)
        print("Output File:", output_file)
        print("Status     : Success")
        print("============================================")

    except FileNotFoundError as e:
        logging.error(e)
        print(e)

    except Exception as e:
        logging.error(e)
        print("Unexpected Error:", e)


if __name__ == "__main__":
     import os

folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(folder, "data.csv")
output_file = os.path.join(folder, "output.xlsx")

if __name__ == "__main__":
    convert_csv_to_excel("data.csv", "output.xlsx")