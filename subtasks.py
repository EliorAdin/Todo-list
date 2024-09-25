from tasks import Task
from tasks import session
import json

def add_subtask(task_id, subtask_title):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"משימה עם ID {task_id} לא נמצאה.")
        return

    subtasks = json.loads(task.subtasks) if task.subtasks else []
    subtasks.append({"title": subtask_title, "completed": False})
    task.subtasks = json.dumps(subtasks)
    session.commit()
    print(f"תת-משימה '{subtask_title}' נוספה למשימה {task_id}.")


def update_subtask(task_id, subtask_index, completed=True):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"משימה עם ID {task_id} לא נמצאה.")
        return

    subtasks = json.loads(task.subtasks) if task.subtasks else []
    if subtask_index < 0 or subtask_index >= len(subtasks):
        print("אינדקס תת-משימה לא תקין.")
        return

    subtasks[subtask_index]['completed'] = completed
    task.subtasks = json.dumps(subtasks)
    session.commit()
    print(f"סטטוס תת-משימה {subtask_index} עודכן ל-{completed}.")


def export_tasks_to_json(file_path='tasks_export.json'):
    tasks = session.query(Task).all()
    tasks_list = []
    for task in tasks:
        tasks_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "status": task.status,
            "subtasks": json.loads(task.subtasks) if task.subtasks else [],
            "notes": json.loads(task.notes) if task.notes else []
        })

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(tasks_list, f, ensure_ascii=False, indent=4)
    print(f"כל המשימות ייוצאו לקובץ {file_path}.")
