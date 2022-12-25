n = int(input())
s=0 # 1 can divide any number 

for i in range(1,n):
  if(n % i ==0):    
   s+=i
if(s>n):
  print("True")
else:
  print("False")