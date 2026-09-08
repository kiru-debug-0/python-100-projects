text=input(" enter a text ")
c=0
for i in text.lower():
  if i in 'aeiou':
    c=c+1
print(" number of character = ",c)
