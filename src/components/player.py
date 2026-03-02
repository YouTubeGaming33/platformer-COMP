# Created by William Nutter
# Player File
# Dedicated to Controls, Collision with Player, Lives
# 
# Movement Method - Handles Left/Right Movement and Up/Down Functuality

# Pygame Documentation used for Movement Notes: https://stackoverflow.com/questions/72041240/pygame-character-movement

import pygame
from settings import TERMINAL_VELOCITY, SCREEN_HEIGHT, GRAVITY, TILE_WIDTH, TILE_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/player V1.png")
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.lives = 5.0
        self.direction = -1
        self.speed = 1
        self.tile_sprites = None
        
    def Movement(self, dx): # Handles Movement - Grabbing Key Pressed and having a corrosponding action
        keyPressed = pygame.key.get_pressed()
        leftPressed = keyPressed[pygame.K_a] or keyPressed[pygame.K_LEFT]
        rightPressed = keyPressed[pygame.K_d] or keyPressed[pygame.K_RIGHT]
        jumpPressed = keyPressed[pygame.K_w] or keyPressed[pygame.K_SPACE] or keyPressed[pygame.K_UP]

        if leftPressed:
            dx -= self.speed
            self.facing = -1

        if rightPressed:
            dx += self.speed
            self.facing = 1

        if jumpPressed:
            self.Jump()

        return dx

    def Jump(self):
        self.y += GRAVITY

        if self.y > TERMINAL_VELOCITY:
            self.y = TERMINAL_VELOCITY

        return self.y
    
    def update_position(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if self.y > 0 and self.rect.bottom <= obstacle.rect.centery:
                    self.rect.bottom = obstacle.rect.top
                    self.vel_y = 0
                elif self.y < 0:
                    self.rect.top = obstacle.rect.bottom
                    self.y = 0
                else:
                    if self.rect.centerx < obstacle.rect.centerx:
                        self.rect.right = obstacle.rect.left
                    else:
                        self.left = obstacle.rect.right 

    def gravity(self):

        self.y += GRAVITY

        if self.y > TERMINAL_VELOCITY:
            self.y = TERMINAL_VELOCITY

        return self.y

    def update(self):
        dx = 0
        dx = self.Movement(dx)

        self.gravity()
        dy = self.y

        self.update_position(dx, dy)
        if self.tile_sprites is not None:
            self.check_collision(self.tile_sprites)

    def draw(self, surface):
        surface.blit(self.image, self.rect)