guests = ["Marilyn Monroe", "Big L", "Leonardo Da vinci"]

message = f"You are welcome to join me for dinner {guests[0]}"
print(message)

message = f"You are welcome to join me for dinner {guests[1]}"
print(message)

message = f"You are welcome to join me for dinner {guests[2]}"
print(message)

print("Alas Big L cannot make it to dinner")

del guests[1]
guests.append("Big Pun")

message = f"You are welcome to join me for dinner {guests[0]}"
print(message)

message = f"You are welcome to join me for dinner {guests[1]}"
print(message)

message = f"You are welcome to join me for dinner {guests[2]}"
print(message)