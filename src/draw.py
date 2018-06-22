import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(6*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    player = PlayerBlock(Vector2(200, 100), 200, 50, [0,255,0])
    print(Vector2(200,100))
    object_list.append(player)

    block = KineticBlock(Vector2(300,200), 100, 100, [0, 0, 255])
    object_list.append(block)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    debug_create_objects(object_list)
    print("OBJECT LIST:", object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            object_list[1].moveLeft(5)
            object_list[1]
            object.update()
            object_list[1].draw(screen, pygame)
            print(object_list[1].position)
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            object_list[1].moveRight(50)
            pass

        for object in object_list:
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            # print("BALL IN OBJ LIST: ", ball)
            object_list[1].draw(screen, pygame)
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
