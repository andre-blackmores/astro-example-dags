from airflow.decorators import dag, task
from datetime import datetime
 
@dag(schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False, tags=["example"])
def simple_taskflow_dag():
 
    @task
    def calculate_square(number: int) -> int:
        return number ** 2
 
    @task
    def double_number(number: int) -> int:
        return number * 2
 
    @task
    def log_result(square: int, doubled: int):
        print(f"The square is {square} and the doubled value is {doubled}.")
 
    # Workflow
    number = 4  # Replace with any input
    square = calculate_square(number)
    doubled = double_number(square)
    log_result(square, doubled)
 
simple_dag = simple_taskflow_dag()