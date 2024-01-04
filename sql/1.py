from sqlalchemy import create_engine, Column, Integer, Numeric, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
from sqlalchemy import inspect
from sqlalchemy import desc,asc
from prettytable import PrettyTable

# Database connection parameters
mysql_url = 'mysql+mysqlconnector://root:12345@localhost:3306/task1'
print("Successfully connected to the database!...")
engine = create_engine(mysql_url)

# Create an SQLAlchemy base class
Base = declarative_base()

# Define the "Order" class representing the "orders" table
class Order(Base):
    __tablename__ = 'orders'
    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer)
    salesman_id = Column(Integer)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#select distinct salesman_id,max(purch_amt) as max_purchase from orders where purch_amt<=2000 group by salesman_id order by max_purchase desc limit 5;
# Perform the first select query
result1a = (
    session.query(Order.salesman_id, func.max(Order.purch_amt).label('max_purchase'))
    .filter(Order.purch_amt < 2000)
    .group_by(Order.salesman_id)
    .order_by(desc('max_purchase') )
    .limit(5)
    .all()
)

#create table format
table = PrettyTable()
table.field_names = ['Salesman ID', 'Max Purchase']

print("Result 1a:")
for row in result1a:
    #result rows added to the table
    table.add_row([row.salesman_id, row.max_purchase])
print(table)

#select distinct salesman_id,min(purch_amt) as min_purchase from orders where purch_amt<=100 group by salesman_id order by min_purchase desc limit 5;
# Perform the second select query
result1b = (
    session.query(Order.salesman_id, func.min(Order.purch_amt).label('min_purchase'))
    .filter(Order.purch_amt > 100)
    .group_by(Order.salesman_id)
    .order_by(asc('min_purchase'))
    .limit(5)
    .all()
)

print("Result 1b:")
#create table format
table1 = PrettyTable()
table1.field_names = ['Salesman ID', 'Min Purchase']

for row in result1b:
    table1.add_row([row.salesman_id, row.min_purchase])
print(table1)
# Close the session
session.close()
