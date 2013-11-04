import random
from player.models import Player

#TODO: Need to centralize this function call.
random.seed(123456789)

# For now just create a new class each
Player.objects.all().delete()
for _ in xrange(3000):
	p = Player.objects.create_player()
	p.save