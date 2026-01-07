import json 



try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("tasks.json not found. Initializing empty task list.")
    tasks = []
    
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
   

    
print(tasks)
        
    

#task_str = json.dumps(tasks, indent=4)
#with open('tasks.json', 'w') as file:
  #  file.write(task_str)


