#Define a glossary with programming terms and their meanings
glossary = {
    "variable": "A container that holds data in program.",
    "loop": "A control structure that allows a program to repeatedly execute a block of code.",
    "if statement": "A control structure that allows a program to make decisions based on conditions.",
    "list": "A collection of items that can be of different types and is ordered and changeable.",
    "function": "A block of code that performs a specific task and can be reused throughtout the program."
}
# Print each word and its meaning 
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")