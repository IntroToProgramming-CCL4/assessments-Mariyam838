#Ask the user to input the color of the alien
alien_color =input("Enter the color of the alien ('green','yellow',or 'red'):")
#Check if the alien's color is green
if alien_color == 'green':
    #Print a statement that the player earned 5 points for shooting the alien
    print("The player just earned 5 points for shooting the alien.")
else:
    #Print the statement that the player just earned 10 points
    print("The player just earned 10 points.")