input_string = input()
userList =input_string.split()
results = list(map(int, userList))
results.sort()
a=results[3]-results[0]
b=results[2]-a
c=results[1]-a
print(str(a)+" "+ str(b)+" "+str(c))
