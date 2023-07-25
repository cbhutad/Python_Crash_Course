filename = "output_files/poll.txt"

with open(filename,"r+") as file_obj:
    while True:
        reason = input("Enter reason or quit to exit: \n")
        if reason != "quit":
            file_obj.write(f"{reason}\n")
        else:
            content = file_obj.read()
            print(content)
            break