# Student Notes API README

Save the following content as `README.md` in your project root.

````markdown
# Student Notes API

A RESTful API built with FastAPI, SQLAlchemy, Pydantic, and SQLite for managing students and their notes.

## Features

- Create students
- Get all students
- Get a student by ID
- Create notes for a student
- Get all notes
- Get a note by ID
- Update notes
- Delete notes
- Automatic API documentation with Swagger UI

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

## Project Structure

```text
student_notes_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   └── crud.py
│
├── .gitignore
├── requirements.txt
└── README.md
````

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-notes-api.git
cd student-notes-api
```

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, open:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Students

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| POST   | `/students/`             | Create a student  |
| GET    | `/students/`             | Get all students  |
| GET    | `/students/{student_id}` | Get student by ID |

### Notes

| Method | Endpoint                        | Description                 |
| ------ | ------------------------------- | --------------------------- |
| POST   | `/students/{student_id}/notes/` | Create a note for a student |
| GET    | `/notes/`                       | Get all notes               |
| GET    | `/notes/{note_id}`              | Get note by ID              |
| PUT    | `/notes/{note_id}`              | Update a note               |
| DELETE | `/notes/{note_id}`              | Delete a note               |

## Example Request

### Create Student

```json
{
  "name": "Harman",
  "email": "harman@example.com"
}
```

### Create Note

```json
{
  "title": "FastAPI Basics",
  "content": "Learn routing, schemas, and SQLAlchemy."
}
```

## Example Response

```json
{
  "id": 1,
  "title": "FastAPI Basics",
  "content": "Learn routing, schemas, and SQLAlchemy.",
  "student_id": 1
}
```

## Key Concepts Practiced

* REST API development
* CRUD operations
* SQLAlchemy ORM models
* One-to-many relationships
* Pydantic schemas
* Dependency injection
* Error handling
* Automatic API documentation

## Future Improvements

* JWT Authentication
* PostgreSQL support
* Docker containerization
* Deployment on Render
* Pagination and filtering

## Author

Harman Dhiman

```
```
