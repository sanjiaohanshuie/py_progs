print("Hello, World!")
for i in range(5):
    print("Iteration", i + 1   )             
    while True:
        user_input = input("Type 'exit' to break the loop: ")
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break
        else:
            print("You typed:", user_input) 