def resultnotes(note):
    arrondi=[]
    for i in note:
        if 40.00 <= i <= 100.00:
            if i % 5 > 2:
                i=i+(5-i%5)
                arrondi+=[i]
            else:
                arrondi+=[i]
            print(i,"Bravo!!!!!!!!!!!!!") 
        else:
            arrondi+=[i]
            print(i,"bof")
    print(arrondi)
    
notes_entre= input("Veuillez entrer les notes séparé par un virgule et s'il y a une partie décimal, séparé la partie entière et décimal avec un point ")
notes_list= list(notes_entre.split(","))
notes = [float(i) for i in notes_list]
resultnotes(notes)