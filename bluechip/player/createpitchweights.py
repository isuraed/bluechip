import random
from player.models import Player, Pitch, PlayerPitchWeight

#TODO: Need to centralize this function call.
random.seed(123456789)

pitch_records = Pitch.objects.all().order_by('id')
pitches_count = pitch_records.count()
for p in Player.objects.all():
	weights = []
	sum_weights = 0
	for _ in xrange(pitches_count):
		mu = 1.0 / pitches_count
		sigma = (2.0 / 3.0) * mu
		w = random.normalvariate(mu, sigma)
		w = max(w, 0.0)
		weights.append(w)
		sum_weights += w

	# Normalize weights before creating records
	for i in xrange(len(weights)):
		weights[i] /= sum_weights

	j = 0
	for pitch in pitch_records:
		ppw = PlayerPitchWeight(player=p, pitch=pitch, weight=weights[j])
		ppw.save()
		j += 1
