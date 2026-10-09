# JR Collision Pros App

A Python customer and vehicle intake system for a collision repair shop, featuring a command-line interface (CLI) and an in-development REST API built with FastAPI.

Customer and vehicle records are stored locally in a SQLite database.

## Features

### Command-Line Application

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
- Update a customer's phone number
- Delete a vehicle while keeping the customer record
- Validate and format phone numbers
- Validate vehicle years
- Handle invalid menu input
- Continue running until the user selects Exit

### REST API (In Development)

- Run an HTTP API using FastAPI and Uvicorn
- Retrieve customer and vehicle records from SQLite
- Return database records as JSON
- Explore and test endpoints using Swagger UI

Currently implemented endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/vehicles` | Returns customer and vehicle records from SQLite |

The API currently provides read-only access. Creating, updating, and deleting records through HTTP are not yet implemented.

## Technologies

- Python
- SQLite
- FastAPI
- Uvicorn
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

## Running the Command-Line Application

From the project directory:

```powershell
python main.py
```

Follow the interactive menu to manage customer and vehicle records.

## Running the REST API

Start the FastAPI development server:

```powershell
uvicorn api:app --reload --port 1990
```

Once the server is running, open:

- API root: http://127.0.0.1:1990/
- Interactive API documentation: http://127.0.0.1:1990/docs
- Vehicle listing: http://127.0.0.1:1990/vehicles

### Example API Response

A successful `GET /vehicles` request returns HTTP `200 OK` with JSON similar to:

```json
{
  "vehicles": [
    {
      "customer_id": 1,
      "first_name": "Example",
      "last_name": "Customer",
      "phone": "408-555-0100",
      "year": 2025,
      "make": "Toyota",
      "model": "Camry",
      "vin": "EXAMPLEVIN123",
      "license_plate": "EXAMPLE1"
    }
  ]
}
```

The actual response depends on the records stored in the local SQLite database.

**Note:** The API is currently intended for local development. Authentication and authorization have not yet been implemented. Do not expose it publicly or use it to serve real customer data over an untrusted network.

## Running Tests

Run the complete test suite:

```powershell
python -m pytest
```

The existing automated tests cover:

- Saving a customer and vehicle
- Rejecting duplicate VINs and rolling back partial data
- Rejecting duplicate license plates and rolling back partial data
- Deleting a vehicle while preserving its customer
- Adding another vehicle to an existing customer
- Storing vehicle information
- Displaying a vehicle summary

Database tests use an isolated temporary database to avoid modifying application records.

Automated API endpoint tests have not yet been added.

## Development Status

JR Collision Pros is an ongoing software engineering project.

The command-line application and initial FastAPI integration are implemented. Planned development includes improved API data retrieval, additional REST endpoints, request validation, automated API testing, and security controls before any production deployment.