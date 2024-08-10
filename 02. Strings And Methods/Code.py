My_Name = "George"
My_Age = "21"
My_Country = "Egypt"
print('"Hello '+"'"+My_Name+"', "+"How You Doing \\ "+ '""" Your Age Is "'+ My_Age+ '""'+ " + And Your Country Is: "+ My_Country, '\n')

print(f'''"Hello \'{My_Name}\', How You Doing \\
""" Your Age Is "{My_Age}"" +
And your Country Is: {My_Country}''', '\n')

name = "Elzero"
print(f'Second Latter Is "{name[1]}"')
print(f'Third Latter Is "{name[2]}"')
print(f'Last Latter Is "{name[-1]}"', '\n')

name = "Elzero"
print(f'"{name[1:4]}"')
print(f'"{name[::2]}"')
print(f'"{name[-2::-2]}"', '\n')

name = "#@#@Elzero#@#@"
print(name.strip("#@"), '\n')

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4), '\n')

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"), '\n')

name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase(), '\n')

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"), '\n')

name = "Elzero"
print(name.index('z'), '\n')

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1), '\n')

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"), '\n')

name = "George"
age = 21
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}", '\n')