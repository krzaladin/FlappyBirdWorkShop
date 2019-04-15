#we first import pygame library
import pygame

#initialize pygame
pygame.init()

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (135, 206, 250)

#define screen size
size = (500, 700)
screen = pygame.display.set_mode(size)

#define screen title
pygame.display.set_caption("Flappy Bird")

#boolean T/F to control game logic
done = False
#clock to control game refresh speed
clock = pygame.time.Clock()

x = 350
y = 250



#define global variables to control speed
x_speed = 0
y_speed = 0

#define function to draw circle
def ball(x,y):
    pygame.draw.circle(screen,black,(x,y),20)

#while logic to keep game running
while not done:
    #capture input events so we can act upon them
    for event in pygame.event.get():
        #if user select 'ESC' key or press windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
        #new if event catch
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5
   
    #fill screen with color defined above
    screen.fill(blue)
    #call function to draw the ball
    ball(x,y)
    #adjust vertical y position
    y += y_speed
    
    #refresh screen by flipping like a flipbook new animation
    pygame.display.flip()
    #refresh times per second this will happen via clock defined above
    clock.tick(60)


#once logic loop end exit game
pygame.quit()