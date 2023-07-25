filename = "output_files/guest_book.txt"

with open(filename,"a") as file_obj:
    while True:
        name = input("Enter your name or quit to exit: \n")
        if name != "quit":
            greeting = f"{name}, Welcome to party\n"
            file_obj.write(greeting)
        else:
            break
