#Initialize an empty list to store pizza toppings
pizza_toppings = []
#Loop to prompt user for toppings
while True:
    topping = input("Enter a pizza topping(or 'quit' to finish):")

    if topping == 'quit':
        break

    pizza_toppings.append(topping)
    print(f" You'll add {topping} to your pizza.")
    #Print the final list of pizza toppings
    print("\nYour pizza will have the following toppings:")
    for topping in pizza_toppings:
        print(topping)