#Ask the user to input their age
age = int(input("Enter your age:"))
#Determine the person's stage of life using if-elif-else chain
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The perosn is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")