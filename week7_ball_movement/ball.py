import pygame

pygame.init()
screen = pygame.display.set_mode((500,300), 0, 32)
pygame.display.set_caption("Noku game")

screen.fill((255,255,255))
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
ballx = 150
bally = 100

# pygame.init()
# screen = pygame.display.set_mode((700,600), 0, 32)
# pygame.display.set_caption("Noku game")
# screen.fill((0,0,0))
# for i in range(100):
#     width = random.randint(0,150)
#     height = random.randint(0,150)
#     left = random.randint(0,600)
#     top = random.randint(0,500)
#     rad = random.randint(10,50)
#     c1=random.randint(0,255)
#     c2=random.randint(0,255)
#     c3=random.randint(0,255)
#     line = c1=random.randint(0,5)
#     if i%2 == 0:
#         pygame.draw.rect(screen, [c1,c2,c3], [left, top, width, height],line)
#     else:
#         pygame.draw.circle(screen, [c1,c2,c3], [left, top], rad, line)

# pygame.display.flip()


# while 1:
#     ev = pygame.event.poll()
#     if ev == pygame.QUIT:
#         break

# pygame.quit()





# myballImage = pygame.image.load('c://project//ball//cat.png')
# rect = myballImage.get_rect()


# held = False
# done = False
# while not done:
#     for event in pygame.event.get ():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             held = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             held = False
#         elif event.type == pygame.MOUSEMOTION:
#             if held:
#                 rect.center = event.pos
#     screen.fill((255, 255, 255))
#     screen.blit(myballImage, rect)
#     pygame.display.flip()

# pygame.quit()


# pygame.draw.rect(screen, [128, 0, 0], [250, 150, 300, 100], 0)
# pygame.draw.circle(screen, [0, 255, 0], [100, 100], 50, 0)
# pygame.draw.line(screen, [125,125,0], [90,100], [270,270],10)
# pygame.draw.polygon(screen, [200,0,100], [(0,0),(300,50),(50,300),(400,400),(300,126)],10)

# cat = pygame.image.load('c://project//ball//cat.png')


# font_1 = pygame.font.Font('freesansbold.ttf', 100)
# title=font_1.render('world', True, GREEN, BLUE)
# textrect = title.get_rect()
# textrect.center=(200, 150)




ball = pygame.image.load('c://project//ball//cat.png')

done = False


while not done:
    for ev in pygame.event.get ():
        if ev.type == pygame.QUIT:
            done = True
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                if not ballx >= 400:
                    ballx += 5
            elif ev.key == pygame.K_LEFT:
                if not ballx <= 0:
                    ballx -= 5
            elif ev.key == pygame.K_UP:
                if not bally <= 0:
                    bally -= 5
            elif ev.key == pygame.K_DOWN:
                if not bally >= 240:
                    bally += 5
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))

    pygame.display.flip()



pygame.quit()







# while 1:
#     ev = pygame.event.poll()

#     if ev.type == pygame.QUIT:
#         break
#     # screen.blit(cat, (100,100))
#     # screen.blit(title,textrect)
#     pygame.display.flip()

# pygame.quit()


# input('Press RETURN to exit')