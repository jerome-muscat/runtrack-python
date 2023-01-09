def cesar(msg="", clef=0): 
    alphabet="abcdefghijklmnopqrstuvwxyz" 
    chiffre="" 

    for l in msg.lower(): 
        pos=alphabet.find(l) 
        chiffre+=alphabet[(pos+clef) % 26] if pos != -1 else l 

    return chiffre 
  
message= input("Taper ce que vous voulez chiffré : ") 
cle = int(input("vous voulez quelle clef de chiffrement ? "))
chiffre=cesar(message, cle) 
dechiffre=cesar(chiffre, -cle) 
print(message, "=>", "voici votre texte chiffré : " + chiffre, "=>", dechiffre)