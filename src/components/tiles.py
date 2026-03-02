import pygame
from settings import TILE_HEIGHT, TILE_WIDTH


class BaseTile(pygame.sprite.Sprite):
    """
    A Base tile that is used throughout the program.

    Implemented by Jamie
    """
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))

        self.x = x
        self.y = y

        self.collidable = True
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

class TestTile(BaseTile):
    """
    A Test tile for debugging.

    Implemented by Jamie
    """
    def __init__(self, x, y):
        super().__init__(x, y, "assets/sprites/placeholder tile.png")
        self.collidable = True
    
class SandTile(BaseTile):
    """
    A Sand Tile for the player to stand on.
    """
    def __init__(self, x, y):
        super().__init__(x,y, "assets/sprites/sand.png")
        self.collidable = True