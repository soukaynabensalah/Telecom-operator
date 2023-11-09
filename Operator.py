
def price(d)
    tab=[]
    tab.append(200)
    if d>=120 :
        tab.append(100+(d-120)*0.5)
    elif d>=60 :
        tab.append(50+(d-60))
    elif d>=30 :
        tab.append(20+(d-30)*1.5)
    else :
        tab.append(d*2)
    return tab


T=[]
print("*****menu*****") 
print("1- Saisir la durée de communication")
print("2- Afficher la liste du côut mensuelle par offre") 
print("3- Afficher l’offre la plus intéressante (moindre coût)") 
print("4- Quitter le programme")
m=int(input("svp entrer votre choix: "))
while m < 1 and m>4 :
   while m != 1 :
       d=fleot(input("il faut saisir la durée de communication au début : "))
   if m = 1 :
       d=fleot(input ("entrer la durée de communication: "))
   T.append(price(d))
   elif m = 2 :
       print("abonnement mensuel :200 prix:",T[0])
       print("abonnement mensuel :100 prix:",T[1])
       print("abonnement mensuel :50 prix:",T[2])
       print("abonnement mensuel :20 prix:",T[3])
       print("abonnement mensuel :0 prix:",T[4])
   elif m = 3 :
       print("l'offre le plus intéressant est: ",min(T))
   elif m = 4 :
       print("au revoir")


