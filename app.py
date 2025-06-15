'''
quick terminal interaction where user can add, subtract, multiply, divide two numbers

will later be updating it to a web app 
'''
def is_real_number(x):
    return isinstance(x, (int, float))

def add_nums(num1, num2):
    return (num1 + num2)

def sub_nums(num1, num2):
    return num1 - num2

def mult_nums(num1, num2):
    return num1 * num2

def div_nums(num1, num2):
    try:
        result = num1 / num2
        return result  # Returns if no error
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None 

def menu():
    print("Welcome to the Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            print("You chose Option 1: Addition.")
            num1 = input("First Number: ")
            num2 = input("Second Number: ")
            try:
                num1, num2 = float(num1), float(num2)
                tot = add_nums(num1, num2) 
                print(f"{num1} + {num2} = {tot}")
            except ValueError:
                print("\nAt least one of the inputs was not a real number.") 

        elif choice == '2':
            print("You chose Option 2: Subtraction.")
            # Action for option 2
            num1 = input("First Number: ")
            num2 = input("Second Number: ")
            try:
                num1, num2 = float(num1), float(num2)
                tot = sub_nums(num1, num2) 
                print(f"{num1} - {num2} = {tot}")
            except ValueError:
                print("\nAt least one of the inputs was not a real number.") 
        
        elif choice == '3':
            print("You chose Option 3: Multiplication.")
            # Action for option 2
            num1 = input("First Number: ")
            num2 = input("Second Number: ")
            try:
                num1, num2 = float(num1), float(num2)
                tot = mult_nums(num1, num2) 
                print(f"{num1} x {num2} = {tot}")
            except ValueError:
                print("\nAt least one of the inputs was not a real number.") 
        
        elif choice == '4':
            print("You chose Option 4: Division.")
            num1 = input("First Number: ")
            num2 = input("Second Number: ")
            try:
                num1, num2 = float(num1), float(num2)
                tot = div_nums(num1, num2) 
                print(f"{num1} / {num2} = {tot}")
            except ValueError:
                print("\nAt least one of the inputs was not a real number.") 
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()