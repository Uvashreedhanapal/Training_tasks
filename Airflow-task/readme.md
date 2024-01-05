Airflow Concepts:
==================
DAGS:
-----
--> a python(.py) file that defines what the steps are in our workflow. Each DAG has some common configuration and details of what task needs to be executed at each step.
-->are placed in Airflow’s DAG_FOLDER
default_args: A dictionary of default parameters to be used by all tasks in the DAG.

Default arguments in DAG:
owner: The person or team responsible for the DAG.
start_date: The date and time when the DAG should start running. Tasks in the DAG won't run until this date and time.
retries: The number of times a task should be retried in case of a failure.
retry_delay: The time to wait between retries.

schedule_interval: The frequency with which to run the DAG. It can be a timedelta or a cron expression.
catchup: For example, if you have a DAG scheduled to run daily and you set catchup to True, and the DAG is paused for a week, when you resume the DAG, Airflow will try to execute tasks for each of the days during the pause period.

--------------------------------------------------------------------------------------------------------------------
operators:

Tasks are executed using Airflow operators. Operators are actually execute scripts, commands, and other operations when a Task is executed
    BashOperator - executes a bash command
    PythonOperator - calls an arbitrary Python function
    EmailOperator - sends an email
    SimpleHttpOperator - sends an HTTP request
    MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, JdbcOperator, etc. - executes a SQL command
    Sensor - an Operator that waits (polls) for a certain time, file, database row, S3 key
-------------------------------------------------------------------------------------------------------------
Airflow scheduler:
The Airflow Scheduler is constantly monitoring and executing DAGs every n seconds. The scheduler also has an internal component called Executor. The executor is responsible for spinning up workers and executing the task to completion.
--------------------------------------------------------------------------------------------------------------
executors:
Executors are what Airflow uses to run tasks that the Scheduler determines are ready to run. By default, Airflow uses the SequentialExecutor.other executors local executor,kubernetes executor,celery executor
----------------------------------------------------------------------------------------------------------------
Variables:
Variables are a generic way to store and retrieve arbitrary content or settings as a simple key value store within Airflow. 
There are several ways to create Airflow variables:
1)Using the Airflow UI
    To create an Airflow variable in the UI, click on the Admin tab and select Variables. Then click on the + button and enter a key, value and an optional description for your Airflow variable. You also have the option to Import Variables from a file.

2)Using the Airflow CLI.
    The Airflow CLI contains options to set, get and delete Airflow variables. To create an Airflow variable via the CLI use the following command:
        airflow variables set my_var my_value
        airflow variables set -j my_json_var '{"key": "value"}'

3)Using an environment variable.
    To set Airflow variables using an environment variable, create an environment variable with the prefix AIRFLOW_VAR_ and the name of the Airflow variable you want to set. For example:
        AIRFLOW_VAR_MYREGULARVAR='my_value'
        AIRFLOW_VAR_MYJSONVAR='{"hello":"world"}'
        Variable.get('<VAR_NAME>', '<default-value>'): This method is recommended and the most secure for fetching secret values.

4)Programmatically from within an Airflow task.
    you can programmatically set Airflow variables within your Airflow tasks via the Variable model. If you want to serialize a JSON value, make sure to set serialize_json=True.
        def set_var_func():
            from airflow.models import Variable
            Variable.set(key="my_regular_var", value="Hello!")
            Variable.set(key="my_json_var", value={"num1": 23, "num2": 42}, serialize_json=True)
-------------------------------------------------------------------------------------------------------------------

The following are the steps by step to write an Airflow DAG or workflow:
    Creating a python file
    Importing the modules
    Default Arguments for the DAG
    Instantiate a DAG
    Creating a callable function
    Creating Tasks
    Setting up Dependencies
    Verifying the final Dag code
    Test the Pipeline
    Running the DAG
-------------------------------------------------------------------------------------------------------------------
To configure a PostgreSQL database for Airflow, you must create a connection to the database in Airflow. You can do this by following these steps-

    Open the Airflow web UI and go to the Admin page.
    Click on the Connections tab, followed by the Create button.
    Select Postgres from the Connection type drop-down menu.
    Enter the following information-
    Connection ID: A unique identifier for the connection.
    Host: The hostname or IP address of the PostgreSQL database server.if you are using airflow from docker -->host.docker.internal
    Port: The port number of the PostgreSQL database server.
    Database: The name of the PostgreSQL database.
    Login: The username to use to connect to the PostgreSQL database.
    Password: The password to use to connect to the PostgreSQL database.
    Click on the Test Connection button to ensure that the connection is successful.
    Click on the Save button to create the connection.