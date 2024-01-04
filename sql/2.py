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
class Salesman(Base):
    __tablename__ = 'salesman'
    salesman_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    commission = Column(Float)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# select * from salesman where (commission > 0.10 AND commission < 0.12);
# Perform the first select query
result2a = (
    session.query(Salesman)
    .filter(Salesman.commission.between(0.10, 0.12))
    .all()
)


#create table format
table = PrettyTable()
table.field_names = ['Salesman ID', 'name','city','commission']

print("Result 1a:")
for row in result2a:
    #result rows added to the table
    table.add_row([row.salesman_id,row.name,row.city ,row.commission])
print(table)

#select AVG(commission) as avg_commission from salesman   where commission between 0.12 AND 0.14;
# Perform the first select query
result2b = (
    session.query(func.avg(Salesman.commission).label('avg_commission'))
    .filter(Salesman.commission.between(0.12, 0.14))
    .first()
)



#create table format
table1 = PrettyTable()
table1.field_names = ['avg_commission']

print("Result 2b:")
for row in result2b:
    #result rows added to the table
    avg_commission = result2b.avg_commission
    table1.add_row([avg_commission])
print(table1)


# Close the session
session.close()
