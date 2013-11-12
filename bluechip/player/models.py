from django.db import models
from distribution import Distribution


class FirstName(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __unicode__(self):
        return self.name


class LastName(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __unicode__(self):
        return self.name
        

class State(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __unicode__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.IntegerField()

    def __unicode__(self):
        return self.name


class TalentProfile(models.Model):
    name = models.CharField(max_length=255)


class ProfilePoint(models.Model):
    talent_profile = models.ForeignKey(TalentProfile)
    grade = models.IntegerField()
    frequency = models.IntegerField()


class PlayerManager(models.Manager):
    def __init__(self):
        super(PlayerManager, self).__init__()
        self.first_name_dist = Distribution(self.create_frequency_dist("FirstName"))
        self.last_name_dist = Distribution(self.create_frequency_dist("LastName"))
        self.state_dist = Distribution(self.create_frequency_dist("State"))
        self.position_dist = Distribution(self.create_frequency_dist("Position"))
        self.talent_dist = Distribution(self.create_frequency_dist("ProfilePoint"))

    @classmethod
    def create_frequency_dist(self, modelName):
        records = None
        if modelName == "FirstName":
            records = FirstName.objects.all()
        elif modelName == "LastName":
            records = LastName.objects.all()
        elif modelName == "State":
            records = State.objects.all()
        elif modelName == "Position":
            records = Position.objects.all()
        elif modelName == "ProfilePoint":
            # TODO: Get profile points through TalentProfile
            records = ProfilePoint.objects.all()

        frequency_dist = []
        for row in records:
            frequency_dist.append((row.id, row.frequency))

        return frequency_dist

    def create_player(self):
        first_name_id = self.first_name_dist.generate_value()
        last_name_id = self.last_name_dist.generate_value()
        state_id = self.state_dist.generate_value()
        position_id = self.position_dist.generate_value()
        profile_point_id = self.talent_dist.generate_value()

        first_name = FirstName.objects.get(id=first_name_id)
        last_name = LastName.objects.get(id=last_name_id)
        state = State.objects.get(id=state_id)
        position = Position.objects.get(id=position_id)
        profile_point = ProfilePoint.objects.get(id=profile_point_id)
        grade = profile_point.grade

        player = self.create(first_name=first_name,
                             last_name=last_name,
                             state=state,
                             position=position,
                             grade=grade)

        return player

        
class Player(models.Model):
	first_name = models.ForeignKey(FirstName)
	last_name = models.ForeignKey(LastName)
	state = models.ForeignKey(State)
	position = models.ForeignKey(Position)
	grade = models.IntegerField()

	objects = PlayerManager()


class Pitch(models.Model):
    name = models.CharField(max_length=255)


class PitchWeight(models.Model):
    player = models.ForeignKey(Player)
    pitch = models.ForeignKey(Pitch)
    weight = models.DecimalField(max_digits=4, decimal_places=4)
