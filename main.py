import matplotlib.pyplot as plt
list = []
list1 = []
y = 0
x = 1
while x == 1:
    x = int(input("enter a number: "))
    list.append(x)
    list1.append(0)
    while x != 1.0:
        if x % 2 == 0:
            x = x/2
        else:
            x = x*3+1
        print(x)
        y = y + 1
        list1.append(y)
        list.append(x)
    plt.plot(list1, list)
    plt.show()
    list.clear()
    list1.clear()


