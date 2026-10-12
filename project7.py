#   TO---D0---LIST


tasks = []
while True:
    print("\n. add task")
    print("2. see task")
    print("3. exit")

    choice = input("write number: ")

    if choice == "1":
        task = input("write task: ")
        tasks.apend(task)
        print("task will be added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("task unavailable")
        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":
        print("Bye!")
        break
    else:
        print("wrong number")