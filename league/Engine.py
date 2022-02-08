
import sys, pygame
from league import Scene
pygame.init()


#Temporary comments about default engine game code in this file were done by Gino 7FEB2022 circa 6p.m.

# tuple of w,h stored in size variable and initialized to 320w and 240h
size = width, height = 1024, 768

#Scene is imported from the class "Scene"
scene = Scene

visible_statistics = False
#speed is saved in the x and y direction in an array here
speed = [2, 2]

#rgb tuple stored references the color black
black = 0, 0, 0

#set the screen width and height
screen = pygame.display.set_mode(size)

#instantiate an object
ball = pygame.image.load("intro_ball.gif")

#sets the rectangular dimensions of the image in the object
ballrect = ball.get_rect()

#Main Game Loop loops until the quit event triggers closing of the program
while 1:
    #this is the main game loop which cycles through events in the queue (there are no native queues in python, so it's built on a list though--please correct me if I'm wrong --Gino)
    for event in pygame.event.get():
        #how to check for certain events, in this case we have QUIT
        if event.type == pygame.QUIT: sys.exit()

    #makes the ballrect object move
    ballrect = ballrect.move(speed)
    #reverses direction if it hits a wall kinematically by reversing the sign of x value stored in the 0th place of the array
    if ballrect.left < 0 or ballrect.right > width:

        speed[0] = -speed[0]
    #same but for top/bottom
    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]

    #colors the background black
    screen.fill(black)

    #worth reading this entry on what blit is, https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit

    #ball is the thing it is going to draw, here we have a reference to a .gif image and ballrect is where it is going to draw
    screen.blit(ball, ballrect)

    #commenting out to see what breaks---breaks everything... lol.
    #this "updates the full display Surface to the screen"--in other words it makes the engine go VROOOOM!! --G
    pygame.display.flip()