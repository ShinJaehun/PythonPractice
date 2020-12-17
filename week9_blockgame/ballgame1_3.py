import pygame, random
pygame.init()
screen = pygame.display.set_mode((500,500),0,32)
image1 = pygame.image.load("c:\\project\\ballgame\\ball2.png")
image2 = pygame.image.load("c:\\project\\ballgame\\boxbox2.png")

ball_rect = image1.get_rect()
rect_rect = image2.get_rect()

x = random.randrange(0,291)
y = random.randrange(0,357)

rect_rect.x = x
rect_rect.y = y

ballx=0
bally=0

done = False

while done == False:
    for ev in pygame.event.get ():
        if ev.type == pygame.QUIT:
            done = True

        elif ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_RIGHT:
                if not ballx >= 400:
                    ballx += 20
            elif ev.key == pygame.K_LEFT:
                if not ballx <= 0:
                    ballx -= 20
            elif ev.key == pygame.K_UP:
                if not bally <= 0:
                    bally -= 20
            elif ev.key == pygame.K_DOWN:
                if not bally >= 400:
                    bally += 20

            ball_rect.x = ballx
            ball_rect.y = bally

            if rect_rect.colliderect(ball_rect):
                print ('충돌!')

                print("x = " + str(x))
                print("y = " + str(y))
                print("ballx = " + str(ballx))
                print("bally = " + str(bally))
                print("rect_rect x = " + str(rect_rect.x))
                print("rect_rect y = " + str(rect_rect.y))
                print("ball_rect x = " + str(ball_rect.x))
                print("ball_rect y = " + str(ball_rect.y))

                pygame.draw.rect(screen,[255,255,255],[x,y,291,143],0)
                
                x = random.randrange(0,291)
                y = random.randrange(0,357)
                rect_rect.x = x
                rect_rect.y = y

    screen.fill((255,255,255))
    screen.blit(image1, (ballx, bally))
    screen.blit(image2, (x, y))

    pygame.display.flip()

pygame.quit()