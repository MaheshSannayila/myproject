dict_a={"mahesh1@gmail.com":"12543","mahesh2@gmail.com":"12354","mahesh3@gmail.com":"12345"}
# print(dict_a)
mail=list(dict_a.keys())
print(mail)
password=list(dict_a.values())

user_mail=input()
user_password=input()
if user_mail.endswith("gmail.com"):
    if user_mail in mail and user_password in password:
        if mail.index(user_mail)==password.index(user_password):
            print("redirect to user page")
        else:
            print("Incorrect Password or Incorrect Mail")
    else:
        print("enter the login details")
        dict_a[user_mail]=user_password  
else:
    print("invalid mail")

# print(dict_a)
            




