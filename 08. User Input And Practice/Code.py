# Commissioning 01
name = input().strip().capitalize()
print(f"Hello {name}, Happy To See You Here.", '\n')

# Commissioning 02
age = int(input())
print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" if age < 16 else f"Hello Your Age Is {age}, All Articles Is Suitable For You", '\n')

# Commissioning 03
first_name = input().strip().capitalize()
second_name = input().strip().capitalize()
print(f"Hello {first_name} {second_name[0]}.", '\n')

# Commissioning 04
email = input().strip().lower()
name = email.split("@")[0].capitalize()
print(f"Your Name Is: {name}")
email_service_provider = email.split("@")[1].split(".")[0]
print(f"Email Service Provider Is {email_service_provider}")
domain = email.split(".")[-1]
print(f"Top Level Domain Is {domain}", '\n')
