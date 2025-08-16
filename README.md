# Contacts Application

This application is a simple contact management system with a React frontend and a Python backend.

## Directory Structure

```
.
├── backend                 # Python FastAPI backend
├── frontend                # React frontend
├── scripts                 # Shell scripts for common operations
├── guidelines.md           # Project guidelines
├── spec.md                 # Project specifications
└── README.md               # This file
```

## Backend

The backend is a Python application built with FastAPI. It provides a REST API for managing contacts.

### Dependencies

*   `fastapi`
*   `uvicorn[standard]`
*   `pytest`
*   `pydantic[email]`

### Setup and Usage

1.  Navigate to the project root directory.
2.  Install the dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```
3.  Run the application:
    ```bash
    uvicorn backend.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

### Testing

To run the backend tests, navigate to the project root directory and run:

```bash
pytest backend/test_unit.py
pytest backend/test_integration.py
```

## Frontend

The frontend is a React application.

### Dependencies

*   `@testing-library/dom`
*   `@testing-library/jest-dom`
*   `@testing-library/react`
*   `@testing-library/user-event`
*   `react`
*   `react-dom`
*   `react-scripts`
*   `web-vitals`

### Setup and Usage

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the dependencies:
    ```bash
    npm install
    ```
3.  Run the application:
    ```bash
    npm start
    ```

The application will be available at `http://localhost:3000`.

### Testing

To run the frontend tests, navigate to the `frontend` directory and run:

```bash
npm test
```

## Scripts

The `scripts/` directory contains utility shell scripts for common operations:

*   `create_contact.sh`: Script to create a new contact.
*   `delete_contact.sh`: Script to delete an existing contact.
*   `list_contacts.sh`: Script to list all contacts.