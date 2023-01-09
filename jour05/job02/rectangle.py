def rectangle(a,b):
    c='|'+'-'*(a)+'|\n'
    print(c+c.replace(*'- ')*(b-2)+c)
 
hauteur = int(input("Quelle hauteur souhaitez vous ? "))
largeur = int(input("Quelle largeur souhaitez vous ? "))
rectangle(hauteur, largeur)