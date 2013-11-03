import random


class Distribution:
    def __init__(self, frequency_dist):
        self.cumulative_dist = []
        self.total_freq = 0
        for point in frequency_dist:
            self.cumulative_dist.append((point[0], self.total_freq + point[1]))
            self.total_freq += point[1]

    def generate_value(self):
        pick = random.randint(1, self.total_freq)
        for point in self.cumulative_dist:
            if pick <= point[1]:
                return point[0]