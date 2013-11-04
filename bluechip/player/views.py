from django.shortcuts import render
from django.template import Context, loader
from models import Player

def bootstrap(request):
	return render(request, 'bootstrap.html')

def players(request):
	players_list = Player.objects.all()
	t = loader.get_template('players.html')
	c = Context({'players_list': players_list, })
	return render(request, 'players.html', {'players_list': players_list})