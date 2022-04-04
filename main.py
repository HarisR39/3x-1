list = list()
x = 1
while x == 1:
    x = int(input("enter a number: "))
    while x != 1.0:
        if x % 2 == 0:
            x = x/2
        else:
            x = x*3+1
        print(x)
        list.append(x)

