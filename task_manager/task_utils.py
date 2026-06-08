from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# In-memory list of tasks for this session
tasks = []


def add_task(title, description, due_date):
    """Validate input and add a task to the in-memory list.

    Returns (True, task) on success or (False, error_message) on failure.
    """
    ok, res = validate_task_title(title)
    if not ok:
        return False, res

    ok, res_desc = validate_task_description(description)
    if not ok:
        return False, res_desc

    ok, res_due = validate_due_date(due_date)
    if not ok:
        return False, res_due

    task = {
        "title": res,
        "description": res_desc,
        "due_date": res_due,
        "completed": False,
    }
    tasks.append(task)
    return True, task


def mark_task_as_complete(index, tasks_list=None):
    """Mark a task complete by 1-based index. Returns (True, task) or (False, error)."""
    if tasks_list is None:
        tasks_list = tasks
    try:
        idx = int(index)
    except Exception:
        return False, "Index must be an integer."
    if idx < 1 or idx > len(tasks_list):
        return False, "Index out of range."
    tasks_list[idx - 1]["completed"] = True
    return True, tasks_list[idx - 1]


def view_pending_tasks(tasks_list=None):
    """Return a list of pending (not completed) tasks."""
    if tasks_list is None:
        tasks_list = tasks
    return [t for t in tasks_list if not t.get("completed")]


def calculate_progress(tasks_list=None):
    """Return percent of tasks completed as float rounded to 2 decimals."""
    if tasks_list is None:
        tasks_list = tasks
    total = len(tasks_list)
    if total == 0:
        return 0.0
    completed = sum(1 for t in tasks_list if t.get("completed"))
    progress = (completed / total) * 100
    return round(progress, 2)
