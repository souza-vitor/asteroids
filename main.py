import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=(0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000

if __name__ == "__main__":
    main()

