"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create a Pygame game with a ship that moves vertically and fires
lasers horizontally at aliens.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 07/25/2026
"""

import sys

import pygame

from laser import Laser
from ship import Ship


def main():
    """Run the game and handle ship movement and laser firing."""
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion - Track 1")

    clock = pygame.time.Clock()
    ship = Ship(screen)
    lasers = []

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
                elif event.key == pygame.K_SPACE:
                    lasers.append(Laser(screen, ship))

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

        ship.update()

        for laser in lasers:
            laser.update()

        screen_right = screen.get_rect().right
        lasers = [
            laser
            for laser in lasers
            if laser.rect.left < screen_right
        ]

        screen.fill((20, 20, 40))
        ship.draw()

        for laser in lasers:
            laser.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()