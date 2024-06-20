# Define a function to add tasks
def add_task(task_list, task):
  task_list.append(task)
  print(f"Task '{task}' added to the list!")

# Define a function to show tasks
def show_tasks(task_list):
  if not task_list:
    print("There are no tasks in the list.")
    return
  print("Your tasks:")
  for index, task in enumerate(task_list):
    print(f"{index+1}. {task}")

# Define a function to remove tasks
def remove_task(task_list, task_number):
  if task_number <= 0 or task_number > len(task_list):
    print("Invalid task number.")
    return
  task_to_remove = task_list.pop(task_number - 1)
  print(f"Task '{task_to_remove}' removed from the list.")

# Initialize an empty list for tasks
tasks = []

# Create a loop to interact with the user
while True:
  print("\nTodo List App")
  print("1. Add a task")
  print("2. Show tasks")
  print("3. Remove a task")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    task = input("Enter the task to add: ")
    add_task(tasks, task)
  elif choice == '2':
    show_tasks(tasks)
  elif choice == '3':
    if not tasks:
      print("There are no tasks to remove.")
      continue
    show_tasks(tasks)  # Show tasks before removing for reference
    task_number = int(input("Enter the number of the task to remove: "))
    remove_task(tasks, task_number)
  elif choice == '4':
    print("Exiting the app.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")
