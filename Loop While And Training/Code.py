# Commissioning 01
num = int(input("Enter Number: "))
if num <= 0 :
    print("Sorry, this number is lower than or equal zero")
    
else :
    Count = 0
    num -= 1
    while num > 0 :
        if num == 6 :
            num -= 1
        
        else :
            print(num)
            Count += 1
            num -= 1
            
    print(f"{Count} Numbers Printed Successfully.", '\n')


    
# Commissioning 02    
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
f = 0
AC = 0
WA = 0
while f <= (len(friends) - 1) :
    Str = friends[f].capitalize()
    if friends[f] == Str :
        AC += 1
        print(friends[f])
        
    else :
        WA += 1
        
    f += 1
        
print(f"{AC} Friends Printed And Ignored Names Count Is {WA}", '\n')



# Commissioning 03
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills :
    print(skills.pop(0))
    
print()



# Commissioning 04
my_friends = []
max_friends = 4
while max_friends > 0 :
    name = input("Enter the names of your friends: ").strip()
    if name.isupper() :
        print("Invalid Name")
        print(f"Names Left in List Is {max_friends}", '\n')
        
    else :
        if name.islower() :
            name = name.capitalize()
            my_friends.append(name)
            max_friends -= 1
            print(f"Friend {name} Added => 1st Letter Become Capital")
            print(f"Names Left in List Is {max_friends}", '\n')
            
        else :
            my_friends.append(name)
            max_friends -= 1
            print(f"Friend {name} Added")
            print(f"Names Left in List Is {max_friends}", '\n')