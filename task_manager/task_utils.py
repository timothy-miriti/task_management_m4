from .validation import validate_task_title, validate_task_description, validate_due_date

# In-memory list of tasks for this session
tasks = []


def add_task(title, description, due_date):
    """Validate input and add a task to the in-memory list.

    Returns (True, task) on success or (False, error_message) on failure.
    """
    try:
        cleaned_title = validate_task_title(title)
        cleaned_description = validate_task_description(description)
        cleaned_due_date = validate_due_date(due_date)
    except ValueError as exc:
        return False, str(exc)

    task = {
        "title": cleaned_title,
        "description": cleaned_description,
        "due_date": cleaned_due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, task


def mark_task_as_complete(index, tasks_list=None):
    """Mark a task complete by 1-based index."""
    if tasks_list is None:
        tasks_list = tasks
    try:
        idx = int(index)
    except (TypeError, ValueError):
        return False, "Index must be an integer."
    if idx < 1 or idx > len(tasks_list):
        return False, "Index out of range."
    tasks_list[idx - 1]["completed"] = True
    return True, tasks_list[idx - 1]


def view_pending_tasks(tasks_list=None):
    """Return a list of pending tasks that are not complete."""
    if tasks_list is None:
        tasks_list = tasks
    return [task for task in tasks_list if not task.get("completed")]


def calculate_progress(tasks_list=None):
    """Calculate percent of tasks completed."""
    if tasks_list is None:
        tasks_list = tasks
    total = len(tasks_list)
    if total == 0:
        return 0.0
    completed = sum(1 for task in tasks_list if task.get("completed"))
    return round((completed / total) * 100, 2)


__all__ = [
    "add_task",
    "mark_task_as_complete",
    "view_pending_tasks",
    "calculate_progress",
    "tasks",
]
