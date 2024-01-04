from sqlalchemy import create_engine, Column, Integer, Numeric, Date, func,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
from sqlalchemy import inspect
from sqlalchemy import desc,asc
from prettytable import PrettyTable

# Database connection parameters
mysql_url = 'mysql+mysqlconnector://root:12345@localhost:3306/task'
print("Successfully connected to the database!...")
engine = create_engine(mysql_url)

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the "Order" class representing the "orders" table
class EmployeeHistory(Base):
    __tablename__ = 'employee_history'
    employee_id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    job_id = Column(String)
    department_id = Column(Integer)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#select employee_id from employee_history group by employee_id having COUNT(*)>=2;

# Perform the first select query
result3a = (
    session.query(EmployeeHistory.employee_id)
    .group_by(EmployeeHistory.employee_id)
    .having(func.count().label('count') >= 2)
    .all()
)


#create table format
table = PrettyTable()
table.field_names = ['employee_id']

print("Result 3a:")
for row in result3a:
    #result rows added to the table
    table.add_row([row.employee_id])
print(table)

# Close the session
session.close()
