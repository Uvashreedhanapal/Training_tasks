from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/sample_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000))
    designation = db.Column(db.String(1000))
    salary = db.Column(db.Integer())
db.create_all()

#add data to the created table
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    # validation checks
    if 'name' not in data or 'designation' not in data or 'salary' not in data:
        return jsonify({'message': 'Missing required fields (name, designation, salary)'})
    if data['salary'] < 0:
        return jsonify({'message':'Invalid input for salary'})
    
    new_employee = Employee(id=data['id'],name=data['name'], designation=data['designation'], salary=data['salary'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message':'Employee added successfully'})

#to get all the employee details
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_list.append({'id': employee.id, 'name': employee.name, 'designation': employee.designation, 'salary': employee.salary})
    return jsonify({'employees': employee_list})

#to get specific employee details using employee id
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        return jsonify({'id': employee.id, 'name': employee.name, 'designation': employee.designation, 'salary': employee.salary})
    return jsonify({'message': 'Employee not found'})

#update employee details 
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    #validation check
    if not employee:
        return jsonify({'message': 'Employee not found'})

    data = request.get_json()
    employee.name = data['name']
    employee.designation = data['designation']
    employee.salary = data['salary']
    db.session.commit()

    return jsonify({'message': 'Employee updated successfully'})

#delete specific data using employee id
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'Employee not found'})

    db.session.delete(employee)
    db.session.commit()

    return jsonify({'message':'Employee deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
