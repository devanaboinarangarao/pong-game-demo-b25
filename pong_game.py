import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball settings
BALL_SPEED = 5
BALL_RADIUS = 10

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball position and velocity
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Paddle positions
left_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or \
       (ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx, ball_dy = BALL_SPEED * random.choice([-1, 1]), BALL_SPEED * random.choice([-1, 1])

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()

# Additional comments added to explain the code:
# - The game loop handles events, updates positions, and redraws the screen.
# - Paddle movement is controlled by W/S keys for the left paddle and UP/DOWN keys for the right paddle.
# - Ball collisions with walls and paddles are detected and handled to reverse direction.
# - If the ball goes out of bounds, it resets to the center with a random direction.