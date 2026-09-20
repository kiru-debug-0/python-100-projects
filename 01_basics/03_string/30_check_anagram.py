s1=input(" enter string 1:")
s2=input(" enter string 2 :")
if(len(s1)!=len(s2)):
  print(" not an anagram ")
else :
  anagram=True 
  for i in s1:
    if s1.count(i)!=s2.count(i):
      anagram=False
if anagram:
  print(" string is a anagram")
else:
  print(" string is not a anagram")
    

  
