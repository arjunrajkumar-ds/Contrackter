import json
from datetime import datetime

# File that stores work logs
DATA_FILE = "contrackter_data.json"



# Loads existing data (or creates empty structure)
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# Saves data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent = 4)

# Function to add an entry to file
def add_entry(date, hours, pay, gst, client_name, address):
    data = load_data()
    entry = {
        "date": date, 
        "hours": hours, 
        "pay": pay, 
        "GST": gst,
        "client_name": client_name,
        "address": address
        }
    data.append(entry)
    save_data(data)
    print("Entry added successfully")

# Format for input lines:
# "DD/MM/YYYY, <# of hours worked>, <pay>, <GST>"

def main():
    while True:
        try:
            date = input("Date (DD/MM/YYYY): ").strip()
            hours = float(input("Hours worked: ").strip())
            pay = float(input("Pay: ").strip())
            gst = pay * 0.10 # GST at 10%
            client_name = input("Client's first name: ").strip()
            address = input("Client's address: ")
            add_entry(date, hours, pay, gst, client_name, address)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break
        except ValueError:
            print("Invalid input. Try again")

main()