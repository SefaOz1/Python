print()

class ToDo:
    def __init__(self):
        self.tasks = []
    
    def menu(self):
        print("\nInput values:")
        print("1.   Add Task")
        print("2.   Edit Task")
        print("3.   Delete Task")
        print("4.   Exit")
        print("5.   Show Tasks")
    
    def add(self):
        task = input("Enter task: ")
        self.tasks.append(task)
    
    def edit(self):
        if self.tasks: # liste bos degilse:
            while (True):
                try:
                    index = int(input("Enter task index to edit: "))

                    if 0 <= index < len(self.tasks):
                        task = input("Enter new task: ")
                        self.tasks[index] = task
                        break
                    else:
                        print("Out of index range!")
                        continue

                except ValueError:
                    print("You didn't enter a number!")
        else:
            print("Tasks list is empty")

    def delete(self):
        if self.tasks:
            while (True):
                try:
                    index = int(input("Enter task index to delete: "))
                    
                    if 0 <= index < len(self.tasks):
                        self.tasks.pop(index)
                        break
                    else:
                        print("Out of index range!")
                        continue
                except ValueError:
                    print("You didn't enter a number!")
        else:
            print("Tasks list is empty")
    
    def show(self):
        if self.tasks:
            for x in self.tasks:
                print(x)
        else:
            print("Tasks list is empty")
    
    def run(self):
        while True:
            try:
                self.menu()
                option = int(input("Select an option: "))

                if 1 <= option <= 5:
                    if option == 1:
                        self.add()
                    elif option == 2:
                        self.edit()
                    elif option == 3:
                        self.delete()
                    elif option == 4:
                        break
                    elif option == 5:
                        self.show()
                else:
                    print("Out of option range!")
            except ValueError:
                print("You didn't enter a number!")

toDoThingsAtHome = ToDo()
toDoThingsAtOutside = ToDo()

choice = int(input("Which want do you want 'Home' (1) or 'Outside' (2): "))
if choice == 1:
    toDoThingsAtHome.run()
elif choice == 2:
    toDoThingsAtOutside.run()

print()

"""
Ornek cikti:

Which want do you want 'Home' (1) or 'Outside' (2): 1

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 3
Tasks list is empty

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 1
Enter task: Clean kitchen

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 1
Enter task: Prepare breakfast

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 2
Enter task index to edit: 1
Enter new task: Prepare dinner

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 5
Clean kitchen
Prepare dinner

Input values:
1.   Add Task
2.   Edit Task
3.   Delete Task
4.   Exit
5.   Show Tasks
Select an option: 4
"""
