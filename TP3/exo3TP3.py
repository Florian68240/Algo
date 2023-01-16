import random
x=random.randrange (1,101,1)
y=0
r=0
print(x)
while y!=x:
    r=r+1
    y = int(input("Devinez le nombre mystère"))
    if y==x:
        print("C'est la bonne valeur")
    elif y>x:
        print("La valeur est plus petite")
    else:
        print("La valeur est plus grande")
print(r)
