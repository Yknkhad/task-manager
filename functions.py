from models import User, Task, Category
from database import session

# Create a new user
def add_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()

# List all users
def list_users():
    users = session.query(User).all()
    return [{"id": user.id, "name": user.name, "email": user.email} for user in users]

# Delete a user (and their tasks)
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()

# Create a new category
def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()

# Create a new task
def add_task(title, description, user_id, category_id=None):
    task = Task(title=title, description=description, user_id=user_id, category_id=category_id)
    session.add(task)
    session.commit()

# Assign task to a user
def assign_task(task_id, user_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.user_id = user_id
        session.commit()

# Mark task as complete
def mark_task_completed(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = 'Completed'
        session.commit()

# View tasks by user
def view_tasks_by_user(user_id):
    tasks = session.query(Task).filter(Task.user_id == user_id).all()
    return [{"id": task.id, "title": task.title, "status": task.status} for task in tasks]


# delete user 
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        # Delete all tasks associated with the user
        session.query(Task).filter_by(user_id=user_id).delete()
        session.delete(user)
        session.commit()
        print(f"User {user_id} and their tasks deleted successfully!")
    else:
        print("Error: User not found!")

def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task {task_id} deleted successfully!")
    else:
        print("Error: Task not found!")

# Function to view all tasks (assigned or unassigned)
def view_all_tasks():
    tasks = session.query(Task).all()
    if tasks:
        return [{"id": task.id, "title": task.title, "status": task.status, "user_id": task.user_id} for task in tasks]
    return []