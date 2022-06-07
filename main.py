import re as r
phone_number = input("phone number")
flag = 0
while True:  
    if (len(phone_number) >10):
        flag = -1
        break
    elif not r.search("[ local number >8]", phone_number):
        flag = -1
        break
    elif not r.search("[country code >=2]", phone_number):
        flag = -1
        break
    else:
        flag = 0
        print("Valid phone number")
        break
  
if flag ==-1:
    print("Not a Valid phone number")