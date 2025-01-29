# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Shot.containers = (shot, updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        updatable.update(dt)
        for obj in asteroid:
            for shot_obj in shot:
                if obj.collides(shot_obj):
                    obj.split()
                    shot_obj.kill()
        for obj in asteroid:
            if player1.collides(obj):
                print("Game over!")
                running = False
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0



if __name__ == "__main__":
    main()
