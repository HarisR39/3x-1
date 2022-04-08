b = []
x = int(input("enter a number: "))
for z in range(2, x):
    for v in range(2, z):
        if z % v == 0:
            break 
        b.append(z)
for g in range(1, len(b)):
    for h in range(g, len(b)):
        if b[g] == b[h]:
            del b[h]
print(b)
    

    


    
    
    