# Insure Claim Tracker System

A centralized system for managing insurance claims.

## Description
This project is a Python-based application that manages insurance claims through a simple command-line interface. It allows users to add, view, update, and delete claim records while making sure all required information is entered correctly.

The system is designed to be simple and efficient, helping reduce the need for manual spreadsheets and inconsistent record tracking.

All data is stored in a CSV file, so information is saved and available each time the program runs. The code is organized into functions, making it easier to read, understand, and update.

## Features
- Add a new insurance claim  
- View all stored claims in a formatted table  
- Update an existing claim  
- Delete a claim  
- Prevent duplicate claim IDs  
- Validate numeric input for claim amounts  
- Handle errors to avoid program crashes  
- Search claims by patient name or filter by status  
- View a summary report with totals and per-status breakdown  
- Automatically track creation and last updated timestamps per claim  

## Technologies Used
- Python  
- CSV file handling  
- Command-line interface (CLI)  

## How to Run the Program

1. Clone the repository  
2. Open the project in a Python environment (such as VS Code)  
3. Find the project folder in your terminal  
4. Run the program:

```bash
python InsureClaim.py
```

5. Follow the on-screen menu to interact with the system  

## Code Logic 

The program is organized into separate functions, with each one handling a specific part of the system:

- **Add Claim:** Collects user input, checks that all required fields are entered, ensures the claim ID is unique, and saves the record to the CSV file.

- **View Claims:** Reads the data from the CSV file and displays it in a clean and readable format.

- **Update Claim:** Finds a claim using its ID, allows the user to update selected details, and saves the changes back to the file.

- **Delete Claim:** Removes a claim by rewriting the file without the selected record.

- **Search and Filter:** Lets users find claims by patient name or filter them based on status.

- **Summary Report:** Calculates totals and shows a breakdown of claims by status.

The CSV file is used to store all data, so information is saved and remains available between program runs. The program also includes checks to prevent errors and keep the data consistent.

## Example Usage

When the program runs, the user will see the following menu:

--- Insure Claim Tracker ---

1. Add Claim  
2. View Claims  
3. Update Claim  
4. Delete Claim  
5. Search / Filter Claims  
6. Summary Report  
7. Exit  

The user selects an option by entering the corresponding number.

## Error Handling

The program includes input validation and error handling to ensure:
- Claim amounts are numeric  
- Duplicate claim IDs are prevented  
- Empty or missing files are handled without crashing  
- Required fields are entered  
- Timestamps are automatically recorded  

## Note

The `claims.csv` file is intentionally submitted empty to allow the program to be tested from a clean state. This allows users to run the program and verify all features, including adding, updating, and deleting claims.

## Project Files

This repository contains:

* `InsureClaim.py` – Main Python application
* `claims.csv` – Stores insurance claim records
* `InsureClaim_BoardUpdate.pptx` – Project presentation slides
* `README.md` – Project overview and instructions

The PowerPoint presentation has been uploaded to this repository and can be downloaded directly from GitHub.


## Authors

- Nini Anukwu  
- Gopi Kacha  
- Jordan Davis  
- Chinelo Aniekwu  