filename = "output_files/guest.txt"

with open(filename,"w") as file_obj:
    while True:
        name = input("Your name please or enter exit to quit: \n")
        if name != "quit":
            file_obj.write(f"{name}\n")
        else:
            break
        
