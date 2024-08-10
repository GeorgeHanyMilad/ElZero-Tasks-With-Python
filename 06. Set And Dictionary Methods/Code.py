# Commissioning 01
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.pop()
print(unique_list, '\n')

# Commissioning 02
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
Merged_Set = nums.copy()
Merged_Set.update(letters)
print(Merged_Set, '\n')

# Commissioning 03
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set, '\n')
my_set.discard("C")

# Commissioning 04
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two), '\n')

# Commissioning 05
myDict = {
    "Html" : "90%",
    "Css" : "80%",
    "Python" : "30%"
}
print(f'"Html Progress Is {myDict["Html"]}"')
print(f'"Css Progress Is {myDict["Css"]}"')
print(f'"Python Progress Is {myDict["Python"]}"')
myDict["AI"] = "20%"
print(f'"AI Progress Is {myDict["AI"]}"', '\n')