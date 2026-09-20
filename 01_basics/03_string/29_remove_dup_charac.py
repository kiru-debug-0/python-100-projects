s=input(" enter statement to remove duplicate  ")
result=""
for i in s :
  if i not in result:
    result=result+i
print(" final string = ",result)
