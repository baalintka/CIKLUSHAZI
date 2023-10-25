
def feladat1(szam):
    i:int = 1
    while i < szam-2:
        if i %3==0 :

            print(i,end=";")

        i+=1
    if szam%3==0:
        print(i+2)
    elif i%3==0:
        print(i)
    else:
        print(szam-1)

def feladat2(szam):
    i:int =1
    while i < szam:
        print(szam,end=",")

        szam-=1
    print(szam,end="")

def feladat3():
    szam=int(input("Kérem adjon meg egy 5el oszható számot: "))
    while szam%5==1:
        int(input("Kérem adjon meg egy 5el oszható számot: "))



feladat1(18)
feladat2(10)
feladat3()
