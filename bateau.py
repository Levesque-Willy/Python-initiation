collone=int(input("choisir une collone entre 1 et 5\n"))
ligne=int(input("choisir une ligne entre 1 et 5\n"))
bateauX=4
bateauY=4
    if collone==bateauX and ligne==bateauY:
        print("touché coulée")
    elif collone==bateauX and ligne!=bateauY or ligne==bateauY and collone!=bateauX:
        print("En vue")
    else:
        print("A l'eau")
