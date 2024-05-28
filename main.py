from pathlib import Path
import json

def extract_tasks():                    # Extracts all the tasks
    path = Path("todo.json")
    contents = path.read_text()
    return json.loads(contents)

def update(value):                      # Updates all the tasks
    path = Path("todo.json")
    path.write_text(json.dumps(value))

def extract_commands():                 # Extracts all the available commands
    commands_path = Path("commands.txt")
    commands = commands_path.read_text(encoding='utf-8')
    return commands

def ask():                              # Main thing
    mes = input("\nEnter your command: ")
    ans = mes.lower()
    tasks = extract_tasks()

    if ans == "view":                   # Shows all the pending tasks
        print("\nThe tasks are:")
        for task in tasks:
            indax = tasks.index(task)
            inndex = indax + 1
            print(f"{inndex}:\t{task}")
    if ans == "remove":                 # Asks to remove a task
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

    if ans == "add":                    # Asks to add a task
        add_task = input("Enter the task you want to add: ")
        tasks.append(add_task)
        update(tasks)
        print(f"The task '{add_task}' has been added to the list.")

    if ans == "help":                   # Prints all the commands
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