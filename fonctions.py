from random import randint

### (cellule,O2,CO2,vie,dernieredivision)

#==============================================================================
# cette partie contient les fonctions pour creer la matrice et l'afficher
#==============================================================================

##### creer la matrice

def creeruneligne (nombredecolones,quantiteO2i,quantiteCO2i):
    ligne = []    
    for i in range (0,nombredecolones):
        ligne += [[0,quantiteO2i,quantiteCO2i,0,0]]
    return ligne
    
def creermatrice(nombredecolones,nombredelignes,quantiteO2i,quantiteCO2i):
    matrice = []    
    for i in range (0,nombredelignes):
        matrice += [creeruneligne(nombredecolones,quantiteO2i,quantiteCO2i)]
    return matrice

def creermatriceS (nombredecolones,nombredelignes,quantiteO2i,quantiteCO2i):  # cette fonction cree une matrice contenant une cellule en son centre
    matrice = creermatrice(nombredecolones,nombredelignes,quantiteO2i,quantiteCO2i)
    matrice [nombredelignes//2][nombredecolones//2][0] = 1
    return matrice

##### afficher la matrice

def affichermatrice(matrice):
    for i in range (0, len(matrice)):
        print (matrice [i])      

def copiermatrice(matrice):   #cette fonction permet de copier une matrice de rang 3
    A = creermatrice(len(matrice[0]),len(matrice),0,0)
    for i in range (0,len(matrice)):
        for j in range (0,len(matrice[0])):
            for k in range (0,len(matrice[0][0])):
                A [i][j][k] = matrice [i][j][k]
    return A

def affichermatricecellules (matrice):  # cette fonction affiche une matrice n indiquant que la presence ou non d une cellule dans une case
    a = copiermatrice(matrice)    
    for i in range (0,len(a)):
        for j in range (0,len (a[0])):
            a [i][j] = a [i][j][0]
            if a [i][j] == 0:
                a [i][j] = 0
            else:
                a [i][j] = 1
    affichermatrice(a)

def affichermatriceO2 (matrice):
    a = copiermatrice(matrice)    
    for i in range (0,len(a)):
        for j in range (0,len (a [0])):
            a [i][j] = a [i][j][1]
    affichermatrice(a)

def enregistrer_matrice (matrice,i):
    fichiersave = open ("matrices","a")
    fichiersave.write ("\n")
    fichiersave.write ("\n")
    fichiersave.write ("boucle   : ")
    fichiersave.write (str(i))
    fichiersave.write ("---------------------------------------------")
    fichiersave.write ("\n")
    fichiersave.write ("\n")
    # extrait de "affichermatricecellule
    a = copiermatrice(matrice)    
    for i in range (0,len(a)):
        for j in range (0,len (a[0])):
            a [i][j] = a [i][j][0]
            if a [i][j] == 0:
                a [i][j] = 0
            else:
                a [i][j] = 1
    # fin extrait
    for i in range (0,len(matrice)):
        fichiersave.write (str(a[i]))
        fichiersave.write ("\n")
    fichiersave.close ()
    

#==============================================================================
# Cette partie contient les fonctions d'evolution du systeme
#==============================================================================

##### evolution liees a l oxygene

def modificationO2(matrice,variationO2sicellule):
     for i in range (0,len(matrice)):
        for j in range (0,len (matrice [0])):
            if matrice [i][j][0] == 1:
                matrice [i][j][1] += variationO2sicellule
     return matrice

def egaliserO2(matrice,nombreegalisationO2):
    for k in range (0,nombreegalisationO2):
        i = randint(1,len(matrice)-2)
        j = randint (1,len(matrice[0])-2)
        somme = matrice[i-1][j-1][1] + matrice[i-1][j][1] + matrice[i-1][j+1][1] + matrice[i][j-1][1] + matrice[i][j][1] + matrice[i][j+1][1] + matrice[i+1][j-1][1] + matrice[i+1][j][1] + matrice[i+1][j+1][1]
        matrice[i][j][1] = somme / 9
    return matrice

def alimentationO2(matrice,alimentation_O2):
    matrice [len(matrice)//2] [len(matrice[0])//2] [1] += alimentation_O2
    return matrice

##### evolution liees au dioxyde de carbon

def modificationCO2(matrice,variationCo2sicellule):
     for i in range (0,len(matrice)):
        for j in range (0,len (matrice [0])):
            if matrice [i][j][0] == 1:
                matrice [i][j][2] += variationCo2sicellule
     return matrice

def egaliserCO2(matrice,nombreegalisationCO2):
    for k in range (0,nombreegalisationCO2):
        i = randint(1,len(matrice)-2)
        j = randint (1,len(matrice[0])-2)
        somme = matrice[i-1][j-1][2] + matrice[i-1][j][2] + matrice[i-1][j+1][2] + matrice[i][j-1][2] + matrice[i][j][2] + matrice[i][j+1][2] + matrice[i+1][j-1][2] + matrice[i+1][j][2] + matrice[i+1][j+1][2]
        matrice[i][j][2] = somme / 9
    return matrice

def alimentationCO2(matrice,alimentation_CO2):
    matrice [len(matrice)//2] [len(matrice[0])//2] [2] += alimentation_CO2
    return matrice

##### autres fonctions

def proliferationdesalgues(matrice,limiteco2,dureeminimaleentredeuxdivisions,ageminimaldedivision):
     for i in range (1,len(matrice)-1):
        for j in range (1,len (matrice [1])-1):
            if (matrice [i][j][2] >= limiteco2) and (matrice [i][j][0] == 1) and (matrice [i][j][4] >= dureeminimaleentredeuxdivisions) and matrice [i][j][3] >= ageminimaldedivision:
                compteur = 0  # ce compteur evite un blocage si une cellule n'a pas la place de se diviser, il est possible de le reduire si le programme est trop lent
                matrice[i][j][4] += -1*dureeminimaleentredeuxdivisions            
                while  compteur < 30:
                    alea = randint(1,8)
                    if alea == 1 and matrice [i-1][j-1][0] == 0:
                        matrice [i-1][j-1][0] = 1
                        compteur = 1000000
                    elif alea == 2 and matrice [i-1][j][0] == 0:
                        matrice [i-1][j][0] = 1
                        compteur = 1000000
                    elif alea == 3 and matrice [i-1][j+1][0] == 0:
                        matrice [i-1][j+1][0] = 1
                        compteur = 1000000
                    elif alea == 4 and matrice [i][j-1][0] == 0:
                        matrice [i][j-1][0] = 1
                        compteur = 1000000
                    elif alea == 5 and matrice [i][j+1][0] == 0:
                        matrice [i][j+1][0] = 1
                        compteur = 1000000
                    elif alea == 6 and matrice [i+1][j-1][0] == 0:
                        matrice [i+1][j-1][0] = 1
                        compteur = 1000000
                    elif alea == 7 and matrice [i+1][j][0] == 0:
                        matrice [i+1][j][0] = 1
                        compteur = 1000000
                    elif alea == 8 and matrice [i+1][j+1][0] == 0:
                        matrice [i+1][j+1][0] = 1
                        compteur = 1000000
                    else:
                        compteur +=1
                matrice [i][j][1] += -1*limiteco2
     return matrice

def modificationvie(matrice,dureeboucle):
     for i in range (0,len(matrice)):
        for j in range (0,len (matrice [1])):
            if matrice [i][j][0] == 1:
                matrice [i][j][3] += dureeboucle
                matrice [i][j][4] += dureeboucle
     return matrice

def mortdescellules (matrice,age_maximal_cellule):
    for i in range (0,len(matrice)):
        for j in range (0,len(matrice[0])):
            if matrice[i][j][3]>= age_maximal_cellule:
                matrice[i][j][3] = 0
                matrice[i][j][4] = 0
                matrice[i][j][0] = 0
    return matrice
    

#==============================================================================
# Cette partie contient les fonctions pour l'analyse de la matrice
#==============================================================================

def nombredecellules(matrice):
    compteur = 0
    for i in range (0,len(matrice)):
        for j in range (0,len (matrice [1])):
            if matrice [i][j][0] == 1:
                compteur += 1
    return compteur

def nombre02 (matrice):
    compteur = 0
    for i in range (0,len(matrice)):
        for j in range (0,len (matrice [1])):
            compteur += matrice [i][j][1]
    return compteur

def testcellulebord(matrice):   # cette fonction analyse toute les cases sur le brd de la matrice et retourne True si une cellule s'y trouve
    a = 0
    for i in range (0,len(matrice[0])):
        if matrice[0][i][0] == 1:
            return True
    for i in range (0,len(matrice[0])):
        if matrice[-1][i][0] == 1:
            return True
    for j in range (0,len(matrice)):
        if matrice[j][0][0] == 1:
            return True
    for j in range (0,len(matrice)):
        if matrice[j][-1][0] == 1:
            return True
    return False

def indicecellulebord(matrice,indice_cellule_bord,i):
    if testcellulebord(matrice) == True and indice_cellule_bord == 0:
        indice_cellule_bord = i
    return indice_cellule_bord





















            
    



