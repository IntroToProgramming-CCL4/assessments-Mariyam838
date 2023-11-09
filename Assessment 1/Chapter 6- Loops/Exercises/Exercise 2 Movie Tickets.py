#Start with indefinite loop
while True :
    # Ask the user to input age
    age = input("Enter your age (or 'quit' to exist ):")
    #Check if user wants to quit
    if age == 'quit':
        break  #Exist the loop if user types 'quit'

    #Convert age to an integer for comparison
    age= int(age)
    #Determine ticket price based on age
    if age<3:
        ticket_price = 0 #Ticket is free for ages under 3
    elif 3 <= age <=12:
        ticket_price = 10 #Ticket is $10 for ages 3 to 12
    else :
        ticket_price = 15 #Ticket is $15 for ages over 12
    #Print the ticket price
    print(f"The cost of you movie tocket is ${ticket_price}\n")