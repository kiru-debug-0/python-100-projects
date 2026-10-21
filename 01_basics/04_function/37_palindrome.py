def palindrome(s):
  s=s.lower()
  rev=s[::-1]
  if(s==rev):
        return (" string is palindrome ")
  else:
        return (" string is not palindrome ")
st=input(" enter word ")
result=palindrome(st)
print(result)
