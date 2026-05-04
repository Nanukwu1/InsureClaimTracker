# ============================================
# INSURE CLAIM TRACKER SYSTEM
# Authors: Nini Anukwu, Gopi Kacha, Jordan Davis, Chinelo Aniekwu
# Description:
# This program allows users to manage insurance claims
# using Create, Read, Update, and Delete (CRUD) operations.
# Data is stored in a CSV file.
# ============================================

import os
from datetime import datetime

FILE_NAME = os.path.join(os.path.dirname(__file__), "claims.csv")

# ----------------------------------------------------------
# Ensure the claim amount is numeric to prevent invalid financial data from being stored
# ----------------------------------------------------------
def is_valid_amount(amount):
    # Try to convert the amount to a number
    try:
        float(amount)
        return True
    # If conversion fails, the amount is not valid
    except ValueError:
        return False

# ----------------------------------------------------------
# Check whether the claim ID already exists to prevent duplicate entries
# ----------------------------------------------------------
def claim_id_exists(claim_id):
    # If the CSV file does not exist yet, no duplicate claim ID can exist
    if not os.path.exists(FILE_NAME):
        return False

    # Read each claim in the CSV file and compare the stored Claim ID
    with open(FILE_NAME, "r") as file:
        for line in file:
            # Split each line and check only the first column, which stores the Claim ID
            if line.split(",")[0] == claim_id:
                return True

    # Return False if no matching Claim ID is found
    return False

# ----------------------------------------------------------
# Return the current timestamp in a readable format
# ----------------------------------------------------------
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------------------------------------------------
# Initialize the CSV file if it does not exist
# Now includes Created and Last Updated columns for date tracking
# ----------------------------------------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Claim ID,Patient Name,Amount,Status,Created,Last Updated\n")

# ----------------------------------------------------------
# Add a new claim to the system by collecting user input
# Automatically records the creation timestamp
# ----------------------------------------------------------
def add_claim():
    print("\n--- Add Claim ---")

    try:
        # Collect user input for each required field with clear instructions
        claim_id = input("Enter Claim ID (must be unique): ").strip()
        name = input("Enter Patient Name: ").strip()
        amount = input("Enter Claim Amount (numbers only): ").strip()
        status = input("Enter Claim Status (e.g., Pending, Paid): ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    # Validate input to ensure all required fields are completed before saving
    if claim_id == "" or name == "" or amount == "" or status == "":
        print("Error: All fields are required.")
        return

    # Validate amount is numeric
    if not is_valid_amount(amount):
        print("Error: Amount must be numeric.")
        return

    # Check for duplicate Claim ID
    if claim_id_exists(claim_id):
        print("Error: Claim ID already exists.")
        return
    
    # Capture the current timestamp as the creation date
    timestamp = get_timestamp()

    # Save the new claim to the CSV file,including created and last updated timestamps
    with open(FILE_NAME, "a") as file:
        file.write(f"{claim_id},{name},{amount},{status},{timestamp},{timestamp}\n")
        print(f"Claim added successfully. Created at: {timestamp}")

# ----------------------------------------------------------
# Display all stored claims from the CSV file
# ----------------------------------------------------------
def view_claims():
    print("\n--- All Claims ---")

    try:
        # Read stored data from the CSV file
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        # Check if file is empty and inform the user if no claims are found
        if len(lines) <= 1:
            print("No claims found.")
            return

        # Display column headers so the output is easier to read
        print(f"{'ID':<10}{'Name':<20}{'Amount':<10}{'Status':<10}{'Created':<22}{'Last Updated':<22}")
        print("-" * 94)
      
        # Go through each claim and display its details
        for line in lines[1:]:
            # Split the line into individual values using comma as delimiter
            data = line.strip().split(",")

            # Handle both old format (4 columns) and new format (6 columns)
            if len(data) == 4:
                print(f"{data[0]:<10}{data[1]:<20}{data[2]:<10}{data[3]:<10}{'N/A':<22}{'N/A':<22}")
            elif len(data) == 6:
                print(f"{data[0]:<10}{data[1]:<20}{data[2]:<10}{data[3]:<10}{data[4]:<22}{data[5]:<22}")
            else:
                # Skip any incomplete or incorrectly formatted lines to prevent errors
                continue

    except FileNotFoundError:
        print("Error: File not found.")

# ----------------------------------------------------------
# Search and filter claims by patient name or status
# Allows partial matches so users don't need exact input
# ----------------------------------------------------------
def search_claims():
    print("\n--- Search / Filter Claims ---")
    print("1. Search by Patient Name")
    print("2. Filter by Status")
 
    try:
        choice = input("Select search type: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return
 
    if choice not in ("1", "2"):
        print("Invalid option.")
        return
 
    try:
        keyword = input("Enter search term: ").strip().lower()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return
 
    if keyword == "":
        print("Error: Search term cannot be empty.")
        return
 
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return
 
    # Collect all matching results
    results = []
    for line in lines[1:]:
        data = line.strip().split(",")
        if len(data) < 4:
            continue
 
        # Match against name (column 1) or status (column 3) based on user choice
        if choice == "1" and keyword in data[1].lower():
            results.append(data)
        elif choice == "2" and keyword in data[3].lower():
            results.append(data)
 
    # Display results or inform the user nothing was found
    if not results:
        print("No matching claims found.")
        return
 
    print(f"\n--- Search Results ({len(results)} found) ---")
    print(f"{'ID':<10}{'Name':<20}{'Amount':<10}{'Status':<10}{'Created':<22}{'Last Updated':<22}")
    print("-" * 94)
    for data in results:
        created = data[4] if len(data) > 4 else "N/A"
        updated = data[5] if len(data) > 5 else "N/A"
        print(f"{data[0]:<10}{data[1]:<20}{data[2]:<10}{data[3]:<10}{created:<22}{updated:<22}")

# ----------------------------------------------------------
# Display a summary report of all claims
# Shows total count, total amount, and a breakdown by status
# ----------------------------------------------------------
def summary_report():
    print("\n--- Claims Summary Report ---")
 
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return
 
    if len(lines) <= 1:
        print("No claims to summarize.")
        return
 
    total_count = 0
    total_amount = 0.0
    status_counts = {}
    status_amounts = {}
 
    for line in lines[1:]:
        data = line.strip().split(",")
        if len(data) < 4:
            continue
 
        total_count += 1
 
        # Safely parse the amount and add to running total
        try:
            amount = float(data[2])
            total_amount += amount
        except ValueError:
            amount = 0.0
 
        # Group counts and amounts by status for the breakdown section
        status = data[3].capitalize()
        status_counts[status] = status_counts.get(status, 0) + 1
        status_amounts[status] = status_amounts.get(status, 0.0) + amount
 
    # Display overall totals
    print(f"\nTotal Claims     : {total_count}")
    print(f"Total Amount     : ${total_amount:,.2f}")
    print(f"Average Amount   : ${(total_amount / total_count):,.2f}" if total_count > 0 else "Average Amount   : $0.00")
 
    # Display a per-status breakdown
    print("\n--- Breakdown by Status ---")
    print(f"{'Status':<15}{'Count':<10}{'Total Amount':<15}")
    print("-" * 40)
    for status, count in sorted(status_counts.items()):
        print(f"{status:<15}{count:<10}${status_amounts[status]:,.2f}")
 
# ----------------------------------------------------------
# Update an existing claim
# Automatically updates the Last Updated timestamp on save
# ----------------------------------------------------------
def update_claim():
    print("\n--- Update Claim ---")

    try:
        # Ask user for the claim ID they want to update
        claim_id = input("Enter Claim ID to update: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    # Track whether the entered claim ID exists so the user can be informed if not found
    updated = False

    try:
        # Read all existing data from the CSV file
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        # Rewrite the file with updated information
        with open(FILE_NAME, "w") as file:
            # Loop through all records to find and update the matching claim ID
            for line in lines:
                # Split each line into parts for easier comparison
                data = line.strip().split(",")

                # Check if this is the first line with column names and keep it unchanged
                if data[0] == "Claim ID":
                    file.write(line)
                    continue

                # Check if the current record matches the claim ID entered by the user
                if data[0] == claim_id:
                    print("Updating claim...")

                    try:
                        # Ask user for updated information for the selected claim
                        name = input(f"Enter new Patient Name [{data[1]}]: ").strip()
                        amount = input(f"Enter new Amount [{data[2]}]: ").strip()
                        status = input(f"Enter new Status [{data[3]}]: ").strip()

                        # Keep existing values if user leaves input blank
                        if name == "":
                            name = data[1]
                        if amount == "":
                            amount = data[2]
                        if status == "":
                            status = data[3]

                        # Validate amount to ensure it is numeric after update
                        if not is_valid_amount(amount):
                            print("Error: Amount must be numeric.")
                            return

                    except KeyboardInterrupt:
                        print("\nUpdate cancelled.")
                        return
                    
                    # Preserve original creation date; update the Last Updated timestamp
                    created = data[4] if len(data) > 4 else get_timestamp()
                    last_updated = get_timestamp()

                    # Write updated claim information to file
                    file.write(f"{claim_id},{name},{amount},{status},{created},{last_updated}\n")
                    updated = True
                else:
                    # Keep all other records unchanged
                    file.write(line)

        # Inform user whether update was successful or not
        if updated:
            print("Claim updated successfully. Last updated at: {get_timestamp()}")
        else:
            print("Error: Claim ID not found.")

    except FileNotFoundError:
        print("Error: File not found.")

# ----------------------------------------------------------
# Delete a claim
# ----------------------------------------------------------
def delete_claim():
    print("\n--- Delete Claim ---")

    try:
        # Ask user for the claim ID they want to delete
        claim_id = input("Enter Claim ID to delete: ").strip()
    except KeyboardInterrupt:
        print("\nInput interrupted. Returning to menu.")
        return

    # Ask for confirmation once before deleting
    confirm = input(f"Are you sure you want to delete claim {claim_id}? (y/n): ").lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    # Track whether the claim ID exists so the user can be informed if not found
    deleted = False

    try:
        # Read all existing data from the CSV file
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        # Rewrite file without the deleted claim
        with open(FILE_NAME, "w") as file:
            # Loop through all records and remove the matching claim ID
            for line in lines:
                data = line.strip().split(",")

                # Check if this is the first line with column names and keep it unchanged
                if data[0] == "Claim ID":
                    file.write(line)
                    continue

                # Check if current record matches the claim ID to delete
                if data[0] == claim_id:
                    deleted = True
                    continue
                else:
                    # Keep all other records unchanged
                    file.write(line)

        # Inform user whether deletion was successful or not
        if deleted:
            print("Claim deleted successfully.")
        else:
            print("Error: Claim ID not found.")

    except FileNotFoundError:
        print("Error: File not found.")

# ----------------------------------------------------------
# Main menu for user interaction
# ----------------------------------------------------------
def menu():
    # Continuously display options and allow user to interact with the system until they choose to exit
    while True:
        print("\n--- Insure Claim Tracker ---")
        print("1. Add Claim")
        print("2. View Claims")
        print("3. Update Claim")
        print("4. Delete Claim")
        print("5. Search / Filter Claims")
        print("6. Summary Report")
        print("7. Exit")

        try:
            # Get user choice for desired operation
            choice = input("Select an option: ").strip()
        except KeyboardInterrupt:
            print("\nProgram interrupted safely. Exiting.")
            break

        # Direct user to the correct function based on their choice
        if choice == "1":
            add_claim()
        elif choice == "2":
            view_claims()
        elif choice == "3":
            update_claim()
        elif choice == "4":
            delete_claim()
        elif choice == "5":
            search_claims()
        elif choice == "6":
            summary_report()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# ----------------------------------------------------------
# Entry point of the program
# ----------------------------------------------------------
if __name__ == "__main__":
    # Start the program by preparing the file and launching the menu
    initialize_file()
    menu()