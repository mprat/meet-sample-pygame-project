import pygame
import fruit
import label

class Button(pygame.Surface):
    def __init__(self, x_corner, y_corner, x, y, img_filename=""):
        pygame.Surface.__init__(self, size=(x, y))
        self.rec = pygame.Rect(x_corner, y_corner, x, y)
        self.img = ""
        if img_filename:
            self.img = pygame.image.load(img_filename)

    def draw(self, screen):
        if self.img: 
            screen.blit(self.img, self.rec)
        else: 
            screen.blit(self, self.rec)

    def click(self):
        print "button clicked"

class AppleButton(Button):
    def click(self, screen):
        a = fruit.Fruit("Apple", 5)
        l = label.Label(30, 50, 50, 200, 30)
        l.draw(str(a) + "      ", screen)


class BananaButton(Button):
    def click(self, screen):
        a = fruit.Fruit("Banana", 10)
        l = label.Label(30, 50, 50, 200, 30)
        l.draw(str(a), screen)