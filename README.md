# 🎨 Assistant Conseil Couleurs

> Un assistant en ligne de commande qui décrit les propriétés symboliques d'une couleur et génère des suggestions de mariages chromatiques personnalisées, avec aperçu visuel.

---

## 📌 Présentation

**Assistant Conseil Couleurs** est un petit progiciel de conseil artistique développé en Python. À partir d'une couleur saisie par l'utilisateur, il interroge une base de données locale pour :

- Fournir une **description symbolique et culturelle** de la couleur
- Proposer des **couleurs harmonieuses** pour un mariage chromatique réussi
- Générer des **aperçus visuels** (images PNG) directement dans le dossier source

Ce projet a été initié en 2024 dans le cadre d'un apprentissage pratique de Python, de la gestion de bases de données avec SQLite et du traitement d'images avec Pillow.

---

## ✨ Fonctionnalités

- 🗣️ Interface conversationnelle en ligne de commande
- 🗄️ Base de données SQLite embarquée (création, alimentation et suppression automatiques à chaque session)
- 🖼️ Génération d'aperçus couleur au format PNG via la bibliothèque Pillow
- 🎲 Suggestion aléatoire de 3 couleurs mariables parmi une palette prédéfinie
- 🔄 Boucle interactive permettant plusieurs consultations successives
- 💬 Affichage progressif du texte (effet machine à écrire)

---

## 🎨 Couleurs prises en charge

| Français  | Anglais   |
|-----------|-----------|
| Rouge     | Red       |
| Vert      | Green     |
| Bleu      | Blue      |
| Noir      | Black     |
| Jaune     | Yellow    |
| Orange    | Orange    |
| Violet    | Purple    |
| Marron    | Brown     |
| Blanc     | White     |
| Rose      | Pink      |
| Gris      | Grey      |
| Doré      | Gold      |
| Acajou    | —         |
| Argent    | Silver    |
| Beige     | —         |

> Les couleurs peuvent être saisies aussi bien en français qu'en anglais.

---

## 🛠️ Technologies utilisées

| Technologie | Rôle |
|---|---|
| **Python 3** | Langage principal |
| **SQLite3** | Base de données embarquée |
| **Pillow (PIL)** | Génération des aperçus couleur |
| **cx_Freeze** | Compilation en exécutable Windows (.exe) |

---

## 📁 Structure du projet

```
App_Conseil/
├── App_Conseil.py          # Script principal
├── ma_bd.db                # Base de données SQLite (générée à l'exécution)
├── apercue_de_la_couleur.png   # Aperçu de la couleur saisie (généré)
├── couleur_mariable1.png   # 1ère suggestion de mariage (générée)
├── couleur_mariable2.png   # 2ème suggestion de mariage (générée)
├── couleur_mariable3.png   # 3ème suggestion de mariage (générée)
└── build/                  # Dossier de l'exécutable (cx_Freeze)
    └── App_Conseil.exe
```

---

## ⚙️ Installation et exécution

### Prérequis

- Python 3.8 ou supérieur
- pip

### Cloner le dépôt

```bash
git clone https://github.com/<votre-username>/app-conseil-couleurs.git
cd app-conseil-couleurs
```

### Installer les dépendances

```bash
pip install pillow
```

> SQLite3 est inclus nativement dans Python, aucune installation supplémentaire n'est nécessaire.

### Lancer l'application

```bash
python App_Conseil.py
```

---

## 🖥️ Utilisation de la version exécutable (.exe)

Une version compilée avec **cx_Freeze** est disponible pour Windows. Aucune installation de Python n'est requise.

1. Téléchargez le dossier `build/` depuis les [Releases](../../releases)
2. Naviguez jusqu'au dossier `exe.win-.../`
3. Double-cliquez sur `App_Conseil.exe`

> ⚠️ Les fichiers PNG d'aperçu seront générés dans le même dossier que l'exécutable.

---

## 💡 Exemple d'utilisation

```
Assistant : Salut! Je suis un assistant qui vous donne des conseils sur le choix du mariage des couleurs.

 Assistant : Par rapport à quelle couleur avez-vous besoin d'aide? bleu

 Assistant : La couleur bleu est une couleur étroitement liée au rêve, à la sagesse
 et à la sérénité [...]. Elle se marie bien avec le bleu, marron, noir, jaune, gris.

 Assistant: Veuillez consulter le dossier source pour voir l'aperçu des couleurs
 possibles pour le mariage. Merci.
```

Trois fichiers PNG sont également générés dans le dossier source pour un aperçu visuel des couleurs suggérées.

---

## 🚧 Limites connues et améliorations futures

- La base de données est recréée à chaque lancement (pas de persistance entre sessions)
- La reconnaissance des couleurs se base sur une correspondance de chaîne simple
- La palette est actuellement limitée à 15 couleurs
- Pistes d'amélioration : interface graphique (Tkinter/PyQt), palette élargie, export PDF des recommandations

---

## 👤 Auteur

Etudiant en 2ème année de Art Numérique à l'ENSPY — 2024.

---

## 📄 Licence

Ce projet est distribué sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.
