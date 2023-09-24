import pygame
import time
import game
import player
import square
import database

def main():
    pygame.init()
    game_instance = game.Game()

    while True:
        game_instance.run()

if __name__ == "__main__":
    main()