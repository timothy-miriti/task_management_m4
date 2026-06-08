"""Backward-compatible shim that delegates to task_manager.validation."""
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

__all__ = [
    "validate_task_title",
    "validate_task_description",
    "validate_due_date",
]