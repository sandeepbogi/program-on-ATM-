print("welcome")
card=input("insert card")
if(card=="yes"):
    print("select your language: English,Hindi,Telugu")
    num=int(input("enter a number"))
    if(num>0 and num<=99):
        print("access granted")
        password=int(input("enter your pin"))
        if(password==1234):
            a="banking"
            b="registration"
            c="mini statement"
            d="services"
            e="balance enquiry"
            f="transfer"
            print(a,b,c,d,e,f)
            options=input("select one from above")
            if(option==a):
                b1="fast cash"
                b2="withdrawl"
                b3="balance enquiry"
                b4="deposit"
                b5="pin change"
                print(b1,b2,b3,b4,b5)
                b0=input("select banking options")
                if(b0==b2):
                    wd=int(input("enter amount"))
                    if(wd>=100 and wd<=10000):
                        print("receive your cash")
                    else:
                        print("amount out of limits")
                else:
                     print("cannot withdraw cash from here")
            else:
                  print("cannot withdraw cash from here")
        else:
              print("incorrect password")
    else:
          print("privacy issue")
else:
    print("valid card needed")
