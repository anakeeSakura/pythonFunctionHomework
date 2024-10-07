'''
1. The Calculator App
Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
'''

def add(num1, num2):
    return num1 + num2      
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed"
    else:
        return num1 / num2



def calculator():
    while  True:
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Quit")
        calculate = input("Please select from menu which arithmetic operation to perform: ")
        
        if calculate ==  "1":
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         print(add(num1, num2))
        elif calculate == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(subtract(num1, num2))
        elif calculate == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(multiply(num1, num2))
        elif  calculate == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(divide(num1, num2))
        elif calculate == "5":
            break
        else:
            print("Invalid input. Please try again.")
    

calculator()


'''
2. The Shopping List Maker
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.
'''


items = ['Eggs', 'Milk', 'Water',  'Lychee',  'Bokchoy', 'Salmon', 'OJ', 'Sweet Rice', 'Ramen']

def edit_list():
    while True:
        print("\nShopping List Assistant")
        print("1. View Shopping list")
        print("2. Add item to Your Shopping list")
        print("3. Remove item to Your Shopping list")
        print("4. Exit")
        choice = input("Enter Your Selection: ")
        if choice == "1":
            shopping_list()    
        elif choice ==  '2':
            add_items()
        elif choice ==  '3':
            remove_items()
        elif choice == '4':
            print("Exiting The Shopping List Assistant")
            break
        else:
            print("Invalid choice. Please try again.")

def shopping_list():
    print("\nCurrent Shopping List:")
    for index, item in enumerate(items):
        print(f"Item {index + 1}: {item}")


def add_items():
    new_item  = input("Enter the name of the item: ")
    items.append(new_item)
    print(f"{new_item} has been added to your shopping list")

def remove_items():
    item_to_remove = input("Enter the name of the item to remove: ")
    if item_to_remove in items:
        items.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from your shopping list")
    else:
        print(f"{item_to_remove} was not found in the inventory.")

edit_list()