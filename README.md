# Insure Claim Tracker System
A centralized system for managing insurance claims.

This project is a Python-based application designed to manage insurance claims through a simple command-line interface. It allows users to add, view, update, and delete claim records while ensuring that all required information is entered correctly.

The system is designed to be simple, efficient, and user-friendly for managing claim records.

This program reduces the need for manual spreadsheets, unnecessary tools, and inconsistent record tracking.

All data is stored in a CSV file, so information is saved and available the next time the program runs. The system is organized using functions, making the code easier to understand, maintain, and update.

## Features

* Add a new insurance claim
* View all stored claims in a formatted table
* Update an existing claim
* Delete a claim
* Prevent duplicate claim IDs
* Validate numeric input for claim amounts
* Handle errors to avoid program crashes

## Technologies Used

* Python
* CSV file handling
* Command-line interface (CLI)

## How to Run the Program

1. Download or clone the repository  
2. Open the project in a Python environment (such as VS Code)  
3. Run the file:

```bash
python InsureClaim.py
```

4. Follow the on-screen menu to interact with the system

## File Structure

* InsureClaim.py → Main program file containing all logic
* claims.csv → Stores all claim records
* README.md → Project documentation

## Example Usage

When the program runs, the user will see the following menu:

--- Insure Claim Tracker ---

1. Add Claim
2. View Claims
3. Update Claim
4. Delete Claim
5. Exit

The user selects an option by entering the corresponding number.

## Error Handling

The program includes error handling to:

* Prevent non-numeric claim amounts
* Avoid duplicate claim IDs
* Handle missing files
* Prevent crashes from invalid or incomplete input

## Authors

* Nini Anukwu
* Gopi Kacha
* Jordan Davis
* Chinelo Aniekwu
