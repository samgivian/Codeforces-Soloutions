a=int(input())
bills=0
b=a%100
a=a-b
bills=bills+a/100
a=b
b=a%20
a=a-b
bills=bills+a/20


a=b
b=a%10
a=a-b
bills=bills+a/10

a=b

b=a%5
a=a-b


bills=bills+a/5

a=b

b=a%1
a=a-b


bills=bills+a
print(int(bills))
