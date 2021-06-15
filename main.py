from conversionApp import *

def main():

    # Variable de passage 
    continuer = True

    print("Super Convertisseur Dgré-Radian")

    # Boucle principale pour faire le chiox de converssion
    while continuer:
        # Affichage du menu 
        choix = Menu()
        # Traitement du choix de l'utilisateur comme une chaine des caracteur 
        if choix == "1":
            # Prendre et convertir l'angle 
            deg = float(input("Mesure de L'angle en degré: "))
            # Affiche le resultat en le convertisant en chaine de caract̀ères
            print("Mesure en radian : " + str(degre_en_rad(deg)))
            # Demande si l'on veux continuer 
            continuer = demande_continuer()
        elif choix == "2":
            # Idem dans l'autre sence de conversion 
            rad = float(input("Mesure de l'engle en radian : "))
            print("Mesure en degré : " + str(radians_en_deg(rad)))
            continuer = demande_continuer()
        elif choix == "q":
            # On veux quitter 
            continuer = False 
        else:
            print("Option inconnue")

    print("\n Ce convertisseur vous est juteusement offert par Ash, cn")



if __name__ == "__main__":
    main()