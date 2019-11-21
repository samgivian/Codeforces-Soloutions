input_string = input()
userList =input_string.split()
results = list(map(int, userList))
if ((results[0]+results[2])==(results[1]+results[3])):
    print('YES')
elif((results[0]+results[3])==(results[1]+results[2])):
    print('YES')

elif ((results[0]+results[1])==(results[2]+results[3])):
    print('YES')
elif((results[0]+results[1]+results[2])==(results[3])):
    print('YES')
elif((results[0]+results[1]+results[3])==(results[2])):
    print('YES')
elif((results[0]+results[3]+results[2])==(results[1])):
    print('YES')
elif((results[3]+results[1]+results[2])==(results[0])):
    print('YES')
else:
    print('NO')
    
