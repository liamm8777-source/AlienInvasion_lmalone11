"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create and display an alien in the game's fleet.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 08/01/2026
"""

from pathlib import Path

import pygame


class Alien:
    """Represent one alien in the fleet."""

    def __init__(self, screen, x_position, y_position):
        """Load an alien image and place it at the given position."""
        self.screen = screen

        image_path = (
            Path(__file__).parent
            / "Assets"
            / "images"
            / "enemy_4.png"
        )
        original_image = pygame.image.load(str(image_path)).convert_alpha()

        self.image = pygame.transform.scale(
            original_image,
            (60, 60)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def draw(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)