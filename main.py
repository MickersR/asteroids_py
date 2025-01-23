# this allows us to use code from the open source pygame library throughout this file
import pygame

#import game consts 
from constants import *

#import player class
from player import *

def main():
    pygame.init()

    frame_timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #instantiate player object
    Player.containers = (updatable, drawable)
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    

    #main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill screen with black    
        screen.fill((0,0,0))
        #frame timer tick
        dt = (frame_timer.tick(60) / 1000)
        

        #Draw
        for PlayerClass in drawable:
            PlayerClass.draw(screen)
        #Update
        for PlayerClass in updatable:
            PlayerClass.update(dt)
        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
    main()