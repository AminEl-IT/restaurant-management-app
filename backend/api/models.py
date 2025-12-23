from django.db import models

# Create your models here.

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)      # Texte court (200 caractères max)
    address = models.CharField(max_length=300)   # Texte pour l'adresse
    contact = models.CharField(max_length=50)    # Numéro de téléphone

    def __str__(self):
        return self.name  # Affiche le nom dans l'admin Django

#Explication : Les models = structure de ta base de données. Django va créer automatiquement les tables SQL pour toi.#