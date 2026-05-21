from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["nom", "email", "telephone", "adresse"]
        labels = {
            "nom": "Nom",
            "email": "Email",
            "telephone": "Téléphone",
            "adresse": "Adresse",
        }
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "Nom du client", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "email@exemple.com", "class": "form-control"}),
            "telephone": forms.TextInput(attrs={"placeholder": "06 12 34 56 78", "class": "form-control"}),
            "adresse": forms.TextInput(attrs={"placeholder": "Adresse complète", "class": "form-control"}),
        }

    def clean_nom(self):
        nom = self.cleaned_data.get("nom", "").strip()
        if not nom:
            raise forms.ValidationError("Le nom ne peut pas être vide.")
        return nom

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()
        if not email:
            raise forms.ValidationError("L'email ne peut pas être vide.")
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone", "").strip()
        if not telephone:
            raise forms.ValidationError("Le téléphone ne peut pas être vide.")
        return telephone

    def clean_adresse(self):
        adresse = self.cleaned_data.get("adresse", "").strip()
        if not adresse:
            raise forms.ValidationError("L'adresse ne peut pas être vide.")
        return adresse
