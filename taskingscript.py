import json 



try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("tasks.json not found. Initializing empty task list.")
    tasks = []
options = ["add", "update", "remove", "view"]
input_action = input("Enter action (add/update/remove/view): ").strip().lower()
if input_action not in options:
    print("Invalid action. Please choose from add, update, remove, or view.")
    exit()
elif input_action == "view":
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
    exit()
elif input_action == "add":

    input_description = input("Enter task description: ")
    input_status = input("Enter task status (not started/in progress/completed): ")
    input_createdAt = input("Enter task creation date (YYYY-MM-DDTHH:MM:SSZ): ")
    input_updatedAt = input("Enter task update date (): ")
    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "description": input_description,
        "status": input_status,
        "createdAt": input_createdAt,
        "updatedAt": input_updatedAt
    }
    tasks.append(new_task)
    tasks_json = json.dumps(tasks, indent=4)
    with open('tasks.json', 'w') as file:
        file.write(tasks_json)    
   

    
for task in tasks:
    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        
input_id = int(input("Enter the ID of the task to update: "))
for task in tasks:
    if task['id'] == input_id:
        new_status = input("Enter new status (not started/in progress/completed): ")
        task['status'] = new_status
        new_updatedAt = input("Enter new update date (YYYY-MM-DDTHH:MM:SSZ): ")
        task['updatedAt'] = new_updatedAt
with open('tasks.json', 'w') as file:
    file.write(tasks_json)
    
input_id = int(input("Enter the ID of the task to remove: "))
remove_id = input_id
for task in tasks:
    if task["id"] == remove_id:
        tasks.remove(task)
        break
with open('tasks.json', 'w') as file:
    file.write(tasks_json)

#with open('tasks.json', 'w') as file:
  #  file.write(task_str)


