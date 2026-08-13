import Pygame
Pygame.init()

screen = Pygame.display.set_mode((400,500))
done = False

while not done:
    for event in Pygame.event.get():
        if event.type == Pygame.quit:
            Pygame.quit()

    Pygame.display.flip()