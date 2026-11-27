# Written config only. Airflow was not installed or run in the lesson.
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def step(name):
    print(name)

with DAG("etl", start_date=datetime(2026, 1, 1), schedule="@daily") as dag:
    a = PythonOperator(task_id="extract", python_callable=step, op_args=["extract"])
    b = PythonOperator(task_id="transform", python_callable=step, op_args=["transform"])
    c = PythonOperator(task_id="load", python_callable=step, op_args=["load"])
    a >> b >> c
