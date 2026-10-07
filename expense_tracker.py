import json
list1 = []
class Expense:
        def __init__(self, name, amount, category):
              self.name = name
              self.amount = amount
              self.category = category
try:
    with open("./day2/data/file.json", encoding= "utf-8") as h:
        list1 = json.load(h)
except FileNotFoundError:
       list1 = []
total = 0
found = True
while True:
    print("=" * 10, "PERSONAL EXPENSE TRACKER", "=" * 10)
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Check remaining budget")
    print("6. Delete expense is selected")
    print("7. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Add expense selected")
        a = input("expense_name:")
        b = int(input("expense amount:"))
        c = input("expense category:")
        expense = Expense(a, b, c)
        list1.append(expense.__dict__)
    elif choice == 2:
            print("View expenses selected")
            for index, item in enumerate(list1):
                   print(f"{index + 1}. {item["name"]} - {item["amount"]} - {item["category"]}")
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
            print("Delete expense is selected")
            del_ex_index = int(input("enter the number of the expense to be deleted:")) - 1
            if 0 <= del_ex_index < len(list1):
                list1.pop(del_ex_index)
            else:
                   print("enter a valid index")
    elif choice == 7:
           print("Exit")
           break
    else:
           print("Enter a valid number")

with open("./day2/data/file.json","w", encoding= "utf8") as f:
       json.dump(list1, f, ensure_ascii = False, indent = 4 )
