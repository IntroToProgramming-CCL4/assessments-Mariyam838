def favorite_book(title):
    #Define a function named favorite_book that accepts a parameter 'title'.
    #This function will print a message about a favorite book.
    message= f"One of my favorite books is {title}."
    # Create a message using an f-string that includes the provided 'title'.
    return message
#Return the generated message.

#Call the function and print the message
book_message = favorite_book("Alice in the wonderland")
# Call the function 'favorite_book' with the title "Alice in the wonderland" and store the returned message in 'book_message'.
print(book_message)

    