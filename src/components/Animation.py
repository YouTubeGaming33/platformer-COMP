""" this file was made by oliver at 13:30 
it will allow animation that bobs the player when idle"""

import pygame

player1 = pygame.image.load("assets/sprites/player V1.png")
player2 = pygame.image.load("assets/sprites/player_2.png")

img_list = []

img_list.append (player1)
img_list.append (player2)

import pygame, sys, os
pygame.init()
# Window
window_size = (800,600)
game_window = pygame.display.set_mode(window_size)
# Sprite Class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# Sprite
sprite = MySprite(os.path.join('Assets', 'mysprite.png'), 50, 50)
# Clock
clock = pygame.time.Clock()
# Target Position
target_pos = [sprite.rect.x, sprite.rect.y]
# Game Loop
run = True
speed = 5
while run:
    clock.tick(60)  # Limit to 60 frames per second.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button.
                # Get mouse position.
                target_pos = list(pygame.mouse.get_pos())
    # Smooth Movement
    dx = target_pos[0] - sprite.rect.x
    dy = target_pos[1] - sprite.rect.y
    if abs(dx) > 3:
        sprite.rect.x += speed if dx > 0 else -speed
    if abs(dy) > 3:
        sprite.rect.y += speed if dy > 0 else -speed
    # Update Display
    game_window.fill((0,0,0))
    game_window.blit(sprite.image, sprite.rect)
    pygame.display.update()
# Quit Pygame
pygame.quit()