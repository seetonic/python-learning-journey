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

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    for n, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] == True else " "
        print(f"{n}. {task["Title"]} [{mark}]")

def add_task(tasks):
    title = input("Task name: ").strip().capitalize()
    if title == "":
        print("Task cannot be empty.")
        return

    tasks.append({"Title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def complete_task(tasks):
    show_tasks(tasks)

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
    show_tasks(tasks)

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
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Please choose 1 to 5.")


main()