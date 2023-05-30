from functools import partial
from random import seed
from uuid import uuid4

from controller import run_job

def main(job_id: str) -> None:
    print(f"Starting job: {job_id}")

    task_callback = partial(task_completed_callback_handler, job_id)
    job_callback = partial(job_completed_callback_handler, job_id)

    task_data = [
        {"task_id": i, "number": i} for i in range(10)
    ]

    run_job(task_data, task_callback, job_callback)


def task_completed_callback_handler(job_id: str, callback_message: dict) -> None:
    print(f"Task completed in {job_id = }: {callback_message = }")


def job_completed_callback_handler(job_id: str, callback_message: dict) -> None:
    print(f"Job {job_id} completed: {callback_message}")
