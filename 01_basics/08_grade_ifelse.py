# to input marks and display total , percentage and grade 
print(" enter your marks to find your grade")
m=int(input("enter marks of math "))
e=int(input("enter marks of english"))
h=int(input("enter marks of hindi"))
s=int(input("enter marks of science"))
ss=int(input("enter marks of sst"))
total=m+e+h+s+ss
per=(total/500)*100
if(per>=90):
   grade="A+"
elif(per>=80 and per<90):
   grade="A"
elif(per>=70 and per<80):
   grade="B"
elif (per>=60and per<70):
   grade='C'
elif( per<=50and per<60):
   grade="D"
else:
   grade="F"
print(" total = ",total)
print(" percentage = ",per)
print(" grade =",grade)
