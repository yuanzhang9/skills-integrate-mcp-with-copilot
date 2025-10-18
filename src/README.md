# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

1. Create and activate a virtual environment, then install the dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r ../requirements.txt
   ```

2. Initialize the database and seed initial data:

   ```bash
   # Creates a local SQLite DB file and seeds initial activities
   python src/seed_db.py
   ```

3. Run the application using Uvicorn:

   ```bash
   uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```
3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

Data is now persisted in `school.db` (SQLite). The in-memory store has been replaced by a SQLAlchemy backend, so activity and participant data will persist across restarts. To reset the database, delete `school.db` and re-run `python src/seed_db.py`.
