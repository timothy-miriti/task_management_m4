from datetime import datetime


def validate_task_title(title):
    """Validate task title: non-empty string up to 100 chars.

    Returns the cleaned title or raises ValueError on invalid input.
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Title cannot be empty.")
    if len(cleaned) > 100:
        raise ValueError("Title must be 100 characters or fewer.")
    return cleaned


def validate_task_description(description):
    """Validate task description: string up to 500 chars.

    Returns the cleaned description or raises ValueError on invalid input.
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    cleaned = description.strip()
    if not cleaned:
        raise ValueError("Description cannot be empty.")
    if len(cleaned) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    return cleaned


def validate_due_date(due_date):
    """Validate due date in YYYY-MM-DD format.

    Returns the ISO-formatted date string or raises ValueError on invalid input.
    """
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string in YYYY-MM-DD format.")
    cleaned = due_date.strip()
    if not cleaned:
        raise ValueError("Due date cannot be empty.")
    try:
        parsed = datetime.strptime(cleaned, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return parsed.isoformat()
