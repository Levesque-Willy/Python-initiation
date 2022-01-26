import random

collone=0
ligne=0

bateauX=random.randint(1,5)
bateauY=random.randint(1,5)
while collone!=bateauX or ligne!=bateauY:
    collone=int(input("choisir une collone entre 1 et 5\n"))
    ligne=int(input("choisir une ligne entre 1 et 5\n"))
    if collone==bateauX and ligne==bateauY:
        print("touché coulée")
    elif collone==bateauX and ligne!=bateauY or ligne==bateauY and collone!=bateauX:
        print("En vue")
    else:
        print("A l'eau")
