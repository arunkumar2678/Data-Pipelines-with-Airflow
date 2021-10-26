  
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator


class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
   
    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 sql='',
                 *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.redshift_conn = redshift_conn_id
        self.sql = sql

    def execute(self, context):
        redshift = PostgresHook(self.redshift_conn)
        redshift.run(self.sql)
