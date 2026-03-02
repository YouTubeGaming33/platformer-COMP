import pygame

pygame.font.init()

class Button:
    def __init__(self, x, y, width, height, text, color=(100,100,100), text_color = (255,255,255)):
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.centerx = x
        self.rect.centery = y

        self.x = x
        self.y = y

        self.text = text
        self.color = color
        self.text_color = text_color
        self.hovered = False
        self.font = pygame.font.Font(size=24)
    
    def draw(self, surface):
        color = (150,150,150) if self.hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (0,0,0), self.rect, 2)

        
        rendered_text = self.font.render(self.text, True, self.text_color)
        text_rect = rendered_text.get_rect()
        text_rect.centerx = self.x
        text_rect.centery = self.y
        
        surface.blit(rendered_text, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
        
    def is_hovered(self, pos):
        self.hovered = self.rect.collidepoint(pos)