text=input(" enter a string ")
new= " "
for i in range(len(text)):
  if text[i] not in new:
    new=new+text[i]
print(" new string =",new)
