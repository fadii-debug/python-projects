# Expence tracker

expenses = []

while True:
    print("\n. add expense")
    print("2. see all expenses")
    print("3. total expenses")
    print("4. Exit")

    choice = input("choice (1-4): ")

    if choice == "1":
        name = ("what was the expense for? ")
        amount = float(input("how much coast? "))
        expenses.append({"name" : name, "amount": amount})
        print("expense will be add!")

    elif choice == "2":
        if len(expenses) == 0:
            print("no expense yet")
        else:
            for item in expenses:
                print(item["name"], "-", item["amount"])

    elif choice == "3":
        total = 0
        for item in expenses:
            total = total + item["amount"]
            print("total expense:", total)

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("wrong choice, try again")        