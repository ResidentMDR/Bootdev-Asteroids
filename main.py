import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    main_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_1 = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        # clear the board
        screen.fill("black")

        # update game objects
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for updatable_object in updatable:    
            updatable_object.update(dt)
        for asteroid in asteroids:
            if (asteroid.collides_with(main_player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if (asteroid.collides_with(shot)):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # render the game 
        pygame.display.flip()



if __name__ == "__main__":
    main()