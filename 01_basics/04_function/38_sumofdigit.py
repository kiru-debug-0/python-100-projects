def sumdigit(num):
  sum=0
  while (num!=0):
       d = num % 10
       sum = sum+d
       num = num//10
  return sum 
n=int(input(" enter number "))
result=sumdigit(n)
print(result)
