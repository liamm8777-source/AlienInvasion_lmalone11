"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create a Pygame game with a ship that moves vertically and fires
lasers horizontally at aliens.
Date: 07/25/2026
"""

import sys

import pygame

from ship import Ship


def main():
    """Run the game and handle ship movement."""

    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion - Track 1")

    clock = pygame.time.Clock()
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

        ship.update()
        screen.fill((20, 20, 40))
        ship.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
