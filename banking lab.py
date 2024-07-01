def ini_():
    savings=0
    return("the account is created ")

def deposit():
    amount=float(input("enter the amount you are going to deposit"))
    savings=savings+amount
    return("your amount is deposited successfully/n","your balance is",savings)

def withdraw():
    deposit(savings)
    amt=float(input("enter the amount you are going to withdraw"))
    if( savings>=amt):
        savings=savings-amt
        return("your amount is withdrawed successfully","your balance is",savings)
    

def enquiry():
        return("your balance is",savings)


#print(ini_(savings))
#print(deposit(savings))
#print(savings)
#print(withdraw())
#print(enquiry())
choice=input(  )  
if choice=="1":
    print( ini_())
elif choice=="2":
    print(deposit())
elif choice=="3":
    print(withdraw())

else:
    print(enquiry())
    
