import json

FILE_NAME = "tasks.json"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    print("-----------------------")
    done_count = sum(1 for task in tasks if task["done"] == True)
    print(f"Done: {done_count} of {len(tasks)}")
    print("-----------------------")

    for n, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] == True else " "
        print(f"{n}. {task['Title']} [{mark}]")

def Show_only_not_done_tasks(tasks):
    if len(tasks) == 0:
            print("No tasks yet.")
            return
    
    for n, task in enumerate(tasks, start=1):
        if task["done"] == False:
            print(f"{n}. {task["Title"]} [ ]")

def add_task(tasks):
    title = input("Task name: ").strip().capitalize()
    if title == "":
        print("Task cannot be empty.")
        return

    tasks.append({"Title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def edit_task(tasks):
    show_all_tasks(tasks)

    if len(tasks) == 0:
        print("No tasks yet.")
        return

    try:
        number = int(input("Which task number to edit? "))
        if number < 1 or number > len(tasks):
            print("That number is not in the list.")
            return

        choose = int(input("What would you want to edit? (1) Title (2) Complete box: "))
        if number < 1 or number > len(tasks):
            print("That number is not in the list.")
            return
        elif choose == 1:
            new_title = input("Enter the new task name: ").strip().capitalize()
            if new_title == "":
                print("Task cannot be empty.")
                return
        
            tasks[number - 1]["Title"] = new_title
            save_tasks(tasks)
            print("Task updated!")
        elif choose == 2:
            tasks[number - 1]["done"] = False
            save_tasks(tasks)
            print("Task updated!")
    except ValueError:
        print("Please type a number.")


def complete_task(tasks):
    show_all_tasks(tasks)

    try:
        number = int(input("Which task number is done? "))
        if number < 1 or number > len(tasks):
            print("That number is not in the list.")
            return
        
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Very nice!")
    except ValueError:
        print("Please type a number.")

def delete_task(tasks):
    show_all_tasks(tasks)

    try:
        number = int(input("Which task number to Delete? "))
        if number < 1 or number > len(tasks):
            print("That number is not in the list.")
            return
        removed = tasks.pop(number -1)
        save_tasks(tasks)
        print("Deleted:", removed["Title"])
    except ValueError:
        print("Please type a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Show All tasks")
        print("2. Show only not-done tasks")
        print("3. Add task")
        print("4. Complete task")
        print("5. Edit task")
        print("6. Delete task")
        print("7. Quit")

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            show_all_tasks(tasks)
        elif choice == "2":
            Show_only_not_done_tasks(tasks)
        elif choice == "3":
            add_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Please choose 1 to 6.")


main()