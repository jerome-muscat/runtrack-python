def tapisserie(n):    
    for i in range(n):
        tapis=""
        for j in range(n-i): 
            tapis+="#" 
        tapis+=" " 
        for j in range(i): tapis+="#" 
        print("|" + tapis + "|")

diagonale = int(input("A quelle ligne souhaitez vous créer votre diagonale ? "))
tapisserie(diagonale)