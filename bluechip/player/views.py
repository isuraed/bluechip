import random
from django.shortcuts import render
from models import Player, Position, Pitch, PitchWeight


def create_players(request):
	#TODO: Need to centralize this function call.
	random.seed(123456789)

	# For now just create a new class each
	Player.objects.all().delete()
	PitchWeight.objects.all().delete()
	for _ in xrange(3000):
		p = Player.objects.create_player()
		Player.objects.create_pitch_weights(p)
	
	return render(request, 'player/done.html')


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


def profile(request, player_id):
	player_id = int(player_id)
	p = Player.objects.get(id=player_id)
	pitch_weights = PitchWeight.objects.filter(player=p)
	return render(request, 'player/profile.html', 
		{'player': p, 'pitch_weights': pitch_weights})

# def qb(request):
# 	players_list = Player.objects.filter(position__name__contains="QB")
# 	return render(request, 'players.html', {'players_list': players_list})