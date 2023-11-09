#Ask user to input the color of the alien
alien_color = input("Enter the color of the alien ('green','yellow, or 'red'):")
#Check the color of the alien
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
elif alien_color == 'red':
    print("The player earned 15 points.")
else:
    print("Invaild color entered. Please enter 'green','yellow' or 'red'")