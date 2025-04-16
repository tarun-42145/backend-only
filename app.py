from flask import Flask, request, jsonify
import database

app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = database.get_employees()
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    if not name or not role:
        return jsonify({'error': 'Missing name or role'}), 400
    emp_id = database.add_employee(name, role)
    return jsonify({'id': emp_id, 'name': name, 'role': role}), 201

@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    success = database.delete_employee(emp_id)
    if success:
        return jsonify({'message': 'Deleted'}), 200
    return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)
