server_username = "www"
server_paassword = "123"

user_entered_username = input("Enter user name:")
user_entered_password = input("Enter password:")
if(server_username == user_entered_username and server_paassword == user_entered_password):
    print("you are logged in")
else:
    print("your password is not incorrect")