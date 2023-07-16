from user_admin import Admin

admin1 = Admin("first1", "last1", 26, "male")
admin1.describe_user()
admin1.greet_user()
admin1.increment_login_attempts()
print(f"Login attempts : {admin1.login_attempts}")
admin1.reset_login_attempts()
print(f"Login attempts : {admin1.login_attempts}")
admin1.privileges.show_privileges()