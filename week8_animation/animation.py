import pygame

pygame.init()
pygame.mixer.init()

m=pygame.mixer.Sound("c:\\project\\animation\\recycle.wav")
m.set_volume(0.70)

m2=pygame.mixer.Sound("c:\\project\\animation\\tada.wav")
m2.set_volume(0.80)

screen = pygame.display.set_mode([500,300])
pygame.display.set_caption("Turn off the switch!")
back = pygame.Surface(screen.get_size())
screen.fill([255,255,255])
Image = pygame.image.load('c://project//animation//cat.png')

pygame.draw.rect(screen,[0,0,0],[340,30,20,50],2)
pygame.draw.rect(screen,[0,0,0],[345,35,10,25],2)

pygame.draw.rect(screen,[128,0,0],[340,210,150,10],0)
pygame.draw.rect(screen,[128,0,0],[410,210,10,70],0)

x=50
y=220

screen.blit(Image, [x, y])
pygame.draw.rect(screen,[1,128,25],[50,260,150,30],0)
pygame.display.flip()

pygame.time.delay(1000)

for i in range(0,260):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    x+=1
    screen.blit(Image, [x, y])
    pygame.display.flip()
    pygame.time.delay(10)

pygame.time.delay(500)

for i in range(0,70):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    y-=1
    screen.blit(Image, [x, y])
    pygame.draw.rect(screen,[128,0,0],[340,210,150,10],0)
    pygame.display.flip()
    pygame.time.delay(2)

pygame.time.delay(1000)

for i in range(0,50):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    y-=1
    screen.blit(Image, [x, y])
    pygame.display.flip()
    pygame.time.delay(2)

for i in range(0,50):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    y+=1
    screen.blit(Image, [x, y])
    pygame.display.flip()
    pygame.time.delay(2)

pygame.time.delay(2000)

for i in range(0,250):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    x+=1
    screen.blit(Image, [x, y])
    pygame.display.flip()
    pygame.time.delay(8)

pygame.time.delay(2000)

for i in range(0,250):
    pygame.draw.rect(screen,[255,255,255],[x,y,250,150],0)
    screen.blit(Image, [x+150, y+70])
    x -= 1
    pygame.draw.rect(screen,[0,0,128],[x,y,150,150],0)
    pygame.time.delay(60)
    pygame.display.flip()
    m.play()

pygame.time.delay(500)

x += 150
y += 70

for i in range(0,130):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    y-=1

    screen.blit(Image,[x, y])
    pygame.display.flip()
    pygame.time.delay(20)

for i in range(0,150):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    x-=1

    screen.blit(Image,[x, y])
    pygame.display.flip()
    pygame.time.delay(5)

pygame.time.delay(800)

for i in range(0, 50):
    pygame.draw.rect(screen,[255,255,255],[x,y,100,60],0)
    y-=1

    screen.blit(Image,[x, y])
    pygame.display.flip()
    pygame.time.delay(1)

pygame.draw.rect(screen,[0,0,0],[0,0,500,300],0)
pygame.display.flip()

pygame.time.delay(3000)
font1 = pygame.font.Font("freesansbold.ttf",100)

title = font1.render('the end', True, [255,255,255],[0,0,0])

textRect = title.get_rect()

screen.blit(title,textRect)
pygame.display.flip()
m2.play()
    
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
    


















# x=50
# y=50
# for i in range(0,300):
#     if not x >= 400 or y >= 240:
#         pygame.draw.rect(screen, [255,255,255], [x,y,100,100],0)
#         pygame.display.flip()
#         screen.blit(Image,[x,y])
#         pygame.display.flip()
#         pygame.time.delay(20)
#         x += 3
#         y += 1






# screen.blit(Image, [x, y])
# pygame.display.flip()
# pygame.time.delay(50)
# pygame.draw.rect(screen,[255,255,255],[x,y,100,100],0)
# pygame.display.flip()
# pygame.time.delay(50)
# screen.blit(Image, [60,60])
# pygame.time.delay(50)
# pygame.display.flip()



# pygame.mixer.music.load("c:\\project\\animation\\ring2.wav")
# pygame.mixer.music.set_volume(0.50)
# pygame.mixer.music.play()

# m=pygame.mixer.Sound("c:\\project\\animation\\tada.wav")
# m.set_volume(0.30)
# m.play()
