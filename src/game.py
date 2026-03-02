"""
game.py was created by Jamie at the beginning of the project.
It holds the Game class which is where the main game loop is defined,
and the game is created.
"""
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FRAMERATE
from src.components.player import Player
from src.components.tiles import TestTile
from src.components.levelhandler import parse_level, load_level
from src.components.player import Player
from src.components.ui import Button

class Game:
    """
    The Game class is the class that holds the game's logic and functionality.
    """
    def __init__(self):
        """
        The init function sets up the game with all of the variables it needs.
        These variables include:
            - self.screen = The screen that is rendered.
            - self.framerate = The framerate that the game runs at.
            - self.clock = The clock that is used for all physics and movement.
            - self.state = The state the game is in.

        Implemented by Jamie
        """
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
        pygame.display.set_caption("Test Caption")

        self.framerate = FRAMERATE
        self.clock = pygame.time.Clock()
        self.delta_time = 0.1
        self.running = True
        self.state = "MAIN_MENU"
        
        self.render_layer = pygame.sprite.Group()
        self.update_layer = pygame.sprite.Group()
        self.tile_layer = pygame.sprite.Group()

        self.load_new_level(1)
        self.test_player = Player(0,0)
        self.render_layer.add(self.test_player)
        self.update_layer.add(self.test_player)
        self.test_player.tile_sprites = self.tile_layer
        self.test_player.check_collision(self.tile_layer)

        self.play_button = Button((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), 100, 50, "Play")

    def tick(self):
        """
        The tick function is called every frame and it calculates the delta_time
        based off of the clock. This allows for smoother movement when stuttering.

        Implemented by Jamie
        """
        self.delta_time = self.clock.tick() / 1000
        self.delta_time = min(0.1, max(self.delta_time, 0.001))

    def load_new_level(self, level_num):
        self.render_layer.empty()
        self.update_layer.empty()
        level_data = parse_level(f"assets/levels/level{level_num}.txt")
        self.level = load_level(level_data, self)

    def main(self):
        """
        The main function is where the main game loop is.
        
        Implemented by Jamie
        """
        while self.running:
            self.tick()

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.is_clicked(mouse_pos):
                        self.state = "PLAYING"

            self.update_layer.update()

            match self.state:
                case "MAIN_MENU":
                    self.screen.fill((200,200,200))
                    self.play_button.draw(self.screen)

                    mouse_pos = pygame.mouse.get_pos()
                    
                    self.play_button.is_hovered(mouse_pos)

                case "PLAYING":
                    self.screen.fill((255,255,255))

                    try:
                        self.render_layer.draw(self.screen)
                    except Exception as e:
                        print (e)


            pygame.display.flip()
                

        
        pygame.quit()
