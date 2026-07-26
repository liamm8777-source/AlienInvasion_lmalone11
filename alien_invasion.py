"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create a Pygame game with a ship that moves vertically and fires
lasers horizontally at aliens.
Date: 07/25/2026
"""

import sys

import pygame


def main():
    """Initialize Pygame and run the main game loop."""
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion - Track 1")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((20, 20, 40))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()