guests = ["Marilyn Monroe", "Big L", "Leonardo Da vinci"]

message = f"You are welcome to join me for dinner {guests[0]}"
print(message)

message = f"You are welcome to join me for dinner {guests[1]}"
print(message)

message = f"You are welcome to join me for dinner {guests[2]}"
print(message)

print(f"Number of guests : {len(guests)}")

print("Alas Big L cannot make it to dinner")

del guests[1]
guests.append("Big Pun")

message = f"You are welcome to join me for dinner {guests[0]}"
print(message)

message = f"You are welcome to join me for dinner {guests[1]}"
print(message)

message = f"You are welcome to join me for dinner {guests[2]}"
print(message)

print(f"Number of guests : {len(guests)}")

print("Found a bigger table so inviting 3 more guests")

guests.insert(0,"guest1")
guests.insert(2,"guest2")
guests.append("guest3")

print(f"Number of guests : {len(guests)}")

message = f"You are welcome to join me for dinner {guests[0]}"
print(message)

message = f"You are welcome to join me for dinner {guests[1]}"
print(message)

message = f"You are welcome to join me for dinner {guests[2]}"
print(message)

message = f"You are welcome to join me for dinner {guests[3]}"
print(message)

message = f"You are welcome to join me for dinner {guests[4]}"
print(message)

message = f"You are welcome to join me for dinner {guests[5]}"
print(message)

print(f"Number of guests : {len(guests)}")

print("Sorry due to inconvienience can only host 2 people")

guests.pop();
guests.pop();
guests.pop();
guests.pop();

print(f"Number of guests : {len(guests)}")

print(f"you are still invited {guests[0]}")
print(f"you are still invited {guests[1]}")

del guests[1]
del guests[0]

print(guests)

print(f"Number of guests : {len(guests)}")