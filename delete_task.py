from tasks import Task
from tasks import session


def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"משימה עם ID {task_id} לא נמצאה.")
        return
    session.delete(task)
    session.commit()
    print(f"משימה {task_id} נמחקה בהצלחה.")
