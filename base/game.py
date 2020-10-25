import random


class Game:

    def __init__(self, name='My Games'):
        self.id = id
        self.name = name
        self.nums = list(range(0, 100))
        self.pop = 0
        self.history = []

    def start(self):
        return self.pop, self.history

    def next(self):
        random.shuffle(self.nums)
        self.pop = self.nums.pop()
        self.history.insert(0, self.pop)
        return self.pop

    def numbers_exists(self):
        return len(self.nums) > 0

    def get_last_n_numbers(self, n=10):
        return self.history[1:n+1]
