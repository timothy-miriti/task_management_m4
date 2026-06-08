from datetime import datetime, date


def validate_task_title(title):
    """Validate task title: non-empty string up to 100 chars.

    Returns (True, cleaned_title) or (False, error_message).
    """
    if not isinstance(title, str):
        return False, "Title must be a string."
    cleaned = title.strip()
    if not cleaned:
        return False, "Title cannot be empty."
    if len(cleaned) > 100:
        return False, "Title must be 100 characters or fewer."
    return True, cleaned


def validate_task_description(description):
    """Validate task description: string up to 500 chars.

    Returns (True, cleaned_description) or (False, error_message).
    """
    if not isinstance(description, str):
        return False, "Description must be a string."
    cleaned = description.strip()
    if not cleaned:
        return False, "Description cannot be empty."
    if len(cleaned) > 500:
        return False, "Description must be 500 characters or fewer."
    return True, cleaned


def validate_due_date(due_date):
    """Validate due date in YYYY-MM-DD format and not in the past.

    Returns (True, iso_date_str) or (False, error_message).
    """
    if not isinstance(due_date, str):
        return False, "Due date must be a string in YYYY-MM-DD format."
    try:
        parsed = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    except Exception:
        return False, "Due date must be in YYYY-MM-DD format."
    if parsed < date.today():
        return False, "Due date cannot be in the past."
    return True, parsed.isoformat()
