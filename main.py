from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks


def _list_all_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t.get("completed") else " "
        print(f"{i}. [{status}] {t['title']} (due: {t['due_date']})")


def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. List All Tasks")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            ok, res = add_task(title, description, due_date)
            if ok:
                print("Task added successfully!")
            else:
                print(res)

        elif choice == "2":
            if not tasks:
                print("No tasks to mark complete.")
                continue
            _list_all_tasks()
            idx = input("Enter task number to mark complete: ")
            ok, res = mark_task_as_complete(idx)
            if ok:
                print("Task marked as complete!")
            else:
                print(res)

        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks. Great job!")
            else:
                for i, t in enumerate(pending, start=1):
                    print(f"{i}. {t['title']} (due: {t['due_date']}) - {t['description']}")

        elif choice == "4":
            prog = calculate_progress()
            print(f"Progress: {prog}% completed")

        elif choice == "5":
            _list_all_tasks()

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
