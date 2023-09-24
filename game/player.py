class Player:
    def __init__(self, name):
        self.name = name
        self.x = 300
        self.y = 200
        self.score = 0

    def increase_score(self):
        self.score += 1
