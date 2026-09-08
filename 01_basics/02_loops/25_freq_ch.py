text=input(" enter text ")
for i in range (len(text)):
    c=0
    for j in range(1,i):
      if text[i]==text[j]:
        c=c=1
    if(c>0):
       print(text[i]," is repeated",c+1,"times")
      
