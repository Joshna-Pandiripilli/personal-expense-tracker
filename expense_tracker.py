list1= []
total = 0
while True:
    print("=" * 10, "PERSONAL EXPENSE TRACKER", "=" * 10)
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Check remaining budget")
    print("6. Exit")
    choice = int(input("Enter your choice:"))
    ("you entered:", choice)
    if choice == 1:
        print("Add expense selected")
        a = input("expense_name:")
        b = int(input("expense amount:"))
        c = input("expense category:")
        expense = { "name" :a,
                    "amount" : b,
                    "category" : c
                    }
        list1.append(expense)
    elif choice == 2:
            print("View expenses selected")
            print(list1)
    elif choice == 3:
            print("View total spending selected")
            total = 0
            for val in list1:
                       total += val["amount"]
            print("Total spending is", total)
    elif choice == 4:
            print("View spending by category selected")
            dict1 = {}
            for val in list1:
                   if val["category"] in dict1:
                          dict1[val["category"]] = dict1[val["category"]] + val["amount"]
                   else:
                          dict1[val["category"]] = val["amount"]
            print(dict1)
    elif choice == 5:
            print("Check remaining budget selected")
            budget = int(input("Enter the total budget: "))
            current_spent = 0
            for val in list1:
                current_spent += val["amount"]
            result = budget -  current_spent
            print("The remaining budget is :", result)    
    elif choice == 6:
            print("Exit")
            break
    else:
            print("Enter a valid number")



