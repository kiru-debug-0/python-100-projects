def check(num):
  if(num%2==0):
    return "even"
  else:
    return "odd"
n=int(input("enter number "))
result=check(n)
print(result)
