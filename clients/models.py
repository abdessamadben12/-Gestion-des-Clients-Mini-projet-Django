from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.CharField(max_length=255, verbose_name="Adresse")
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.nom
