import random
from math import log2, ceil

import pygame


def sieve(N):
    i = 2
    is_prime = [1] * N
    is_prime[0] = 0
    is_prime[1] = 0

    while i * i <= N:
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2 * i
        while j < N:
            is_prime[j] = 0
            j += i

        i += 1
    return is_prime


windowWidth = 1920
windowHeight = 1080

pygame.init()
screen = pygame.display.set_mode([windowWidth, windowHeight], pygame.FULLSCREEN)
screen.fill([0, 0, 120])

is_prime = sieve(2 ** ceil(log2(max(windowHeight, windowWidth))))  # sieve size = max x|y in cycle

for y in range(1, windowHeight):
    for x in range(1, windowWidth):
        xored = x ^ y
        if is_prime[xored]:
            screen.set_at((x, y), [random.randint(70, 255), random.randint(70, 255), random.randint(70, 255)])

try:
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                break
        pygame.display.flip()
finally:
    pygame.quit()
