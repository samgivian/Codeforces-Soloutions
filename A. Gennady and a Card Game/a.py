a=str(input())
input_string = input()
userList =input_string.split()
results = list(map(str, userList))
##results = list(map(int, userList))
b=a[0:1]
c=a[1:2]
list_one=[]
for i in range(0,5):
    list_one.append(results[i][0])

list_two=[]
for i in range(0,5):
    list_two.append(results[i][1])
if b in list_one:
    print('YES')
elif c in list_two:
    print('YES')
else:
    print('NO')
