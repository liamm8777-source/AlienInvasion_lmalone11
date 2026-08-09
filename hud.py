"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Display the score, high score, and lives remaining.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 08/08/2026
"""

import pygame


class HUD:
    """Display the game's score, high score, and lives."""

    def __init__(self, screen):
        """Create the HUD."""
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.text_color = (255, 255, 255)

    def draw(self, score, high_score, lives):
        """Draw the score, high score, and lives remaining."""
        score_text = self.font.render(
            f"Score: {score}",
            True,
            self.text_color
        )
        high_score_text = self.font.render(
            f"High Score: {high_score}",
            True,
            self.text_color
        )
        lives_text = self.font.render(
            f"Lives: {lives}",
            True,
            self.text_color
        )

        self.screen.blit(score_text, (20, 20))

        high_score_rect = high_score_text.get_rect()
        high_score_rect.midtop = (
            self.screen.get_rect().centerx,
            20
        )
        self.screen.blit(high_score_text, high_score_rect)

        lives_rect = lives_text.get_rect()
        lives_rect.topright = (
            self.screen.get_rect().right - 20,
            20
        )
        self.screen.blit(lives_text, lives_rect)