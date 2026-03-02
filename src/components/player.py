# Created by William Nutter
# Player File
# Dedicated to Controls, Collision with Player, Lives
# 
# Movement Method - Handles Left/Right Movement and Up/Down Functuality

# Pygame Documentation used for Movement Notes: https://stackoverflow.com/questions/72041240/pygame-character-movement

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/player V1.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.lives = 5.0
        self.direction = -1
        self.speed = 10
        
    def Movement(self): # Handles Movement - Grabbing Key Pressed and having a corrosponding action
        keyPressed = pygame.event.get()
        leftPressed = keyPressed[pygame.K_a] or keyPressed[pygame.K_LEFT]
        rightPressed = keyPressed[pygame.K_d] or keyPressed[pygame.K_RIGHT]
        jumpPressed = keyPressed[pygame.K_w] or keyPressed[pygame.K_SPACE] or keyPressed[pygame.K_UP]

        if leftPressed:
            self.rect.x -= 5

        if rightPressed:
            self.rect.x += 5

        if jumpPressed:
            self.Jump()

    def Jump(self):
        self.player.rect.y += 5

    def update(self):
        self.Movememnt()
