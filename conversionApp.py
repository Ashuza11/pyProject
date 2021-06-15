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
# This is my functions 

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