import random


class Distribution:
    def __init__(self, frequency_dist):
        self.weighted_values = []
        for point in frequency_dist:
            freq = point[1]
            if freq > 0:
                for n in xrange(freq):
                    self.weighted_values.append(point[0])


    def generate_value(self):
        return random.choice(self.weighted_values)