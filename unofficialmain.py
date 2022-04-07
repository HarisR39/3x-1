import time

b = []
y = 1
x = True
for g in range(50):
    y= y +1 
    for z in range(1, y):
        if y % z != 0:
            break
        else:
            b.append(y)
print(b)


    
    
    