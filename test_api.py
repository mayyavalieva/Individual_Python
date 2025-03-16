import requests

BASE_URL = "http://127.0.0.1:8000"

# Get all tasks
response = requests.get(f"{BASE_URL}/tasks")
tasks = response.json()

if not tasks:
    print("No tasks available. Creating a new task first...")
    response = requests.post(f"{BASE_URL}/tasks", json={"title": "New Task", "description": "Task for testing", "completed": False})
    task_id = response.json()["id"]
else:
    task_id = tasks[0]["id"]  # Use the first available task ID

# Fetch a specific task
print(f"Fetching task with ID {task_id}...")
response = requests.get(f"{BASE_URL}/tasks/{task_id}")
print(response.json())

# Update the task
print(f"Updating task {task_id}...")
response = requests.put(f"{BASE_URL}/tasks/{task_id}", json={"completed": True})
print(response.json())

# Delete the task
print(f"Deleting task {task_id}...")
response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
print(response.json())

# Verify deletion
print(f"Verifying deletion of task {task_id}...")
response = requests.get(f"{BASE_URL}/tasks/{task_id}")
print(response.json())  # Should return a 404 error