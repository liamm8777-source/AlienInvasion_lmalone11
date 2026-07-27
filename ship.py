"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create and display the player's spaceship.
Date: 07/25/2026
"""

from pathlib import Path

import pygame


class Ship:
    """Represent the player's ship."""

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
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move the ship vertically while keeping it on the screen."""
        if self.moving_up:
            self.rect.top = max(0, self.rect.top - 5)
        if self.moving_down:
            screen_bottom = self.screen.get_rect().bottom
            self.rect.bottom = min(screen_bottom, self.rect.bottom + 5)

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)
