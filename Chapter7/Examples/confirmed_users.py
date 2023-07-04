# Moving items from one list to another

unconfirmed_users = ["alice","bryan","candice"]
confirmed_users = []

while len(unconfirmed_users) > 0:
	confirmed_user = unconfirmed_users.pop()
	print(f"Confirming user : {confirmed_user.title()}")
	confirmed_users.append(confirmed_user)

print("List of confirmed_users are : ")
for user in confirmed_users:
	print(user)
