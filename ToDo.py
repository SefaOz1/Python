print()

tasks = []

def addFunc():
    text = input("Enter task: ")
    
    tasks.append(text)
    
    print("\nOutput value:")
    print("Task added successfully.")

    print(f"\nCheck it: {tasks}")

def editFunc():
    while (True):
        try:
            index = int(input("Enter task index to edit: "))

            if not (0 <= index < len(tasks)):
                print("Please enter a number within the given range.")
                continue
            break
        except:
            print("Error! Please enter a number.")
            continue
    
    text = input("Enter new task: ")

    tasks[index] = text

    print("\nOutput value:")
    print("Task edited successfully.")

    print(f"\nCheck it: {tasks}")

def deleteFunc():
    while (True):
        try:
            index = int(input("Enter task index to delete: "))

            if not (0 <= index < len(tasks)):
                print("Please enter a number within given range.")
                continue
            break
        except:
            print("Error! Please enter a number.")
            continue

    tasks.pop(index)

    print("\nOutput value:")
    print("Task deleted successfully.")

    print(f"\nCheck it: {tasks}")

while (True):
    print("\nInput values:")
    print("1.   Add Task")
    print("2.   Edit Task")
    print("3.   Delete Task")
    print("4.   Exit")
    try:
        option = int(input(f"\nSelect an option: "))
        if not (1 <= option <= 4):
            print("Please enter a number within the given range.")
            continue
    except:
        print("Error! Please enter a number.")
        continue

    if option == 1:
        addFunc()
    elif option == 2:
        editFunc()
    elif option == 3:
        deleteFunc()
    elif option == 4:
        break
    else:
        continue

print()
"""
Ornek cikti:

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 9
Please enter a number within the given range.

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: dfg
Error! Please enter a number.

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 1
Enter task: Clean the car

Output value:
Task added successfully.

Check it: ['Clean the car']

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 1
Enter task: Buy apple

Output value:
Task added successfully.

Check it: ['Clean the car', 'Buy apple']

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 2
Enter task index to edit: 9
Please enter a number within the given range.
Enter task index to edit: dfg
Error! Please enter a number.
Enter task index to edit: 1
Enter new task: Buy red apple

Output value:
Task edited successfully.

Check it: ['Clean the car', 'Buy red apple']

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 3
Enter task index to delete: 1

Output value:
Task deleted successfully.

Check it: ['Clean the car']

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit

Select an option: 4

"""
