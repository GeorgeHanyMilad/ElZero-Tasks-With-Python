# Commissioning 01
print("Commissioning 01")
def calculate(num1, num2, operation="add") :
    operation = operation.lower()
    if operation in ["a", "add"] :
        return num1 + num2
    elif operation in ["s", "subtract"] :
        return num1 - num2
    elif operation in ["m", "multiply"] :
        return num1 * num2
    else :
        return "This operation isn't defined!"

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30
print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10
print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200
print("\n")



# Commissioning 02
print("Commissioning 02")
def addition(*nums):
    sum = 0
    for num in nums :
        if num == 5 :
            sum -= num
        elif num != 10 :
            sum += num

    return sum

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
print("\n")



# Commissioning 03
print("Commissioning 03")
def show_skills(name, *skills):
    if len(skills) > 0 :
        print(f"Hello {name} your skills are: ")
        for skill in skills :
            print(f"- {skill}")
    else :
        print (f"Hello {name} You Have No Skills To Show")

# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")
print()

# Input
show_skills("Ahmed")
print("\n")



# Commissioning 04
print("Commissioning 04")
def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name} your age is {age} and you live in {country}")

# Input
say_hello("Osama", 38, "Egypt")
print()

# Input
say_hello()



