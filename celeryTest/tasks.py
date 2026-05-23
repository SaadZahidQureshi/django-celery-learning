from celery import shared_task

@shared_task
def test_periodic_task():
    print("Periodic task executed!")
    return "Success"



@shared_task
def debug_task():
    print("--- WINDOWS WORKER SUCCESS ---")
    return "Task Complete"
