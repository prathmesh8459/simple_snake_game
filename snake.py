import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors (RGB)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake setup
snake = [(100, 100)]  # Snake starts with one block
snake_dir = (CELL_SIZE, 0)  # Initial direction: right
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # Random food position
score = 0

# Font for score display
font = pygame.font.SysFont("Arial", 25)

# Game clock (FPS)
clock = pygame.time.Clock()

def draw_snake(snake):
    """Draw each block of the snake."""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    """Draw the food."""
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    """Display the score on the screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score = score_text
    screen.blit(score_text, [10, 10])

# Game loop
running = True
while running:
    clock.tick(8)  # Control speed (10 frames per second)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keypresses for direction change
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Move the snake by adding new head
    head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, head)

    # Check for food collision
    if head == food:
        score += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake.pop()  # Remove tail unless food is eaten

    # Check for wall collision or self collision
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        running = False  # Game over

    # Drawing
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    show_score(score)
    pygame.display.flip()

pygame.quit()
sys.exit()
