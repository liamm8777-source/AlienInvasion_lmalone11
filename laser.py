"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create and move lasers fired by the player's spaceship.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 07/25/2026
"""

import pygame


class Laser:
    """Represent a laser fired by the player's spaceship."""

    def __init__(self, screen, ship):
        """Create a laser at the right side of the ship."""
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 18, 4)
        self.rect.midleft = ship.rect.midright
        self.speed = 8

    def update(self):
        """Move the laser horizontally toward the right."""
        self.rect.x += self.speed

    def draw(self):
        """Draw the laser on the screen."""
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            self.rect
        )