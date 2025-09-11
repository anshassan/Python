# Simple Calculator Program in Python

print("----- Simple Calculator -----")

# User se input lena
num1 = float(input("Pehla number daalo: "))
num2 = float(input("Dosra number daalo: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nApni choice daalo (1/2/3/4): ")

# Conditions lagana
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:  # zero division ka check
        print("Result:", num1 / num2)
    else:
        print("Error: Zero se divide nahi kar saktay!")
else:
    print("Invalid choice! Sahi option select karo.")
