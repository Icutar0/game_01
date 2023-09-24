import random
import time

class Square:
    def __init__(self):
        self.x = random.randint(0, 575)
        self.y = random.randint(0, 375)
        self.color = (255, 0, 0)
        self.width = 25
        self.height = 25
        self.creation_time = time.time()

    def should_remove(self):
        return time.time() - self.creation_time >= 5