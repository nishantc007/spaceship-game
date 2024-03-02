import pygame, random
pygame.init()

screen_width = 1280
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("bg.jpg").convert_alpha()
spaceship_image = pygame.image.load("Spaceship-2.png").convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image,(100,100))
spaceship_image = pygame.transform.rotate(spaceship_image,-90)
position_spaceship_x = 200
position_spaceship_y = 300

missile_image = pygame.image.load("missile.png").convert_alpha()
missile_image = pygame.transform.scale(missile_image,(100,100))
position_missile_x = 200
position_missile_y = 300
missile_speed = 0
triggered = False

alien_image = pygame.image.load("alien.png").convert_alpha()
alien_image = pygame.transform.scale(alien_image,(100,100))
position_alien_x = 800
position_alien_y = 300

spaceship_rectangle = spaceship_image.get_rect()
missile_rectangle = missile_image.get_rect()
alien_rectangle = alien_image.get_rect()
user_points = 20
font = pygame.font.SysFont("font/PixelGameFont.fft",50)
def respawn():
    x_pos = 1400
    y_pos = random.randint(100,600)
    return [x_pos,y_pos]

def missile_respawn():
    triggered = False
    missile_speed = 0
    position_missile_x = position_spaceship_x
    position_missile_y = position_spaceship_y
    return[triggered,missile_speed,position_missile_x,position_missile_y] 

def collisions():
    global user_points
    if spaceship_rectangle.colliderect(alien_rectangle) :
        user_points = user_points - 1
        return True
    elif missile_rectangle.colliderect(alien_rectangle):
        user_points = user_points + 1 
        return True
    else:
        return False
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(background,(0,0))

    relative_x = screen_width % background.get_rect().width
    screen.blit(background,(relative_x - background.get_rect().width,0))
    if relative_x < 1280:
        screen.blit(background,(relative_x,0))

    spaceship_rectangle.x = position_spaceship_x
    spaceship_rectangle.y = position_spaceship_y 
    missile_rectangle.x = position_missile_x
    missile_rectangle.y = position_missile_y

    screen_width = screen_width - 1

    position_alien_x = position_alien_x - 2

    position_missile_x = position_missile_x + missile_speed

   
    # pygame.draw.rect(screen,"red",spaceship_rectangle,3)
    # pygame.draw.rect(screen, "red", missile_rectangle,3 )

    score = font.render(f' Points: {int(user_points)}',True,"red")
  
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and position_spaceship_y > -25:
        position_spaceship_y = position_spaceship_y - 1
        if not triggered:
            position_missile_y = position_missile_y - 1

    if key[pygame.K_DOWN] and position_spaceship_y < 580:
        position_spaceship_y = position_spaceship_y + 1
        if not triggered: 
            position_missile_y = position_missile_y + 1

    if key[pygame.K_SPACE]:
        missile_speed = 10
        triggered = True

    if position_missile_x > 1300:
        triggered,missile_speed,position_missile_x,position_missile_y = missile_respawn()

    if position_alien_x <= -100 or collisions(): 
        position_alien_x = respawn()[0]
        position_alien_y = respawn()[1]
        # user_points = user_points - 1
    if user_points == 0:
        run = False

    screen.blit(missile_image,(position_missile_x,position_missile_y))
    screen.blit(spaceship_image,(position_spaceship_x,position_spaceship_y))
    screen.blit(alien_image,(position_alien_x,position_alien_y))
    screen.blit(score,(0,0))


    pygame.display.update()

    

pygame.quit()