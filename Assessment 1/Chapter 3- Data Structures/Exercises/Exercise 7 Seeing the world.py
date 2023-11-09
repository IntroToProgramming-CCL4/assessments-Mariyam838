#Define the list of places to vist
places_to_vist =["Tokyo","Paris","Rome","New York","Sydney"]
#Print the list in its original order
print("original order:",places_to_vist)
#Print the list in Alphabetical order without modifying the original list
print("alphabetical order:",sorted(places_to_vist))
#Show that the list is still in its original order
print("original order (Again):",places_to_vist)
#Print the list in reverse Alphabetical order without changing the original list
print("reverse alphabetical order:", sorted(places_to_vist, reverse=True))
#Print that the list is still in its original
print("original order(Again):", places_to_vist)
#Change the order of the list
places_to_vist.reverse()
print("reversed order:",places_to_vist)
#Change the order of the list back to its original order
places_to_vist.reverse()
print("original order(Again)",places_to_vist)
#Change the order of the list to alphabetical order
places_to_vist.sort()
print("alphabatical order:",places_to_vist)
#Change the order of the list to reverse alphabatical order
places_to_vist.sort(reverse=True)
print("reverse alphabatical order:",places_to_vist)