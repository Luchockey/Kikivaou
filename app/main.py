import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import pandas as pd

# Définir les postes et les jours
postes = ['AMP', 'Assistant', 'Polyvalent', 'Moulins', 'Décantation', 'Sécheur Gluten', 'Amidonnerie', 'Ligne 1', 'Ligne 2', 'Ligne 3', 'Ligne 4', 'Mélanges', 'Chargements Sirops']
jours = ['Matin 1', 'Matin 2', 'Après-Midi 1', 'Après-Midi 2', 'Nuit 1', 'Nuit 2']

# Définir les données pour remplir le tableau
donnees = {
    'Matin 1': ['Donnée 1', 'Donnée 2', 'Donnée 3'],
    'Matin 2': ['Donnée 4', 'Donnée 5', 'Donnée 6'],
    'Après-Midi 1': ['Donnée 7', 'Donnée 8', 'Donnée 9'],
    'Après-Midi 2': ['Donnée 10', 'Donnée 11', 'Donnée 12'],
    'Nuit 1': ['Donnée 13', 'Donnée 14', 'Donnée 15'],
    'Nuit 2': ['Donnée 16', 'Donnée 17', 'Donnée 18']
}

# Créer un tableau avec les données
tableau = pd.DataFrame(donnees, index=postes)

print(tableau)