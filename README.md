
# Student Management REST API

A simple REST API for managing `Student` records, built with **Flask**. Supports CRUD operations.

## Setup

1. **Clone**:
   ```bash
   git clone <repository-url> && cd <repository-directory>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

## Run Locally

1. **Start the Flask App**:
   ```bash
   python app.py
   ```

2. **Access API**: `http://127.0.0.1:5000`

## Endpoints

- **GET /students**: Retrieve all students
- **GET /students/{id}**: Retrieve a student by ID
- **POST /students**: Add a new student
- **PUT /students/{id}**: Update a student by ID
- **DELETE /students/{id}**: Delete a student by ID

## Testing

Use `test-api.http` for testing with VS Code REST Client or Postman.

---
