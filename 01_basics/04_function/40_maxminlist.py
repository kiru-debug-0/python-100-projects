def find(l):
  max=l[0]
  min=l[0]
  for i in l :
    if(i<min):
      min=i
    if(i>max):
      max=i
  return min,max
  
n=[12,10,5,0]
result=find(n)
print(result)
