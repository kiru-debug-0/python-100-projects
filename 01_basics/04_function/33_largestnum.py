def large(n1,n2,n3):
  l=n1
  if(n2>n1 and n2>n3):
    l=n2
  elif(n3>n1 and n3>n2):
    l=n3
  else:
    l=n1
  return l 
n=int(input(" enter number 1 "))
num=int(input(" enter number 2 "))
no=int(input("enter number 3 "))
result=large(n,num,no)
print(result)
