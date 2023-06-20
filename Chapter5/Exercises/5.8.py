usernames = ["user1", "user2", "admin", "user3", "user4"]
usernames = []

if len(usernames) == 0:
	print("We need some users")
else:
	for username in usernames:
		if username == "admin":
			print(f"Hello {username}, would you like to see the report")
		else:
			print(f"Hello {username}, Thanks for logging again today")