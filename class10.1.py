# contacts
contact=[ ]
while True:
    print("\n--contact manager--")
    print("1. add contact")
    print("2. search contact")
    print("3. remove contact")
    print("4. view all contacts")
    print("5. exit")

    choice = input("enter your choice(1-5):")

    # Add contact
    if choice == "1":
        name = input("enter contact name:")
        if name in contact:
            print("contact already exit:")
        else:
            contact.append(name)
            print("contact added successfully")


    # search contact
    elif choice =="2":
        name = input("enter contact name to search:")
        if name in contact:
            print("contact found.")  
        else: print("contact not found.")


    # remove contact
    elif choice == "3":
        name = input("enter contact name to remove:")
        if name in contact :
            contact.remove(name)
            print("contact removed successfully")
        else: 
            print("contact not found")


    # view all contact
    elif choice == "4":
        if len(contact) == 0:
            print("no contacts available.")
            for c in contact:
                print("-", c)   


    # exit program
    elif choice == "5":
        print("exiting contact manager. goodbye!")
        break

    else:
        print("invalid choice. please select 1-5")