# Commissioning 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(f"First Friend (M1) => {friends[0]}")
print(f"First Friend (M2) => {friends[len(friends) * -1]}")
print(f"Last Friend (M1) => {friends[-1]}")
print(f"Last Friend (M2) => {friends[len(friends) - 1]}", '\n')

# Commissioning 02
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2], '\n')

# Commissioning 03
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:],'\n')

# Commissioning 04
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2] = "Elzero"
friends[-1] = "Elzero"
print(friends, '\n')

# Commissioning 05
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends, '\n')

# Commissioning 06
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends = friends[2:]
print(friends)
friends.pop()
print(friends, '\n')

# Commissioning 07
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends, '\n')

# Commissioning 08
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends = sorted(friends, reverse=False)
print(friends)
friends = sorted(friends, reverse=True)
print(friends ,'\n')

# Commissioning 09
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends), '\n')

# Commissioning 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1], '\n')