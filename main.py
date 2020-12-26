import fonctions as f
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Cette partie contient les parametres de la matrice et les parametres a l'etat initial
#==============================================================================

nombredesimulation = 60

# variables liees a la taille de la matrice
nombre_de_lignes = 30
nombre_de_colones = 30

# variables liees a l'oxygen
quantiteO2i = 0  # quantite initiale en oxygene dans chaque case de la matrice
alimentation_O2 = 0  # cette variable est la quantitee d oxygen ajoute par bocle dans la case cenrale de la matrice, elle intervient dans la fonction alimentation O2
variationO2sicellule = 10  # variation de la quantite d oxygen dans une casi si il y a une cellule
nombreegalisationO2 = 0*nombre_de_lignes*nombre_de_colones  # nombre de fois que les cases sont moyennees

# variables liees au dioxyde de carbon
quantiteCO2i = 100  # quantite initiale en dioxyde de carbon dans chaque case de la matrice 
variationCo2sicellule = -10  # variation de la quantite da dioxyde de carbon dans une casi si il y a une cellule
limiteco2 = 10 # limite au dela de laquelle la cellule peut se diviser
alimentation_CO2 = 0
nombreegalisationCO2 = 10*nombre_de_lignes*nombre_de_colones

# variables liees au temps
dureeboucle = 1  # n'affecte que la duree de vie des cellules
dureeminimaleentredeuxdivisions = 2  # homogene au temps d'une boucle // l'incrementation de cette variable au sein du programme est gere dans la fonction modificationvie
ageminimaldedivision = 2  # age minimum de la cellule pour que la division soit possible
age_maximal_cellule = 10

# variables non modifiables
indice_cellule_bord = 0
nombre_de_cellules_au_cour_du_temps = []
qte_O2_au_cours_du_temps = []

#==============================================================================
# Boucle
#==============================================================================


print ()
print (" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Demarrage ")
print ()

matrice = f.creermatriceS(nombre_de_colones,nombre_de_lignes,quantiteO2i,quantiteCO2i)

for i in range (1,nombredesimulation+1):
    
# fonctions O2
    matrice = f.modificationO2 (matrice,variationO2sicellule)
    matrice = f.egaliserO2 (matrice,nombreegalisationO2)
    matrice = f.alimentationO2(matrice,alimentation_O2)
# fonctions CO2
    matrice = f.modificationCO2 (matrice,variationCo2sicellule)
    matrice = f.egaliserCO2 (matrice,nombreegalisationCO2)
    matrice = f.alimentationCO2(matrice,alimentation_CO2)
# autres fonctions
    matrice = f.proliferationdesalgues(matrice,limiteco2,dureeminimaleentredeuxdivisions,ageminimaldedivision)
    matrice = f.modificationvie (matrice,dureeboucle)
    nombre_de_cellules_au_cour_du_temps += [f.nombredecellules(matrice)]
    qte_O2_au_cours_du_temps += [f.nombre02(matrice)]
    indice_cellule_bord = f.indicecellulebord(matrice,indice_cellule_bord,i)
    matrice = f.mortdescellules (matrice,age_maximal_cellule)
    f.enregistrer_matrice (matrice,i)
# affichage du processus
    print (int(100*i/(nombredesimulation+1)))

print (" <<<<<<<<<<<<<<< fin du pogramme")

#==============================================================================
# Dans cette partie il s'agit de representer le nombre de cellules au cour du tamps
#==============================================================================

absisses = np.arange(0,len(nombre_de_cellules_au_cour_du_temps),1)
plt.subplot(211)
plt.plot(absisses,nombre_de_cellules_au_cour_du_temps,"b--")
plt.subplot(212)
plt.plot(absisses,qte_O2_au_cours_du_temps)
plt.show()

