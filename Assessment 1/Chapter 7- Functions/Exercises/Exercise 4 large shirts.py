def make_shirt(size= 'L', message= 'I love Python'):
    # Print the size and message for the shirt.
    print(f"A {size}- sized shirt will be made with the message: '{message}'")
    #Make a large shirt with the default message
make_shirt()
# Make a medium-sized shirt with the default message
make_shirt(size='M')
# Make a small-sized shirt with a custom message
make_shirt(size='S', message='keep coding')