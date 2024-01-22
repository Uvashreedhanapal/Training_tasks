from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        result = a + b
        return f'The Result: {result}'
    else:
        return 'Error: Please provide value for the parameters "a" and "b".'

@app.route('/netamt', methods=['POST'])
def net_amount():
    try:
        data = request.get_json()
        net_amount = data.get('net_amount')
        mode = data.get('mode')
        amount = data.get('amount')

        if mode == 'deposit':
            net_amount += amount
        elif mode == 'withdraw':
            net_amount -= amount
        else:
            return jsonify(error='Invalid input...use deposit or withdraw')

        return jsonify(f'The current balance amount is {net_amount}')

    except Exception as e:
        return jsonify(error=f'Error processing the request: {str(e)}')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@host.docker.internal:5432/sample_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000))
    designation = db.Column(db.String(1000))
    salary = db.Column(db.Integer())

# db.create_all()

# Decorator for handling exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return wrapper

# Decorator for common validation checks
def validate_input(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if 'name' not in data or 'designation' not in data or 'salary' not in data:
            return jsonify({'message': 'Missing required fields (name, designation, salary)'}), 400
        if data['salary'] < 0:
            return jsonify({'message': 'Invalid input for salary'}), 400
        return func(*args, **kwargs)
    return wrapper

# Add data to the created table
@app.route('/employees', methods=['POST'] ,endpoint='add_employee_endpoint')
@handle_exceptions
@validate_input
def add_employee():
    data = request.get_json()
    new_employee = Employee(id=data['id'], name=data['name'], designation=data['designation'], salary=data['salary'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully'})

# Get all employee details
@app.route('/employees', methods=['GET'], endpoint='get_employees_endpoint')
@handle_exceptions
def get_employees():
    employees = Employee.query.all()
    employee_list = [{'id': employee.id, 'name': employee.name, 'designation': employee.designation, 'salary': employee.salary} for employee in employees]
    return jsonify({'employees': employee_list})

# Get specific employee details using employee id
@app.route('/employees/<int:employee_id>', methods=['GET'], endpoint='get_employee_endpoint')
@handle_exceptions
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        return jsonify({'id': employee.id, 'name': employee.name, 'designation': employee.designation, 'salary': employee.salary})
    return jsonify({'message': 'Employee not found'})

# Update employee details
@app.route('/employees/<int:employee_id>', methods=['PUT'],endpoint='update_employee_endpoint')
@validate_input
@handle_exceptions
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'})

    data = request.get_json()
    employee.name = data['name']
    employee.designation = data['designation']
    employee.salary = data['salary']
    db.session.commit()

    return jsonify({'message': 'Employee updated successfully'})


# Delete specific data using employee id
@app.route('/employees/<int:employee_id>', methods=['DELETE'], endpoint='delete_employee_endpoint')
@handle_exceptions
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'})
    db.session.delete(employee)
    db.session.commit()

    return jsonify({'message': 'Employee deleted successfully'})

# Delete all data in table
@app.route('/employees', methods=['DELETE'], endpoint='delete_employees_endpoint')
@handle_exceptions
def delete_employee():
    employee = Employee.query.all()
    for employee in employee:
            db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'All employee details deleted successfully'})

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
