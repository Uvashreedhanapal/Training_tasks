from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator



default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=4),
}

dag = DAG(
    'insert_purchase_details',
    default_args=default_args,
    schedule_interval='*/4 * * * *',  # Run every 4 minutes
    # schedule_interval=None
)

# Use Orders and Product_returns tables to get total_orders and total_returns of each customer and insert the details in the Purchase_details table for every 4 mins.
# Use current timestamp for created_time column

insert_purchase_details = PostgresOperator(
    task_id="insert_purchase_details_task",
    postgres_conn_id="postgres",
    sql="""

    INSERT INTO Purchase_details (customer_id, total_orders, total_returns, created_time)
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.order_id) AS total_orders,
        COUNT(DISTINCT pr.return_id) AS total_returns,
        NOW() AS created_time
    FROM
        orders o
    LEFT JOIN
        product_returns pr ON o.customer_id = pr.customer_id
    GROUP BY
        o.customer_id;
    """,
    dag=dag
)

#set task dependencies 
insert_purchase_details
