import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (25, 90, 25)
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 0.7

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Initialize ball position and velocity
ball_x = WIDTH // 3
ball_y = HEIGHT // 3
ball_x_speed = 0.1
ball_y_speed = 0.1

# Initialize paddle positions
left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 3
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 3

# Initialize a font for displaying text
font = pygame.font.Font(None, 36)

# Initialize a variable to track the game state
game_over = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        # Check for a key press to restart the game
        if keys[pygame.K_r]:
            game_over = False
            # Reset the game variables here (ball position, paddle positions, etc.)
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_x_speed = 0.1
            ball_y_speed = 0.1
            left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 1
            right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 1
        else:
            continue  # Skip updating and drawing the game if it's in the "Game Over" state and the "R" key is not pressed

    if keys[pygame.K_w]:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        right_paddle_y += PADDLE_SPEED

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Ball collisions
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_y_speed = -ball_y_speed

    if ball_x <= PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_x_speed = -ball_x_speed

    if ball_x >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_x_speed = -ball_x_speed

    # Ball out of bounds (scoring)
    if ball_x <= 0:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_x_speed = 5
        game_over = True  # Set the game state to "Game Over"

    if ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_x_speed = -5
        game_over = True  # Set the game state to "Game Over"

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
   
    # Display "Game Over" message if the game is over
    if game_over:
        text = font.render("Game Over. Press 'R' to restart.", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.update()

