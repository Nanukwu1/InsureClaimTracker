# ============================================
# INSURE CLAIM TRACKER SYSTEM
# Authors: Nini Anukwu, Gopi Kacha, Jordan Davis, Chinelo Aniekwu
# Description:
# This program allows users to manage insurance claims
# using Create, Read, Update, and Delete (CRUD) operations.
# Data is stored in a CSV file.
# ============================================


import os

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
# Initialize the CSV file if it does not exist
# ----------------------------------------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Claim ID,Patient Name,Amount,Status\n")

# ----------------------------------------------------------
# Add a new claim to the system by collecting user input
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

    # Save the new claim to the CSV file
    with open(FILE_NAME, "a") as file:
        file.write(f"{claim_id},{name},{amount},{status}\n")

    print("Claim added successfully.")

# ----------------------------------------------------------
# Display all stored claims from the CSV file
# ----------------------------------------------------------
def view_claims():
    print("\n--- All Claims ---")

    try:
        # Read stored data from the CSV file to display existing claims
           with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except Exception as e:
            print(f"Unexpected error: {e}")
            return

            # Check if file is empty, and inform user if no claims are found
            if len(lines) <= 1:
                print("No claims found.")
                return
            
            # Display formatted table for better readability
                print(f"{'ID':<10}{'Name':<20}{'Amount':<10}{'Status':<10}")
                print("-" * 50)

            # Loop through all records and display each claim to the user
            for line in lines[1:]:
                data = line.strip().split(",")
                print(f"{data[0]:<10}{data[1]:<20}{data[2]:<10}{data[3]:<10}")

    except FileNotFoundError:
        print("Error: File not found.")

# ----------------------------------------------------------
# Update an existing claim
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

                    # Write updated claim information to file
                    file.write(f"{claim_id},{name},{amount},{status}\n")
                    updated = True
                else:
                    # Keep all other records unchanged
                    file.write(line)

        # Inform user whether update was successful or not
        if updated:
            print("Claim updated successfully.")
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
                confirm = input(f"Are you sure you want to delete claim {claim_id}? (y/n): ").lower()
                if confirm != "y":
                    print("Deletion cancelled.")
                    return
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
        print("5. Exit")

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
