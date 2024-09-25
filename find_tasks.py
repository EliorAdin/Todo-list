from tasks import Task
from tasks import session

def find_tasks_by_status(status):
    tasks = session.query(Task).filter(Task.status == status).all()
    for task in tasks:
        print(f"ID: {task.id}, כותרת: {task.title}, סטטוס: {task.status}")