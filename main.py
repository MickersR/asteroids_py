# this allows us to use code from the open source pygame library throughout this file
import pygame
import sys

#import game consts 
from constants import *

#import player class
from player import *
from asteroid import *

#import Asteroid field logic
from asteroidfield import *

def main():
    pygame.init()

    frame_timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #instantiate objects and their containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroidfield1 = AsteroidField()


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
        for sprite in drawable:
            sprite.draw(screen)
        #Update
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print(f"Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()

        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
    main()