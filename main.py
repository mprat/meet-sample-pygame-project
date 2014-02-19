import pygame
import sys
import fruit
import button

if __name__=="__main__":
    pygame.init()
    screen_size = 400
    main_screen = pygame.display.set_mode((screen_size, screen_size))
    main_screen.fill((255,255,255))
    label_rec = pygame.Rect(50, 50, 200, 30)
    orderlabel = pygame.font.Font(None, 30)

    b1 = button.BananaButton(0, 0, 40, 40, 'baby-bamba.jpg')
    b2 = button.AppleButton(100, 0, 40, 40)
    b1.draw(main_screen)
    b2.draw(main_screen)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if b1.rec.collidepoint(x, y):
                b1.click(main_screen)
            if b2.rec.collidepoint(x, y):
                b2.click(main_screen)
        pygame.display.flip()
 
	# pygame.quit()