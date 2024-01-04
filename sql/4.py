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
engine = create_engine(mysql_url)

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the "Order" class representing the "orders" table
class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    cust_name = Column(String)
    city = Column(String)
    grade = Column(Integer)
    salesman_id = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer)
    salesman_id = Column(Integer)

class Salesman(Base):
    __tablename__ = 'salesman'
    salesman_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    commission = Column(Float)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

result4a_query = """
    select c.cust_name, c.city, c.grade, s.name as salesman, o.ord_no, o.ord_date, o.purch_amt from customer c 
    LEFT JOIN salesman s ON c.salesman_id = s.salesman_id 
    LEFT JOIN orders o ON c.customer_id = o.customer_id 
    where (c.customer_id is not null AND o.purch_amt >= 2000) OR c.customer_id is null;
"""

result4a = session.execute(result4a_query)

# Create table format
table4a = PrettyTable()
table4a.field_names = ['cust_name', 'city','grade','salesman','ord_no','ord_date','purch_amt']

print("Result 4a")

for row in result4a:
    # Result rows added to the table
    table4a.add_row([row.cust_name,row.city,row.grade,row.salesman,row.ord_no,row.ord_date,row.purch_amt])

print(table4a)

result4b_query = """
    select c.cust_name, c.city, o.ord_no, o.ord_date, o.purch_amt from customer c 
    LEFT JOIN orders o ON c.customer_id = o.customer_id 
    where (c.grade is not null AND o.ord_no is not null) OR (c.grade is null AND o.ord_no is not null);
"""

result4b = session.execute(result4b_query)

# Create table format
table4b = PrettyTable()
table4b.field_names = ['cust_name', 'city','ord_no','ord_date','purch_amt']

print("Result 4b")

for row in result4b:
    # Result rows added to the table
    table4b.add_row([row.cust_name,row.city,row.ord_no,row.ord_date,row.purch_amt])

print(table4b)
# Close the session
session.close()