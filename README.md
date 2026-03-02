# platformer-COMP
Suedo

To Do:
- [ ] Tilemap.py
- [ ] Camrea.py
- [ ] player.py
- [ ] Watergun.py
- [ ] enimies.

import pygame
import random
class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'regen'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()

powerup_images = {}
powerup_images['shield'] = pygame.image.load('shieldGold.png').convert()
powerup_images['heart'] = pygame.image.load('heart.png').convert()

powerups = pygame.sprite.Group()


# check to see if player hit a powerup
hits = pygame.sprite.spritecollide(player, powerups, True)
for hit in hits:
    if hit.type == 'shield':
        player.shield += random.randrange(10, 30)
        if player.shield >= 100:
            player.shield = 100
    if hit.type == 'heart':
        pass

# Implemented by Josh



import pygame
# Bullet class for water pistol 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill() # add colour 
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

    for event in pygame.event.get():
    # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player.shoot()
                
    bullets = pygame.sprite.Group()


