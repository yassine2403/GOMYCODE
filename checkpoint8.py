f =open("texte.txt",'r',encoding = 'utf-8')

def nth_line_reader(f,n):
    for i in range (n):
        print(f.readline())
        
n=input('enter number of lines you want to print counting from the top')
print('the first ' +n+' lines are')
nth_line_reader(f,int(n))

def lastnth_lines(f,n):
    str1=''
    lines=f.readlines()
    last_lines = lines[-n-1:]
    for i in last_lines:
        str1=str1+i
    return(str1)

t=input('enter number of lines you want to print counting from the bottom')
print('the last ' +t+' lines are')
print(lastnth_lines(f,int(t)))

def nb_words(f):
    b=[]
    a=0
    for i in f:
        b=b+i.split()
    for i in b:
        a=a+1
    return(a)

print(nb_words(f))
    
