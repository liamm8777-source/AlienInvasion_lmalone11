"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create and display the Play button for the game.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 08/07/2026
"""

import pygame


class Button:
    """Represent the game's Play button."""

    def __init__(self, screen):
        """Create a Play button in the center of the screen."""
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 200, 60)
        self.rect.center = screen.get_rect().center

        self.font = pygame.font.Font(None, 48)
        self.text = self.font.render("Play", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self):
        """Draw the Play button."""
        pygame.draw.rect(
            self.screen,
            (0, 120, 200),
            self.rect
        )
        self.screen.blit(self.text, self.text_rect)

    def is_clicked(self, mouse_position):
        """Return True when the mouse clicks inside the button."""
        return self.rect.collidepoint(mouse_position)