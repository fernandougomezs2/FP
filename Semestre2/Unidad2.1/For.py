n=int(input("Indique el número menor: "))  
m=int(input("Indique el número mayor: "))  
p = 0
for i in range(n,m):
    if i%2==0:
        print(i)
        p = p + 1

print("Hay",p, "pares")