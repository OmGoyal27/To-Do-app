from pathlib import Path
import json

def extract_tasks():
    path = Path("todo.json")
    contents = path.read_text()
    return json.loads(contents)

def update(value):
    path = Path("todo.json")
    path.write_text(json.dumps(value))

def extract_commands():
    commands_path = Path("commands.txt")
    commands = commands_path.read_text(encoding='utf-8')
    return commands

def ask():
    mes = input("\nEnter your command: ")
    ans = mes.lower()
    tasks = extract_tasks()

    if ans == "view":
        print("\nThe tasks are:")
        for task in tasks:
            indax = tasks.index(task)
            inndex = indax + 1
            print(f"{inndex}:\t{task}")
    if ans == "remove":
        print("\nThe tasks are:")
        for task in tasks:
            indax = tasks.index(task)
            inndex = indax + 1
            print(f"{inndex}:\t{task}")

        removee = input("Enter the task number you want to remove: ")
        removee = int(removee)
        remove = removee - 1
        tasks.pop(remove)
        print("Done!")
        update(tasks)

    if ans == "add":
        add_task = input("Enter the task you want to add: ")
        tasks.append(add_task)
        update(tasks)
        print(f"The task '{add_task}' has been added to the list.")

    if ans == "help":
        print(extract_commands())

    if not ans == "exit":                               # Checking to exit
        loopin()
    else:
        print("Good bye...")

def loopin(): # The loop.
    try:
        ask()
    except KeyboardInterrupt:
        print("\nBye...")

print(extract_commands())

ask()