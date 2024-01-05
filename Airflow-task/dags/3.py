# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
import functions
# dag = DAG(
#     'calci_dag',
#     schedule_interval=None,
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
# )

# # Define values for the operations
# a, b, c, d, e, f = 5, 3, 8, 2, 4, 6

# # Task 1: Add values a and b
# def add_values(**kwargs):
#     print(f'value for a: {a}')
#     print(f'value for b: {b}')
#     result = a + b
#     print(f"Addition Result: {result}")

# task_add = PythonOperator(
#     task_id='add_values',
#     python_callable=add_values,
#     dag=dag,
# )

# # Task 2: Subtract values c and d
# def subtract_values(**kwargs):
#     print(f'value for c: {c}')
#     print(f'value for d: {d}')
#     result = c - d
#     print(f"Subtraction Result: {result}")

# task_subtract = PythonOperator(
#     task_id='subtract_values',
#     python_callable=subtract_values,
#     dag=dag,
# )

# # Task 3: Multiply values e and f
# def multiply_values(**kwargs):
#     print(f'value for e: {e}')
#     print(f'value for f: {f}')
#     result = e * f
#     print(f"Multiplication Result: {result}")

# task_multiply = PythonOperator(
#     task_id='multiply_values',
#     python_callable=multiply_values,
#     dag=dag,
# )

# # Set task dependencies for parallel execution
# [task_add, task_subtract, task_multiply]

# # Set task dependencies for sequential execution
# #task_add >> task_subtract >> task_multiply

# code to get input from airflow web UI


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

dag = DAG(
    'calci_dag',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)



task_add = PythonOperator(
    task_id='add_values',
    python_callable=functions.add_values,
    dag=dag,
)



task_subtract = PythonOperator(
    task_id='subtract_values',
    python_callable=functions.subtract_values,
    dag=dag,
)

task_multiply = PythonOperator(
    task_id='multiply_values',
    python_callable=functions.multiply_values,
    dag=dag,
)

# Set task dependencies for parallel execution
[task_add, task_subtract, task_multiply]

# Set task dependencies for sequential execution
#task_add >> task_subtract >> task_multiply