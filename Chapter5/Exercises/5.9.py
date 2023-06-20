current_users = ["cuser1", "cuser2", "cuser3", "cuser4", "cuser5"]
new_users = ["user1", "user3", "user4", "cuser1", "cuser4"]

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Username already exists!!")
	else:
		print("Username is available for use")

