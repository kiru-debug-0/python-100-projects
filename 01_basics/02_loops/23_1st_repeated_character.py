text=input(" enter a string ")
for i in range(len(text)):
  c=0
  for j in range(i+1,len(text)):
    if text[i]==text[j] :
      c=c+1
  if c>0:
     print(" repeated character = ",text[i])
