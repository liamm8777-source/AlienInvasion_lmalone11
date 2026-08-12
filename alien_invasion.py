"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create a Pygame game with a Play button, HUD, ship, lasers,
alien fleet, collisions, lives, and game states.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 07/25/2026
"""

import sys

import pygame

from alien import Alien
from button import Button
from hud import HUD
from laser import Laser
from ship import Ship


def create_fleet(screen):
    """Create a small alien fleet on the right side of the screen."""
    aliens = []

    start_x = screen.get_rect().right - 180
    start_y = 100
    horizontal_spacing = 80
    vertical_spacing = 100

    for column in range(2):
        for row in range(6):
            x_position = start_x + (column * horizontal_spacing)
            y_position = start_y + (row * vertical_spacing)

            aliens.append(
                Alien(screen, x_position, y_position)
            )

    return aliens


def check_laser_alien_collisions(lasers, aliens):
    """Remove collisions and return lasers and number of aliens hit."""
    remaining_lasers = []
    aliens_destroyed = 0

    for laser in lasers:
        alien_hit = None

        for alien in aliens:
            if laser.rect.colliderect(alien.rect):
                alien_hit = alien
                break

        if alien_hit is not None:
            aliens.remove(alien_hit)
            aliens_destroyed += 1
        else:
            remaining_lasers.append(laser)

    return remaining_lasers, aliens_destroyed


def restart_game(screen, ship, lasers, aliens):
    """Reset the ship, lasers, and alien fleet."""
    ship.rect.midleft = (20, screen.get_rect().centery)
    ship.moving_up = False
    ship.moving_down = False

    lasers.clear()
    aliens.clear()
    aliens.extend(create_fleet(screen))


def check_loss_conditions(ship, aliens):
    """Return True when an alien hits the ship or left edge."""
    return any(
        alien.rect.colliderect(ship.rect) or alien.rect.left <= 0
        for alien in aliens
    )


def main():
    """Run the game and manage gameplay, HUD, lives, and game states."""
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion - Track 1")

    clock = pygame.time.Clock()
    ship = Ship(screen)
    lasers = []
    aliens = create_fleet(screen)
    play_button = Button(screen)
    hud = HUD(screen)

    game_active = False
    score = 0
    high_score = 0
    lives = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_active and play_button.is_clicked(event.pos):
                    score = 0
                    lives = 3
                    restart_game(screen, ship, lasers, aliens)
                    game_active = True

            elif event.type == pygame.KEYDOWN and game_active:
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    lasers.append(Laser(screen, ship))

            elif event.type == pygame.KEYUP and game_active:
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False

        if game_active:
            ship.update()

            for laser in lasers:
                laser.update()

            for alien in aliens:
                alien.update()

            screen_right = screen.get_rect().right
            lasers = [
                laser
                for laser in lasers
                if laser.rect.left < screen_right
            ]

            lasers, aliens_destroyed = (
                check_laser_alien_collisions(lasers, aliens)
            )

            score += aliens_destroyed * 100

            if score > high_score:
                high_score = score

            if check_loss_conditions(ship, aliens):
                lives -= 1

                if lives > 0:
                    restart_game(screen, ship, lasers, aliens)
                else:
                    game_active = False
                    ship.moving_up = False
                    ship.moving_down = False

        pygame.mouse.set_visible(not game_active)

        screen.fill((20, 20, 40))
        ship.draw()

        for laser in lasers:
            laser.draw()

        for alien in aliens:
            alien.draw()

        hud.draw(score, high_score, lives)

        if not game_active:
            play_button.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()