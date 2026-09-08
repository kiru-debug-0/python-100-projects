n=int(input("enter number  "))
c=0
for i in range(2,n-1):
  if(n%i==0):
    c=c+1
if(c==0):
  print(" number is prime ")
else:
  print(" number is not prime ")
