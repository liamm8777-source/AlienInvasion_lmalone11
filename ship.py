"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create and display the player's spaceship.
Date: 07/25/2026
"""

from pathlib import Path

import pygame


class Ship:
    

    def __init__(self, screen):
        """Load the ship image and place it on the left side."""
        self.screen = screen

        image_path = Path(__file__).parent / "Assets" / "images" / "ship.png"
        original_image = pygame.image.load(str(image_path)).convert_alpha()

        self.image = pygame.transform.rotate(original_image, -90)
        self.image = pygame.transform.scale(self.image, (90, 62))
        self.rect = self.image.get_rect()

        screen_rect = self.screen.get_rect()
        self.rect.midleft = (20, screen_rect.centery)

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)