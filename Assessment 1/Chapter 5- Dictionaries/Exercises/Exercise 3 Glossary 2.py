#Define a glossary with programming terms and their meanings
glossary = {
    "variable": "A container that holds data in program.",
    "loop": "A control structure that allows a program to repeatedly execute a block of code.",
    "if statement": "A control structure that allows a program to make decisions based on conditions.",
    "list": "A collection of items that can be of different types and is ordered and changeable.",
    "function": "A block of code that performs a specific task and can be reused throughtout the program.",
    #Add more terms to the dictionary
    "float": "A number with a decimal point like 3.14.",
    "boolean": "A result that can only have one of two possible values: true or false",
    "string": "A bunch of characters put together.",
    "dictionary": "A way to store information with labels.",
    "integer" : " A whole number number, like 5 or -3."
}
# Print each word and its meaning using loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")