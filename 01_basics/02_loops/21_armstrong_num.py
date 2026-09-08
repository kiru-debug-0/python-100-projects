n=int(input("enter number"))
b=n
sum=0
while n!=0:
  rem=n%10
  sum=sum+rem**3
  n=n//10
if(b==sum):
  print(" the number is armstrong ")
else:
  print(" the number is not armstrong ")
