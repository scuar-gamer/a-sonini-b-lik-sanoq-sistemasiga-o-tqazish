a,b=map(int,input().split());s='';ans=0
while a >= b:
       s+=str(a%b)
       a//=b
s+=str(a%b)
print(s[::-1])

