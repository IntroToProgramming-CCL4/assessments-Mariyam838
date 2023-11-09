# The function takes two parameters: city and country (with a default value of 'Unknown').
def describe_city(city, country = 'Unknown'):
    # Print a sentence describing the city and its country.
     print(f"{city} is in {country}.")
     # The function for three different cities
describe_city('Reykjavik', 'Iceland')
describe_city('Paris','France')
describe_city('Tokyo')