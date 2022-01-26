"""
lettre=str(input("choisir une lettre\n"))
phrase=str(input("ecrire une phrase\n"))
cpt=0
for i in range(len(phrase)):
    if phrase[i] == lettre:
        cpt+=1
print(cpt)
"""
"""
def table(nombre):
    cpt=0
    res=0
    while cpt!=10:
        cpt+=1
        res=nombre*cpt
        print(f"{nombre} X {cpt} = {res}")
    return res

print(table(4))
"""
"""
nombre=int(input("choisir un nombre\n"))
for i in range(1,nombre+1):
    if nombre%i==0:
        print(i)
"""
taille = float(input("Entrez votre taille en mètre\n"))
poids = float(input("Entrez votre poids en kilos : \n"))
imc = poids/(pow(taille,2)) 

print(f"Votre IMC est de {imc}")
