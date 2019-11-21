a =input()
input_string = input()
userList =input_string.split()
results = list(map(int, userList))
if(sum(results)>0):
    print('HARD')
else:
    print('EASY')
