a=input("enter first number")
b=input("enter second number")
c=input("enter third number")
def abc_check (a,b,c):
    if a>b and a>c:
        print(a,"is the biggest")
    elif b>a and b>c:
        print(b,"is the biggest")
    else:
        print(c,"is the biggest")
abc_check(a,b,c)
    
