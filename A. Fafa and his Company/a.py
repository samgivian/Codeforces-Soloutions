a=int(input())
b=0
for r in range(1,a):
    c=a-r
    if(c%r==0):
        b=b+1
print(b)
