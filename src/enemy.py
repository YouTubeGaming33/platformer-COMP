"""
enemy.py was created by oliver at 12.30.
It holds the enemy behaviour and traits.

"""
import pygame
from settings import TILE_HEIGHT, TILE_WIDTH

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed = None
        self.patrol_dist = None
        self.attack_cooldown = None

        self.collidable = False

class Cactus(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x,y, "CACTUS", "assets/WHERETHECATCUSIS")

        # CHANGE SPEED, PATROL DIST, ATTACK COOLDOWN, COLLIDABLE
        # DEPENDING ON THE CACTUS AND ADD METHODS FOR IT