def main():
    tasks = []

    while True:
        print("\n~~~~~ To-Do List ~~~~~")
        print("Enter key 1 to Add Task")
        print("Enter key 2 to Show Tasks")
        print("Enter key 3 to Mark Task as Done")
        print("Enter key 4 to Exit")

        choice = input("Enter your choice key: ")

        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task one by one: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task is marked as done!")
            else:
                print("Please enter a valid choice key")

        elif choice == '4':
            print("Exiting the To-Do List, thank you!")
            break

        else:
            print("Invalid choice.  Please enter a valid input.")

if __name__ == "__main__":
    main()