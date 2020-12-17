import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),0,32)
image = pygame.image.load("c:\\project\\ballgame\\ball2.png")
ball_rect = image.get_rect()
ball_rect.center = (100,100)
yspeed = 1
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if ball_rect.bottom >= 500 or ball_rect.top <= 0:
        yspeed = -yspeed
    ball_rect.move_ip(0,yspeed)
    screen.fill((255,255,255))
    screen.blit(image,ball_rect)
    pygame.display.flip()

pygame.quit()