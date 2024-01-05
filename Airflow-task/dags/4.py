from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Define the default_args for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
dag = DAG(
    'insert_data',
    default_args=default_args,
    schedule_interval='*/2 * * * *',  # Run every 2 minutes
    # schedule_interval=None,
    catchup=False
)
# task to insert 2 rows in the Orders and Product_returns table for every 2 minutes. 
insert_data = PostgresOperator(
    task_id="insert_data_orders",
    postgres_conn_id="postgres",
    sql="""
        INSERT INTO orders (customer_id, order_date)
        SELECT customer_id, NOW()
        FROM customers
        ORDER BY RANDOM()
        LIMIT 2;
    """,
    dag=dag
)
insert_data = PostgresOperator(
    task_id="insert_data_product",
    postgres_conn_id="postgres",
    sql="""
        INSERT INTO product_returns (customer_id, return_date)
        SELECT customer_id, NOW()
        FROM customers
        ORDER BY RANDOM()
        LIMIT 2;
    """,
    dag=dag
)

 # Set task dependencies for parallel execution
# [task_add, task_subtract, task_multiply]
