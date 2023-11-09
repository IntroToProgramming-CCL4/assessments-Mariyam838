#Define the list of sandwich orders with 'pastrami' appearing multiple times
sandwich_orders = ["Grilled chicken", "pastrami","Grilled cheese","Tune","Ham and cheese","pastrami","pastrami"]
#Print a message indicating the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.\n")
#List of finished sandwiches
finished_sandwiches = []
#Loop through the sandwich orders and remove all occurance of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
#Continue with making other sandwiches
while sandwich_orders:
    currrent_sandwich = sandwich_orders.pop(0) # Take the first sandwich from the list
    #Print a message indicating the sandwich is being made 
    print(f" I'm making your {currrent_sandwich} sandwich.")
    #Add the finished sandwich to the list of finished sandwiches
    finished_sandwiches.append(currrent_sandwich)
#Print the list of finished sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)      
