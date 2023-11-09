#Define a list of people to invite to dinner
guest_list = ["Muskan","Areeba","Masooma","Andy","Kisha"]
#Print initial invitations
for person in guest_list:
    print(f"Dear {person}, I would like to invite you to dinner. It would be an honor to have you as my guest.")
#Announce the guest who cant make it
unavailable_guest = "Masooma"
print(f"\nUnfortunately, {unavailable_guest} can't make it to the dinner") 
#Replace the unavailable guest with a new person
new_guest= "Sarah"
guest_list.remove(unavailable_guest)
guest_list.append(new_guest)
#Print the second set of invitations
for person in guest_list:
    print(f"Dear {person}, I would like to invite you to dinner. It would be an honor to have you as my guest.")