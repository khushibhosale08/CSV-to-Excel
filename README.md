# CSV to Excel Converter

## Overview

CSV to Excel Converter is a Python automation project that reads data from a CSV file, performs basic data cleaning, and exports the cleaned data into an Excel (.xlsx) file.

This project is useful for data preparation, reporting, and automation tasks.

---

## Features

- Read data from a CSV file
- Convert CSV to Excel (.xlsx)
- Handle missing values
- Parse and format dates
- Rename column headers
- Generate log file for conversion status
- Error handling for missing or invalid files

---

## Technologies Used

- Python 3
- openpyxl
- csv (built-in)
- logging (built-in)
- datetime (built-in)
- os (built-in)

---

## Project Structure

```
csv-excel-converter/
│── converter.py
│── data.csv
│── README.md
│── requirements.txt
└── .gitignore
```

---

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the Python script:
```bash
python converter.py
```

---

## Input

The program reads data from:

```
data.csv
```

Example:

```csv
Name,DOB,City,Salary
Rahul,12-01-2003,Pune,25000
Priya,,Mumbai,30000
Amit,25-05-2002,,28000
John,18-11-2001,Delhi,
```

---

## Output

The program generates:

- `output.xlsx` – Converted Excel file
- `converter.log` – Log file containing conversion status

---

## Error Handling

The project checks for:

- Missing CSV file
- Invalid date formats
- Empty values
- Unexpected runtime errors

---

## Future Improvements

- Add command-line arguments (`-i` and `-o`)
- Support multiple CSV files
- Apply Excel formatting
- Create summary reports
- Add a graphical user interface (GUI)

---

## Author

Developed as a Python automation project for internship practice.
