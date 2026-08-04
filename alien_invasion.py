"""
Program: Alien Invasion - Track 1
Author: Liam Malone
Purpose: Create a Pygame game with a ship, lasers, and a moving alien fleet.
Starter Code: Based on the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: 07/25/2026
"""

import sys

import pygame

from alien import Alien
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
    """Remove lasers and aliens that collide with each other."""
    remaining_lasers = []

    for laser in lasers:
        alien_hit = None

        for alien in aliens:
            if laser.rect.colliderect(alien.rect):
                alien_hit = alien
                break

        if alien_hit is not None:
            aliens.remove(alien_hit)
        else:
            remaining_lasers.append(laser)

    return remaining_lasers


def main():
    """Run the game and handle the ship, lasers, fleet, and collisions."""
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion - Track 1")

    clock = pygame.time.Clock()
    ship = Ship(screen)
    lasers = []
    aliens = create_fleet(screen)

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

        for alien in aliens:
            alien.update()

        screen_right = screen.get_rect().right
        lasers = [
            laser
            for laser in lasers
            if laser.rect.left < screen_right
        ]

        lasers = check_laser_alien_collisions(lasers, aliens)

        screen.fill((20, 20, 40))
        ship.draw()

        for laser in lasers:
            laser.draw()

        for alien in aliens:
            alien.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()