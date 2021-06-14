from math import pi as p

# Table of contentes 
"""
    1. Menu
        - Ask for the value of the angle if yes 
        - If not Quit 
        - If yes keep prompting the user by printing the menu 
    2. convert (user the formular) 
    3. Display the result 
"""


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
            deg = float(input("Mesure en degré: "))
            # Affiche le resultat en le convertisant en chaine de caract̀ères
            print("Mesure en radian : " + str(degre_en_rad(deg)))
            # Demande si l'on veux continuer 
            continuer = demande_continuer()
        elif choix == "2":
            # Idem dans l'autre sence de conversion 
            rad = float(input("Mesure en radian : "))
            print("Mesure en degré : " + str(radians_en_deg(rad)))
            continuer = demande_continuer()
        elif choix == "q":
            # On veux quitter 
            continuer = False 
        else:
            print("Option inconnue")

print("\n Ce convertisseur vous est juteusement offert par Ash, cn")



# Menu
def Menu():
    print("\nOptions disponibles :")
    print("1 : Convertir des degrés en radians")
    print("2 : Convertir des radians en degrés")
    print("q : Quitter\n")
    return input("Votre choix : ")

# Conversion  
# Convertir des degrés en radians  
def degre_en_rad(deg):
    return deg * 180 / p

# Conertir des radians en degrés 
def radians_en_deg(rad):
    return rad * p / 180

# Demande conversion ou arret 
def demande_continuer():
    # On demande si l'utilisateur veut quitter avant de réafficher le menu
    reponse = input("Effectuer une autre conversion ? (Oui/Non) : \n")
    string1 = "Oui"
    if reponse == string1.lower():
        return True
    else:
        return False



if __name__ == "__main__":
    main()