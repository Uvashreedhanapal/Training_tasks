from sqlalchemy import create_engine, Column, Integer, Numeric, Date, func,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
from sqlalchemy import inspect
from sqlalchemy import desc,asc
from prettytable import PrettyTable
from sqlalchemy.orm import aliased

# Database connection parameters
mysql_url = 'mysql+mysqlconnector://root:12345@localhost:3306/task'
print("Successfully connected to the database!...")
engine = create_engine(mysql_url)   #echo=True -->used to log SQL statements.

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the "Order" class representing the "orders" table
class Employee(Base):
    __tablename__ = 'employee'
    emp_idno = Column(Integer, primary_key=True)
    emp_fname = Column(String)
    emp_lname = Column(String)
    emp_dept = Column(Integer)

class Department(Base):
    __tablename__ = 'department'
    dpt_code = Column(Integer, primary_key=True)
    dpt_name = Column(String)
    dpt_allotment = Column(Integer)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
# select emp_fname, emp_lname from employee where emp_dept in (select dpt_code from department where dpt_allotment > 50000);

# Perform the first select query
subquery = (
    session.query(Department.dpt_code)
    .filter(Department.dpt_allotment > 50000)
    .subquery()
)

# Main query to select emp_fname, emp_lname from employee where emp_dept in (subquery)
result5a= (
    session.query(Employee.emp_fname, Employee.emp_lname)
    .filter(Employee.emp_dept.in_(subquery))
    .all()
)


#create table format
table5a = PrettyTable()
table5a.field_names = ['emp_fname', 'emp_lname']

# Create table format for Result 5a
print("Result 5a:")
for row in result5a:
    # Result rows added to the table
    table5a.add_row([row.emp_fname, row.emp_lname])

print(table5a)

result5b_query = """
    SELECT emp_fname, emp_lname FROM employee 
    WHERE emp_dept IN ( SELECT dpt_code FROM department WHERE dpt_allotment= (SELECT MIN(dpt_allotment) FROM department 
    WHERE dpt_allotment > (SELECT MIN(dpt_allotment) FROM department )));
"""

result5b = session.execute(result5b_query)

# Create table format
table5b = PrettyTable()
table5b.field_names = ['emp_fname', 'emp_lname']

print("Result 5b")

for row in result5b:
    # Result rows added to the table
    table5b.add_row([row.emp_fname, row.emp_lname])

print(table5b)
# Close the session
session.close()
