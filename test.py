import csv

TempDataInt = []

def loop_through_usernames(username):
    global TempDataInt
    with open('user_data.csv', 'r', newline='') as readingfile:
        reader = csv.DictReader(readingfile)
        for row in reader:
            if row['Username'].strip() == username.strip():
                TempDataInt.append(row)  # Append the entire row for later use
                break  # Stop the loop once the username is found

def CheckingScores():
    global TempDataInt
    if not TempDataInt:
        print("No matching row found to update")
        return

    row = TempDataInt[0]  # Get the row for the username
    if not row['TestResult1'].strip():  # Check if TestResult1 is empty
        row['TestResult1'] = '11'  # Update the value if empty
    
    write_updated_data(row)

def write_updated_data(updated_row):
    rows = []
    fieldnames = None

    # Read the current data and collect rows
    with open('user_data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            if row['Username'].strip() == updated_row['Username'].strip():
                rows.append(updated_row)  # Append the updated row
            else:
                rows.append(row)  # Append unchanged rows

    # Write the updated data back to the file
    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Example usage:
username = 'Ignatius'
loop_through_usernames(username)
CheckingScores()
