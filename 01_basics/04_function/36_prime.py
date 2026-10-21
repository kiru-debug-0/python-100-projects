def prime(num):
  c=0
  for i in range(2,num):
    if(num%i==0):
        c=c+1
  if(c==0):
    print(" it is a prime number ")
  else:
    print(" it is not a prime number ")
    6
n=int(input(" enter number "))
result=prime(n)
print(result)
