from django.shortcuts import render
from models import Player, Position

def home(request):
	positions = Position.objects.all()
	return render(request, 'player/home.html', {'positions': positions})


def all(request):
	players_list = Player.objects.all().order_by('-grade')
	return render(request, 'player/table.html', {'players_list': players_list})


def top_100(request):
	players_list = Player.objects.all().order_by('-grade')[:100]
	return render(request, 'player/table.html', {'players_list': players_list})


def by_position(request, position_name):
	players_list = Player.objects.filter(position__name=position_name).order_by('-grade')
	return render(request, 'player/table.html', {'players_list': players_list})


# def qb(request):
# 	players_list = Player.objects.filter(position__name__contains="QB")
# 	return render(request, 'players.html', {'players_list': players_list})