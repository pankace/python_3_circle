import pygame
import random
from typing import Self


def circle():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Circles")
    clock = pygame.time.Clock()
    running = True
    circles = []
    for _ in range(10):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        radius = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circles.append((x, y, radius, color))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for x, y, radius, color in circles:
            pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# animate the circles
def animate():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Circles")
    clock = pygame.time.Clock()
    running = True
    circles = []
    for _ in range(10):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        radius = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        circles.append((x, y, radius, color, dx, dy))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for i, (x, y, radius, color, dx, dy) in enumerate(circles):
            x += dx
            y += dy
            if x < 0 or x > 800:
                dx = -dx
            if y < 0 or y > 600:
                dy = -dy
            circles[i] = (x, y, radius, color, dx, dy)
            pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    animate()