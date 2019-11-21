input_string = input()
userList =input_string.split()
results = list(map(int, userList))
a=True
n=1
while(a):
    if((results[0]*(3**n))>(results[1]*(2**n))):
        print(n)
        a=False
    n=n+1
    
