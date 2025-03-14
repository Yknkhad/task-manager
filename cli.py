import sys
from functions import (
    add_user, list_users, delete_user, 
    add_task, assign_task, mark_task_completed, 
    view_tasks_by_user, add_category, 
    delete_task, view_all_tasks  # Added delete_task and view_all_tasks
)

def print_menu():
    print("\nTask Manager CLI")
    print("1. User Management")
    print("2. Task Management")
    print("3. Exit")

def user_management():
    print("\nUser Management")
    print("1. Create a new user")
    print("2. View all users")
    print("3. Delete a user")

def task_management():
    print("\nTask Management")
    print("1. Create a task")
    print("2. Assign a task to a user")
    print("3. Mark a task as completed")
    print("4. View tasks by user")
    print("5. Create a category")
    print("6. Delete a task")
    print("7. View all tasks")  # New option to view all tasks

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':  # User Management
            user_management()
            user_choice = input("Choose an action: ").strip()

            if user_choice == '1':  # Create User
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                add_user(name, email)

            elif user_choice == '2':  # View Users
                users = list_users()
                if users:
                    print("\nRegistered Users:")
                    for user in users:
                        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
                else:
                    print("No users found.")

            elif user_choice == '3':  # Delete User
                try:
                    user_id = int(input("Enter user ID to delete: ").strip())
                    delete_user(user_id)
                except ValueError:
                    print("Invalid input. Please enter a valid User ID.")

        elif choice == '2':  # Task Management
            task_management()
            task_choice = input("Choose an action: ").strip()

            if task_choice == '1':  # Create Task
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()

                try:
                    user_id = int(input("Assign to user (ID): ").strip())
                except ValueError:
                    print("Invalid input. Please enter a valid User ID.")
                    continue

                category_id_input = input("Enter category ID (or press Enter to skip): ").strip()
                category_id = int(category_id_input) if category_id_input.isdigit() else None

                add_task(title, description, user_id, category_id)

            elif task_choice == '2':  # Assign Task to User
                try:
                    task_id = int(input("Enter task ID to assign: ").strip())
                    user_id = int(input("Assign to user (ID): ").strip())
                    assign_task(task_id, user_id)
                except ValueError:
                    print("Invalid input. Please enter valid Task and User IDs.")

            elif task_choice == '3':  # Mark Task as Completed
                try:
                    task_id = int(input("Enter task ID to mark as completed: ").strip())
                    mark_task_completed(task_id)
                except ValueError:
                    print("Invalid input. Please enter a valid Task ID.")

            elif task_choice == '4':  # View Tasks by User
                try:
                    user_id = int(input("Enter user ID to view tasks: ").strip())
                    tasks = view_tasks_by_user(user_id)
                    if tasks:
                        print("\nTasks for User:")
                        for task in tasks:
                            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
                    else:
                        print("No tasks found for this user.")
                except ValueError:
                    print("Invalid input. Please enter a valid User ID.")

            elif task_choice == '5':  # Create Category
                name = input("Enter category name: ").strip()
                add_category(name)

            elif task_choice == '6':  # Delete Task
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    delete_task(task_id)
                    print(f"Task {task_id} deleted successfully!")
                except ValueError:
                    print("Invalid input. Please enter a valid Task ID.")

            elif task_choice == '7':  # View All Tasks
                tasks = view_all_tasks()
                if tasks:
                    print("\nAll Tasks:")
                    for task in tasks:
                        assigned_to = f"User {task['user_id']}" if task['user_id'] else "Not Assigned"
                        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Assigned to: {assigned_to}")
                else:
                    print("No tasks found.")

        elif choice == '3':  # Exit Program
            print("\nExiting Task Manager... Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
