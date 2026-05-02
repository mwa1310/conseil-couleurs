import random
from PIL import Image
import sqlite3
import time
import os

#Introduction de l'assistant
print("Assitant : Salut! Je suis un assistant qui vous donne des conseils sur le choix du mariage des couleurs.")
print()
while True:
#Generation de la palette des recommandées
    def recommander_couleurs(n):
        return random.choices(couleurs_recommandees, k=n)
    
# Définition d'une liste de couleurs possibles
    couleurs_recommandees = ["rouge", "vert", "bleu", "noir", "jaune", "orange", "violet", "marron", "blanc", "rose", "gris", "doré"]
    
    def print_slowly(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
    

    width = 200
    height = 200

#Creation de la base de donnee
# Connexion à la base de donnees
    conn = sqlite3.connect('ma_bd.db')

# Creation d'un curseur
    cursor = conn.cursor()

# Creation de la table utilisateurs
    cursor.execute('''CREATE TABLE utilisateurs (
                        nom_couleur VARCHAR PRIMARY KEY,
                        description_couleur TEXT,
                        couleurs_compatibles TEXT)''')

# Insertion d'un utilisateur dans la table
#Rouge
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('red', 'est symbole de colère, d interdiction, de danger, d amour, de passion, de chaleur, de sexualité, d ardeur, de triomphe; Elle s impose comme une couleur chaleureuse, énergique, pénétrante et d une certaine manière rassurante et enveloppante', 'le bleu, vert, noir, blanc, gris')")
#Vert
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('green', 'est une couleur qui représente le mieux la nature; Elle est symbole de chance, de stabilité, de concentration, d échec, d infortune, d espérance', 'le bleu, rose, noir, blanc, gris')")
#Bleu
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('blue', 'est une couleur étroitement liée au rêve, à la sagesse et à la sérénité; Le bleu est symbole de vérité, de rêve, de sagesse, de sérénité, de loyauté, de fraîcheur', 'le bleu, marron, noir, jaune, gris')")
#Noir
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('black', 'est la couleur sombre par excellence; Elle est symbole de mort, de deuil, de tristesse, de vide, d obscurité, d élégance, de simplicité, de sobriété, de rigueur, de mystère', 'toutes les couleurs: le bleu, vert, noir, blanc, gris, ...')")
#Jaune
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('yellow', 'est la couleur la plus joyeuse; Elle est symbole de fête, de joie, de chaleur, d égo, de puissance, de connaissance, d amitié, de traîtrise, de mensonge, de tromperie', 'le bleu, marron, noir, blanc, gris')")
#Orange
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('orange', 'est une couleur tonifiante et piquante qui insuffle partout où elle passe une dose de bonne humeur, de joie, de créativité, de communication, de sécurité, d optimisme, de kitch', 'le jaune, vert, violet, blanc, gris')")
#Violet
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('purple', 'a des vertus apaisantes sur les esprits; Elle est symbole de rêve, de délicatesse, de paix, d amitié, de méditation, de mélancolie, de solitude', 'le rouge, orange, noir, blanc, marron')")
#Marron
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('brown', 'est la couleur de la terre par excellence; Elle est symbole de nature, de douceur, de neutralité', 'le jaune, bleu, noir, blanc, violet')")
#Blanc
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('white', 'représente la pureté de la mariée, de la feuille blanche; Elle est symbole de pureté, d innocence, de virginité, de mariage', 'toutes les couleurs: le bleu, vert, noir, blanc, gris, ....')")
#Rose
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('pink', 'est la couleur des filles; Elle est symbole de féminité, de romantisme, de séduction, de bonheur, de tendresse, de jeunesse', 'le bleu, vert, rouge, blanc, marron')")
#Gris
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('grey', 'est une couleur neutre; Elle est symbole de calme, de douceur, de tristesse, de solitude, de monotonie, de mélancolie', 'pratiquement toutes les couleurs: le bleu, vert, noir, blanc, gris, ...')")
#Dore
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('gold', 'est la couleur du faste et du luxe; Elle est symbole de richesse, de fortune, de fécondité', 'le marron, rouge, noir, blanc, gris')")
#Acajou
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('acajou', 'est un brun aux nuances de rouge, une teinte toujours un peu empreinte de magie lorsque reprise dans la décoration, sur des vêtements, dans la couleur des cheveux; Elle inspire, rappelle la terre, ses origines, la nature, évoque la chaleur, rassure; Elle représente la force, le courage, la continuité, le lourd d histoire, le vécu ancien, les croyances tribales.', 'le beige, le turquoise, le vert, le blanc teinté de nuances bleues')")
#Argent
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('silver', 'est une couleur froide, et associée à une certaine forme de richesse et d opulence; Elle est aussi synonyme de fêtes et de faste; Elle incarne le futur, les nouvelles technologies, la lune, ce qui accentue sa féminité, et sa prestance, la richesse, l’élégance, le strass, la froideur du métal, le vide, l’épurement total.', 'le cuivre, le turquoise, le bleu, le violet')")
#Beige
    cursor.execute("INSERT INTO utilisateurs (nom_couleur, description_couleur, couleurs_compatibles) VALUES ('beige', 'est  une couleur qui a tout d une couleur discrète, simple et efficace, reposante et invitant au respect et au silence; Elle offrirait une vision du monde archaïque et instinctive, un mode de fonctionnement tourné vers les besoins essentiels à la survie, selon une étude; Elle est douce, chaleureuse dans le sens qu elle tient chaud au mental et au coeur, symbolise l élégance, la sobriété excessive, la morosité, la neutralité, la capacité à se conjuguer, est classieuse.', 'le bleu, le blanc, le marron, le noir, le rouge, le rose')")

# Validation des modifications
    conn.commit()

#Traitement de la question 
    question = input(" Assistant : Par rapport à quelle couleur avez-vous besoin d'aide? ")

    def envoyer():
        if ("rouge" or "red") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'red' ")
            result = cursor.fetchone()
        elif ("vert" or "green") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'green' ")
            result = cursor.fetchone()
        elif ("bleu" or "blue") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'blue' ")
            result = cursor.fetchone()
        elif ("noir" or "black") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'black' ")
            result = cursor.fetchone()
        elif ("jaune" or "yellow") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'yellow' ")
            result = cursor.fetchone()
        elif "orange" in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'orange' ")
            result = cursor.fetchone()
        elif ("violet" or "purple") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'purple' ")
            result = cursor.fetchone()
        elif ("marron" or "brown") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'brown' ")
            result = cursor.fetchone()
        elif ("blanc" or "white") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'white' ")
            result = cursor.fetchone()
        elif ("rose" or "pink") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'pink' ")
            result = cursor.fetchone()
        elif ("gris" or "grey") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'grey' ")
            result = cursor.fetchone()
        elif ("dore" or "gold") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'gold' ")
            result = cursor.fetchone()
        elif ("acajou") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'acajou' ")
            result = cursor.fetchone()    
        elif ("argent" or "silver") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'silver' ")
            result = cursor.fetchone()
        elif ("beige") in question:
            cursor.execute("SELECT * FROM utilisateurs WHERE nom_couleur = 'beige' ")
            result = cursor.fetchone()
        else : 
            result= cursor.fetchone()
        return result
    result = envoyer()

#Affichage du resultat + affichage de l'aperçue de la couleur + génération des couleurs pour mariage
    if result is not None:
        nom_couleur, description_couleur, couleurs_compatibles = result

        if nom_couleur=="red":
            color='red'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show() 
            print_slowly(f" Assistant : La couleur rouge {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "green"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = [ "black", "grey"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = [ "green", "blue"] 
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="green":
            color='green'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur vert {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["pink", "white"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["blue", "black"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["pink","grey"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="blue":
            color='blue'
            print_slowly(f" Assistant : La couleur bleu {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            width = 200
            height = 200
            colors1 = ["black", "yellow"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["brown", "grey"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["blue", "white"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="black":
            color='black'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur noir {description_couleur}. Elle se marie bien avec {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "green"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["pink", "grey"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = [ "red", "blue"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="yellow":
            color='yellow'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur jaune {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["black", "grey"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["white", "brown"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["blue", "gold"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="orange":
            color='orange'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur orange {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "green"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["yellow", "brown"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["black", "grey"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="purple":
            color='purple'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur violet {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = [ "blue", "black"]  
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["orange", "brown"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["red", "white"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="brown":
            color='brown'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur marron {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "blue"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["yellow", "black"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["purple", "grey"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="white":
            color='white'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur blanc {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["black", "grey"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["yellow", "orange"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["pink", "gold"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="pink":
            color='pink'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur rose {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "green"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = [ "blue", "black"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["brown", "red"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="grey":
            color='grey'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur gris {description_couleur}. Elle se marie bien avec {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = ["white", "green"] 
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["black", "orange"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["blue", "grey"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="gold":
            color='gold'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur dore {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = [ "black", "grey"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["red", "brown"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["yellow", "white"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="acajou":
            color='#88421d'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur acajou {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = [ "beige"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["green"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["turquoise"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")
       
        if nom_couleur=="silver":
            color='silver'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur argent {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = [ "blue"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["turquoise"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["black", "#b36700"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")

        if nom_couleur=="beige":
            color='beige'
            image = Image.new("RGB", (width, height), color)
            image.save("apercue_de_la_couleur.png")
            image = Image.open("apercue_de_la_couleur.png")
            image.show()
            print_slowly(f" Assistant : La couleur beige {description_couleur}. Elle se marie bien avec: {couleurs_compatibles}.")
            print()
            width = 200
            height = 200
            colors1 = [ "blue","pink"]   
            color1=random.choice(colors1) #  (RVB))
            image1 = Image.new("RGB", (width, height), color1)
            image1.save("couleur_mariable1.png")
            colors2 = ["white", "red"]  
            color2=random.choice(colors2) #  (RVB))
            image2 = Image.new("RGB", (width, height), color2)
            image2.save("couleur_mariable2.png")
            colors3 = ["black", "brown"]  
            color3=random.choice(colors3) #  (RVB))
            image3 = Image.new("RGB", (width, height), color3)
            image3.save("couleur_mariable3.png")
    else:
        print_slowly(" Désolé la base de données ne contient pas la donnée que vous avez entré. Notre base de données grandira avec les prochaines mise à jour. Merci pour votre compréhension!  ")
        print()
        print()

    if result is not None:
        print_slowly(" Assistant: Veuillez consulter le dossier source pour voir l'apercu des couleurs possibles pour le mariage. Merci.")
        print()
        print()

#Suppression de la table
    cursor.execute('''DROP TABLE utilisateurs''')
# Fermeture de la connexion
    conn.close()