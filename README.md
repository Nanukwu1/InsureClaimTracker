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
* Search claims by patient name or filter by status
* View a summary report with totals and per-status breakdown
* Automatically track creation and last updated timestamps per claim

## Technologies Used

* Python
* CSV file handling
* Command-line interface (CLI)

## How to Run the Program

1. Clone the repository  
2. Open the project in a Python environment (such as VS Code)
3. Find the project folder in your terminal
4. Run the file:

```bash
python InsureClaim.py
```

5. Follow the on-screen menu to interact with the system


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

This system includes input validation and error handling to ensure:

* Claim amounts are numeric
* Avoid duplicate claim IDs
* Handles empty or missing files without crashing
* Required fields are entered
* Timestamps are automatically recorded and cannot be manually entered or skipped

## Authors

* Nini Anukwu
* Gopi Kacha
* Jordan Davis
* Chinelo Aniekwu
