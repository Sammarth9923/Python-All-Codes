email = input("Enter the email: ")

position = email.index("@")
username= email[ :position]
print(username)