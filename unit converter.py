def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

while True:
    print("\n1. cm to inch\n2. inch to cm\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        try:
            cm = float(input("Enter value in cm: "))
            print(f"{cm} cm = {cm_to_inch(cm):.2f} inch")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "2":
        try:
            inch = float(input("Enter value in inch: "))
            print(f"{inch} inch = {inch_to_cm(inch):.2f} cm")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
