import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),0,32)
image1 = pygame.image.load("c:\\project\\ballgame\\ball2.png")
image2 = pygame.image.load('c:\\project\\ballgame\\boxbox2.png')
ball_rect = image1.get_rect()
rect_rect = image2.get_rect()
ball_rect.center = (100,100)
rect_rect.center = (145,71)
yspeed = 1

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    rectx,recty = pygame.mouse.get_pos()



    rect_rect.x = rectx
    rect_rect.y = 357


    if ball_rect.top <= 0 or ball_rect.bottom >= 500 or ball_rect.colliderect(rect_rect):

        yspeed = -yspeed
    ball_rect.move_ip(0,yspeed)
        
    screen.fill((255,255,255))
    screen.blit(image1,ball_rect)
    screen.blit(image2,rect_rect)
    pygame.display.flip()

pygame.quit()