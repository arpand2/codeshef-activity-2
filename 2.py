import re as r
url= input("enter a url")
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not r.search("[a-z]", password):
        flag = -1
        break
    elif not r.search("[A-Z]", password):
        flag = -1
        break
    elif not r.search("[0-9]", password):
        flag = -1
        break
    elif not r.search("[,@$]", password):
        flag = -1
        break
    elif r.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")