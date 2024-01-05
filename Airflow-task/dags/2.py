from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
import functions

dag = DAG(
    'word_length_dag',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)


# task_get_input = PythonOperator(
#     task_id='get_input',
#     python_callable=functions.get_input,
#     dag=dag,
# )

# task_get_word_counts = PythonOperator(
#     task_id='get_word_counts',
#     python_callable=functions.get_word_counts,
#     op_args=[task_get_input.output],
#     dag=dag,
# )

# # Set task dependencies
# task_get_input >> task_get_word_counts


# Task 1: Set Input Data in Airflow Variable from the Web UI
def get_input(**kwargs):
    input_data = Variable.get('input_data')
    return input_data


task_set_input = PythonOperator(
    task_id='get_input',
    python_callable=get_input,
    provide_context=True,
    dag=dag,
)

# Task 2: Get Word Counts and Store in Dictionary
def get_word_counts(**kwargs):
    ti = kwargs['ti']  # Get the TaskInstance object
    input_data = Variable.get('input_data',deserialize_json=True)
    word_lengths = {word: len(word) for word in input_data}
    print(word_lengths)

task_get_word_counts = PythonOperator(
    task_id='get_word_counts',
    python_callable=get_word_counts,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
task_set_input >> task_get_word_counts