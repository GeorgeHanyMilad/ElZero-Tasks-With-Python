# Commissioning 01
My_Name = "George", 
print(My_Name[0])
print(type(My_Name), '\n')

# Commissioning 02
friends = ("Osama", "Ahmed", "Sayed")
friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))
print(f"{len(friends)} Elements", '\n')

# Commissioning 03
nums = (1, 2, 3)
letters = ("A", "B", "C")
New_Tuple = nums + letters
print(f"nums_and_letters_one = {New_Tuple}")
print(f"{len(New_Tuple)} Elements", '\n')

# Commissioning 04
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c, '\n')