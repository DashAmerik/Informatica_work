
a = 0
b = 0
num = int(input())
while num != 0:
    if num > b:
        a = b
        b = num
    elif num > a:
        a = num
    num = int(input())

print(a)

#100
