import tasks
import json



def add_task(title, description="", start_date="", end_date="", status="open", subtasks=None, notes=None):
    if subtasks is None:
        subtasks = []
    if notes is None:
        notes = []

    task = tasks.Task(
        title=title,
        description=description,
        start_date=start_date,
        end_date=end_date,
        status=status,
        subtasks=json.dumps(subtasks),
        notes=json.dumps(notes)
    )

    tasks.session.add(task)
    tasks.session.commit()
    print(f"משימה '{title}' נוספה בהצלחה.")
