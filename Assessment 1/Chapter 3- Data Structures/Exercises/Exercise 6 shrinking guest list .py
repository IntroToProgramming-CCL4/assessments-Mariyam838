# Define a list of people to invite to dinner
guest_list = ["Muskan", "Areeba", "Masooma", "Andy", "Kisha"]

# Announce limited space
print("Unfortunately, I can only invite two people for dinner.\n")

# Inform the guest who can't make it
unavailable_guest = "Masooma"
print(f"Unfortunately, {unavailable_guest} can't make it to the dinner.\n")

# Replace the unavailable guest with a new person
new_guest = "Sarah"
guest_list.remove(unavailable_guest)
guest_list.append(new_guest)

# Invite the two remaining guests
for person in guest_list[:2]:
    print(f"Dear {person}, you're still invited to dinner. I'm looking forward to seeing you!")

# Inform the others they can't be invited
for person in guest_list[2:]:
    print(f"Sorry {person}, I can't invite you to dinner this time.\n")

# Clear the list
del guest_list[:]

# Print the list to confirm it's empty
print("Guest list:", guest_list)
