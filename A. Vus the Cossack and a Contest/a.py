input_string = input()
userList =input_string.split()
results = list(map(int, userList))
if(results[1]>= results[0] and results[2]>=results[0]):
    print('YES')
else:
    print('NO')
