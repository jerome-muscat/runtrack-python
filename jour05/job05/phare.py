def hauteurParcourue(nb, h) :  
    print(f"Pour {nb} marches de {h}cm, il parcourt {nb*h*2*5*7/100.0:.2f}m par semaine !") 
   
nombre_marches = int(input("Combien de marches ?"))  
hauteur_marche = int(input("Hauteur d'une marche (cm) ?"))  
  
hauteurParcourue(nombre_marches, hauteur_marche)