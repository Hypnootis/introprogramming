# Password security checker

password = str(input("Give your password:\n"))
is_secure = False

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "^",
                     "&", "*", "(", ")", "-", "+", "?",
                      "_", "=", ",", "<", ">", "/"]

# If password contains numbers
if len(password) >= 12:
    if any(x in password for x in numbers) and any(x in password for x in special_characters):
        for i in password:
            if i.isupper():
                is_secure = True

if is_secure:
    print("Your password is secure!")
else:
    print("Your password is not secure :(")
