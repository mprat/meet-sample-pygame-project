import pygame
import fruit
import label

class Button(pygame.Surface):
    def __init__(self, x_corner, y_corner, x, y, text="", img_filename=""):
        pygame.Surface.__init__(self, size=(x, y))
        self.rec = pygame.Rect(x_corner, y_corner, x, y)
        self.img = ""
        self.text = ""
        self.x_corner = x_corner
        self.y_corner = y_corner
        self.x = x
        self.y = y
        if img_filename:
            self.img = pygame.image.load(img_filename)
        if text: 
            self.text = text

    def draw(self, screen):
        if self.img: 
            screen.blit(self.img, self.rec)
        else: 
            # screen.blit(self, self.rec)

            if self.text: 
                l = label.Label(30, self.x_corner, self.y_corner, self.x, self.y)
                l.draw(self.text, screen)
            else: 
                screen.blit(self, self.rec)

    def click(self):
        print "button clicked"

class AppleButton(Button):
    def click(self, screen, num):
        l = label.Label(30, 50, 50, 200, 30)
        l.draw("Apples: " + str(num), screen)


class BananaButton(Button):
    def click(self, screen, num):
        l = label.Label(30, 50, 100, 200, 30)
        l.draw("Bananas: " + str(num), screen)