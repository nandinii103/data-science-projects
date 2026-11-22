import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Project")

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player = pygame.Rect(100, 100, player_size, player_size)

# Enemies
enemy_size = 50
enemies = []

for _ in range(7):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT - enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

# Score
score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
running = True

# Game loop
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player inside screen
    player.x = max(0, min(player.x, WIDTH - player_size))
    player.y = max(0, min(player.y, HEIGHT - player_size))

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, WIDTH - enemy_size)
            enemy.y = random.randint(0, HEIGHT - enemy_size)

    # Draw everything
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
