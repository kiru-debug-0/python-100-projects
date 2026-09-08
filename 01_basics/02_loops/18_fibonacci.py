n=int(input("enter number of terms "))
a=0
print(a)
b=1
print(b)
for i in range(1,n-1):
  c=a+b
  a=b
  b=c
  print(c)

