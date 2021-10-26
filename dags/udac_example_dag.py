from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator, LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2021, 10, 25),
    'retries' : 0,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False,
    'depends_on_past': False,
    'catchup_by_default': False,
    'trigger_rule': 'all_success'
}

dag = DAG('udacity_college_football_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow'
          #schedule_interval='0 * * * *'
          #schedule_interval='@once'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)


create_table_playtype_to_redshift = StageToRedshiftOperator(
    task_id='create_playtype_table',
    dag=dag,
    redshift_conn_id = "redshift",
    sql="playtype_table_create",
    append_only=False,
    bash_command='exit 0'
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

# Execute tasks

start_operator >> create_table_playtype_to_redshift >> end_operator

