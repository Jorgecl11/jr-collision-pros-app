# JR Collision Pros App

A Python command-line customer and vehicle intake system for a collision repair shop. Customer and vehicle records are stored locally in a SQLite database.

## Features

- Add a customer and their vehicle
- Add another vehicle to an existing customer
- Store customer and vehicle records in SQLite
- Prevent duplicate VINs and license plates
- Roll back failed customer and vehicle saves
- View all customer and vehicle records
- View the most recently added customer record
- Search customers by:
  - First name
  - Last name
  - Full name
  - License plate
  - VIN
  - Phone number
- Update a customer’s phone number
- Delete a vehicle while keeping the customer record
- Validate and format phone numbers
- Validate vehicle years
- Handle invalid menu input
- Continue running until the user selects Exit
- Test database behavior using an isolated temporary database

## Technologies

- Python
- SQLite
- pytest
- Git and GitHub

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Jorgecl11/jr-collision-pros-app.git
```

2. Enter the project directory:

```bash
cd jr-collision-pros-app
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

```powershell
python main.py
```

## Running Tests

Run the complete test suite:

```powershell
python -m pytest
```

The automated tests cover:

- Saving a customer and vehicle
- Rejecting duplicate VINs and rolling back partial data
- Rejecting duplicate license plates and rolling back partial data
- Deleting a vehicle while preserving its customer
- Adding another vehicle to an existing customer
- Storing vehicle information
- Displaying a vehicle summary
