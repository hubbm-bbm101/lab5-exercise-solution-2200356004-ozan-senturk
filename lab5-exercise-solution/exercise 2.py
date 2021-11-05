email= str(input("please enter your email"))
x=int(email.count("@"))
y=int(email.count("."))           
if x==1:
    if y > 0 :
        print("valid")
    else:
        print("invalid")
else:
    print ("invalid")