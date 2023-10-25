i = 0
szam=10

while i != szam:
    i += 1
    if i % 3 == 0:
        if i == szam or i ==szam-1  or i==szam-2:
            print(i,end="")
        else:
            print(i,end=",")

