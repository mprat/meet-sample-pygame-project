import pygame
import sys
import fruit
import button
import label

if __name__=="__main__":
    pygame.init()
    screen_size = 400
    main_screen = pygame.display.set_mode((screen_size, screen_size))
    main_screen.fill((255,255,255))

    b1 = button.BananaButton(0, 0, 40, 40, 'baby-bamba.jpg')
    b2 = button.AppleButton(100, 0, 40, 40)
    b1.draw(main_screen)
    b2.draw(main_screen)

    checkoutbtn = button.Button(300, 200, 50, 50)
    checkoutbtn.fill((255, 0, 0))
    checkoutbtn.draw(main_screen)

    donelabel = label.Label(30, 50, 300, 200, 30)
    donelabel.draw("no checkout", main_screen)

    newbtn = button.Button(200, 0, 40, 40)

    checkout = []
    numapples = 0
    numbananas = 0

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if b1.rec.collidepoint(x, y):
                numapples += 1
                checkout.append(fruit.Fruit("Apple", 5))
                b1.click(main_screen, numapples)
            if b2.rec.collidepoint(x, y):
                numbananas += 1
                checkout.append(fruit.Fruit("Banana", 10))
                b2.click(main_screen, numbananas)
            if checkoutbtn.rec.collidepoint(x, y):
                donelabel.draw(str(numapples) + " apples and " + str(numbananas) + " bananas", main_screen)
        pygame.display.flip()
 
	# pygame.quit()