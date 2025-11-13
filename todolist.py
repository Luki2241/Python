tasks = []
choices = [1, 2, 3, 4]
print("Welcome to the todo-list app!")
#main loop
while True:
    print()
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")
    print()
    choice = int(input("Choose an option: "))
    
    if choice == choices[0]:
        task = input("Enter your task name: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == choices[1]:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
            remove = int(input("Which task do you wanna remove?: "))
            tasks.pop(remove - 1)
    
    elif choice == choices[2]:
        if len(tasks) > 0:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
        else:
            print("There are no tasks right now.")
    
    elif choice == choices[3]:
        print("Quitting...")
        quit()
        
    else: 
        print("Invalid option.")