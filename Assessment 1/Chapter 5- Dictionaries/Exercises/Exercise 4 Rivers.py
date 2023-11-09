#Define the dictionary with rivers and their corresponding countries
rivers= {
    'nile': 'egypt',
    'amazon' : 'brazil',
    'lena' : 'russia'
}
#Print sentences about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")
#Print the names of each river
print("\nRivers:")
for river in rivers:
    print(river.capitalize())
#Print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country.capitalize())
