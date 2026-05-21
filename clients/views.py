from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientForm
from .models import Client


def liste_clients(request):
    recherche = request.GET.get("q", "").strip()
    clients = Client.objects.all()
    if recherche:
        clients = clients.filter(nom__icontains=recherche)
    return render(
        request,
        "clients/liste.html",
        {"clients": clients, "recherche": recherche},
    )


def ajouter_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client ajouté avec succès.")
            return redirect("liste_clients")
    else:
        form = ClientForm()
    return render(request, "clients/formulaire.html", {"form": form, "titre": "Ajouter un client"})


def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client modifié avec succès.")
            return redirect("liste_clients")
    else:
        form = ClientForm(instance=client)
    return render(
        request,
        "clients/formulaire.html",
        {"form": form, "titre": "Modifier le client", "client": client},
    )


def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        nom = client.nom
        client.delete()
        messages.success(request, f'Client "{nom}" supprimé avec succès.')
        return redirect("liste_clients")
    return render(request, "clients/confirmer_suppression.html", {"client": client})
