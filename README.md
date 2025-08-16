# Contacts Application

This application is a simple contact management system with a React frontend and a Python backend.

## Directory Structure

```
.
├── backend
│   ├── main.py         # FastAPI application
│   ├── test_main.py    # Backend unit tests
│   └── requirements.txt  # Python dependencies
├── frontend
│   ├── public
│   ├── src
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.js
│   │   └── ... (other React components)
│   ├── package.json
│   └── ...
├── guidelines.md
├── spec.md
└── README.md
```

## Backend

The backend is a Python application built with FastAPI. It provides a REST API for managing contacts.

### Setup and Usage

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

### Testing

To run the backend tests, navigate to the `backend` directory and run:

```bash
pytest
```

## Frontend

The frontend is a React application.

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
