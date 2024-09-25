from tasks import Task
from tasks import session

def list_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"ID: {task.id}, כותרת: {task.title}, סטטוס: {task.status}")
