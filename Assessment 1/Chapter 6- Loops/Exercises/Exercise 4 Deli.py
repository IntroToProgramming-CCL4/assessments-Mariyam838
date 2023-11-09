#Define the list of sandwich orders
sandwich_orders = ["Grilled chicken", "pastrami", "Grilled cheese", "Tuna", "Ham and cheese"]
#List of finished sandwiches
finished_sandwiches =[]
#Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) #Take the first sandeich from the list
    #Print a message indicating the sandwich is being made
    print(f"I'm making your {current_sandwich} sandwich.")
    #Add the finished sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

#Print the list of finished sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)