from colorist import red

line01 = "*************************"  # header / footer
line02 = "*                       *"  # re-use
line03 = "*    Welcome to To do   *"
line04 = "*                       *"


def add_task(tasks):
    add_task_name = input("Please insert task name ...\n")
    tasks.append(add_task_name)

# starts with blank
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('')  # ends with blank

red("!! TASKS DO NOT SAVE. KEEP APPLICATION OPEN !!")
print("")
tasks = []

while True:
    choice = input(
        "Please choose an action ...\nadd To add a task\nremove To remove a task\nview To view tasks\nexit To exit\n\n")

    if choice == 'add':
        print("")
        add_task(tasks)
        print("")
    elif choice == 'remove':
        print("")
        remove_task_name = input("Please enter task name ...\n")
        tasks.remove(remove_task_name)
        pass
    elif choice == 'view':
        print("")
        print(tasks)
        print("")
        pass
    elif choice == 'exit':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print("")

# Rest of your code
