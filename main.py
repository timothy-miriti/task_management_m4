from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks


def _list_all_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task.get("completed") else " "
        print(f"{i}. [{status}] {task['title']} (due: {task['due_date']})")


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            ok, result = add_task(title, description, due_date)
            if ok:
                print("Task added successfully!")
            else:
                print(result)

        elif choice == "2":
            if not tasks:
                print("No tasks to mark complete.")
                continue
            _list_all_tasks()
            idx = input("Enter task number to mark complete: ")
            ok, result = mark_task_as_complete(idx)
            if ok:
                print("Task marked as complete!")
            else:
                print(result)

        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks. Great job!")
            else:
                for i, task in enumerate(pending, start=1):
                    print(f"{i}. {task['title']} (due: {task['due_date']}) - {task['description']}")

        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress}% completed")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
