from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Party, Clown
from .forms import PartyForm, ClownForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def party_list(request):
    parties = Party.objects.all()
    clowns = Clown.objects.all()
    return render(request, 'party_list.html', {'parties': parties, 'clowns': clowns, 'form': PartyForm(), 'clown_form' : ClownForm() })
    # pass

def party_detail(request, pk):
    clowns = Clown.objects.all()
    party = Party.objects.get(id=pk)
    return render(request, 'party_detail.html', {'party': party, 'clowns': clowns } )

def clown_detail(request, pk):
    party = Party.objects.all()
    clowns = Clown.objects.get(id=pk)
    return render(request, 'clown_detail.html', {'party': party, 'clowns': clowns})

class PartyDelete(DeleteView):
    model = Party
    success_url = reverse_lazy("party_list")

class PartyUpdate(UpdateView):
    model = Party
    fields = ['title', 'location', 'description']
    success_url = reverse_lazy("party_list")

class PartyCreate(CreateView):
    model = Party
    fields = ["title","location","description"]
    success_url = reverse_lazy("party_list")

class PartyUpdate(UpdateView):
    model = Party
    fields = ['title', 'location', 'description']
    success_url = reverse_lazy("party_list")

class ClownCreate(CreateView):
    model = Clown
    fields = ["name","description"]
    success_url = reverse_lazy("party_list")
