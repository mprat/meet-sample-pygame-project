import pygame

class Label(pygame.font.Font):
    def __init__(self, size, x_corner, y_corner, x, y):
        pygame.font.Font.__init__(self, None, size)
        self.rec = pygame.Rect(x_corner, y_corner, x, y)
        self.textcolor = (0, 0, 0)
        self.background = (255, 255, 255)

    def draw(self, text, screen):
        label = self.render(text, 1, self.textcolor, self.background)
        screen.blit(label, self.rec)