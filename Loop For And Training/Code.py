# Commissioning 01
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums = sorted(my_nums, reverse=True)
Count = 0
for n in my_nums :
    if n % 5 == 0 :
        Count += 1
        print(f"{Count} => {n}")
        
print("All Numbers Printed", '\n')



# Commissioning 02
for i in range(1, 21) :
    if (i == 6) or (i == 8) or (i == 12) :
        continue
    
    elif (i < 10) :
        print(f"0{i}")
        
    else :
        print(i)
        
print("All Numbers Printed", '\n')



# Commissioning 03
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
Count = 0
for k, v in my_ranks.items() :
    if v == "A" :
        Count += 100
        print(f"My Rank in {k} Is {v} And This Equal 100 Points")
        
    elif v == "B" :
        Count += 80
        print(f"My Rank in {k} Is {v} And This Equal 80 Points")
        
    else :
        Count += 40
        print(f"My Rank in {k} Is {v} And This Equal 40 Points")
        
print(f"Total Points Is {Count}", '\n')



# Commissioning 04
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
for key, value in students.items() :
    print("---------------------------")
    print(f"-- Student Name => {key}")
    print("---------------------------")
    C = 0
    for v1, v2 in value.items():
        if v2 == "A" :
            C += 100
            print(f"-- {v1} => 100 Points")
            
        elif v2 == "B" :
            C += 80
            print(f"-- {v1} => 80 Points")
            
        elif v2 == "C" :
            C += 40
            print(f"-- {v1} => 40 Points")
            
        elif v2 == "D" :
            C += 20
            print(f"-- {v1} => 20 Points")
            
    print(f"Total Point For {key} Is {C}")