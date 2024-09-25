from tasks import Task
from tasks import session
import json

def update_task(task_id, **kwargs):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"משימה עם ID {task_id} לא נמצאה.")
        return

    for key, value in kwargs.items():
        if key in ['subtasks', 'notes']:
            setattr(task, key, json.dumps(value))
        elif hasattr(task, key):
            setattr(task, key, value)
    session.commit()
    print(f"משימה {task_id} עודכנה בהצלחה.")
