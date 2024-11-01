from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data storage for students
students = [
    {"id": 1, "name": "Alice", "grade": "A", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "grade": "B", "email": "bob@example.com"}
]

# Helper function to find a student by ID
def find_student(student_id):
    return next((student for student in students if student["id"] == student_id), None)

# GET /students - Retrieve a list of all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET /students/{id} - Retrieve details of a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = find_student(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": request.json["name"],
        "grade": request.json["grade"],
        "email": request.json["email"]
    }
    students.append(new_student)
    return jsonify(new_student), 201

# PUT /students/{id} - Update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = find_student(id)
    if student:
        student["name"] = request.json.get("name", student["name"])
        student["grade"] = request.json.get("grade", student["grade"])
        student["email"] = request.json.get("email", student["email"])
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

# DELETE /students/{id} - Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = find_student(id)
    if student:
        students.remove(student)
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
