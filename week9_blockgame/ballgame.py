import pygame,random

pygame.init()
pygame.mixer.init()
m=pygame.mixer.Sound("c:\\project\\ballgame\\tada.wav")
m.set_volume(0.90)
m2=pygame.mixer.Sound("c:\\project\\ballgame\\Windows Pop-up Blocked.wav")
m2.set_volume(0.90)
screen = pygame.display.set_mode((500,500),0,32)
image1 = pygame.image.load("c:\\project\\ballgame\\ball.png")
image2 = pygame.image.load('c:\\project\\ballgame\\boxbox.png')
image3 = pygame.image.load("c:\\project\\ballgame\\bboxx.png")
ball_rect = image1.get_rect()
rect_rect = image2.get_rect()

Rectt1 = image3.get_rect()
Rectt1.center = (40,20)
Rectt1.x = random.randrange(0,460)
Rectt1.y = random.randrange(0,200)
Rectt2 = image3.get_rect()
Rectt2.center = (40,20)
Rectt2.y = random.randrange(0,200)
Rectt2.x = random.randrange(0,460)
Rectt3 = image3.get_rect()
Rectt3.center = (40,20)
Rectt3.x = random.randrange(0,460)
Rectt3.y = random.randrange(0,200)
Rectt4 = image3.get_rect()
Rectt4.center = (40,20)
Rectt4.x = random.randrange(0,460)
Rectt4.y = random.randrange(0,200)
Rectt5 = image3.get_rect()
Rectt5.center = (40,20)
Rectt5.x = random.randrange(0,460)
Rectt5.y = random.randrange(0,200)
Rectt6 = image3.get_rect()
Rectt6.center = (40,20)
Rectt6.x = random.randrange(0,460)
Rectt6.y = random.randrange(0,200)
Rectt7 = image3.get_rect()
Rectt7.center = (40,20)
Rectt7.x = random.randrange(0,460)
Rectt7.y = random.randrange(0,200)
Rectt8 = image3.get_rect()
Rectt8.center = (40,20)
Rectt8.x = random.randrange(0,460)
Rectt8.y = random.randrange(0,200)
ball_rect.center = (20,20)
rect_rect.center = (10,50)
yspeed = 1
xspeed = 1

d1 = False
d2 = False
d3 = False
d4 = False
d5 = False
d6 = False
d7 = False
d8 = False
done = False
total = 8

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    rectx,recty = pygame.mouse.get_pos()



    rect_rect.x = rectx
    rect_rect.y = 480

    if ball_rect.top <= 0 or ball_rect.colliderect(rect_rect):
        yspeed = -yspeed
        xspeed = random.randrange(1,5)
        
    ball_rect.move_ip(xspeed,yspeed)
    if ball_rect.left <= 0 or ball_rect.right >= 500:
        xspeed = -xspeed
        
    if ball_rect.bottom >= 500:
        done = True
    
    if ball_rect.colliderect(Rectt1) or ball_rect.colliderect(Rectt2) or ball_rect.colliderect(Rectt3) or ball_rect.colliderect(Rectt4) or ball_rect.colliderect(Rectt5) or ball_rect.colliderect(Rectt6) or ball_rect.colliderect(Rectt7) or ball_rect.colliderect(Rectt8) :
        m2.play()
        if ball_rect.colliderect(Rectt1):
            d1=True
            Rectt1.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt2):
            d2=True
            Rectt2.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt3):
            d3=True
            Rectt3.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt4):
            d4=True
            Rectt4.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt5):
            d5=True
            Rectt5.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt6):
            d6=True
            Rectt6.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt7):
            d7=True
            Rectt7.y=-40
            total = total-1
        elif ball_rect.colliderect(Rectt8):
            d8=True
            Rectt8.y=-40
            total = total-1
        xspeed = -xspeed
        yspeed = -yspeed
    screen.fill((255,255,255))
    
    screen.blit(image1,ball_rect)
    screen.blit(image2,rect_rect)
    if d1 == False:
        screen.blit(image3,Rectt1)
    if d2 == False:
        screen.blit(image3,Rectt2)
    if d3 == False:
        screen.blit(image3,Rectt3)
    if d4 == False:
        screen.blit(image3,Rectt4)
    if d5 == False:
        screen.blit(image3,Rectt5)
    if d6 == False:
        screen.blit(image3,Rectt6)
    if d7 == False:
        screen.blit(image3,Rectt7)
    if d8 == False:
        screen.blit(image3,Rectt8)
    pygame.display.flip()
    if total <= 0:
        print('You win!!!')
        m.play()
        pygame.time.delay(1000)
        done = True
    pygame.time.delay(5)

pygame.quit()
