class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Task index out of range.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Task index out of range.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index + 1}. {task['task']} - {status}")
        else:
            print("To-Do List is empty.")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()