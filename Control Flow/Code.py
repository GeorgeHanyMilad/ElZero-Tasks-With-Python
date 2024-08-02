# Commissioning 01
num1 = input("Enter the first number: ").strip()
num2 = input("Enter the second number: ").strip()
operation = input("Enter the operator: ").strip()
if operation == "+" :
    print(f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}", '\n')
    
elif operation == "-" :
    print(f"{int(num1)} - {int(num2)} = {int(num1) - int(num2)}", '\n')
    
elif operation == "*" :
    print(f"{int(num1)} * {int(num2)} = {int(num1) * int(num2)}", '\n')
    
elif operation == "/" :
    print(f"{int(num1)} / {int(num2)} = {int(num1) // int(num2)}", '\n')
    
elif operation == "%" :
    print(f"{int(num1)} % {int(num2)} = {int(num1) % int(num2)}", '\n')
 
# Commissioning 02
age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You", '\n')

# Commissioning 03
my_age = int(input("Enter your age: "))
if 10 < my_age < 100 :
    print(f"Your Age In Months Is {my_age * 12} Months")
    print(f"Your Age In Weeks Is {my_age * 52} weeks")
    print(f"Your Age In Days Is {my_age * 365} days")
    print(f"Your Age In Hours Is {(my_age * 365) * 24} Hours")
    print(f"Your Age In Minutes Is {((my_age * 365) * 24) * 60} minutes")
    print(f"Your Age In Seconds Is {(((my_age * 365) * 24) * 60) * 60} seconds", '\n')
    
else :
    print("Your age is out of range", '\n')
    
# Commissioning 04
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}", '\n')
    
else :
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}", '\n')