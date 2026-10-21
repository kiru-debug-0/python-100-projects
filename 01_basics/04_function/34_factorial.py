def fac(num):
       f=1
       for i in range(1,num+1):
           f=f*i
       return f
n=int(input("enter number"))
factorial=fac(n)
print(factorial)
