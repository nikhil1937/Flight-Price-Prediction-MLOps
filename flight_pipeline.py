from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


# Define the DAG
with DAG(
    dag_id='flight_price_prediction_pipeline',
    start_date=datetime(2026, 11, 10),
    schedule=None,
    catchup=False,
    tags=['flight', 'machine-learning']
) as dag:

    # Task 1: Data ingestion
    data_ingestion = BashOperator(
        task_id='data_ingestion',
        bash_command='python /opt/airflow/project/ingest_data.py'
    )

    # Task 2: Data preprocessing
    data_preprocessing = BashOperator(
        task_id='data_preprocessing',
        bash_command='python /opt/airflow/project/preprocess.py'
    )

    # Task 3: Train-test splitting
    train_test_split = BashOperator(
        task_id='train_test_split',
        bash_command='python /opt/airflow/project/train-test-split.py'
    )

    # Task 4: Model training
    model_training = BashOperator(
        task_id='model_training',
        bash_command='python /opt/airflow/project/modeltraining.py'
    )

    # Task 5: Model performance evaluation
    performance_metrics = BashOperator(
        task_id='performance_metrics',
        bash_command='python /opt/airflow/project/performancemetrics.py'
    )

    # Define execution sequence
    data_ingestion >> data_preprocessing >> train_test_split >> model_training >> performance_metrics