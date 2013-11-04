import random
from models import Player

def create_players():
	#TODO: Need to centralize this function call.
	random.seed(123456789)

	# TODO: Do we need to delete all?
	Player.objects.all().delete()
	for _ in xrange(3000):
		p = Player.objects.create_player()
		p.save