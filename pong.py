import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Pong')

# Paddle settings
paddle_width = 15
paddle_height = 90
player_paddle_x = 50
opponent_paddle_x = screen_width - 50 - paddle_width
paddle_y = (screen_height / 2) - (paddle_height / 2)
paddle_speed = 7

# Ball settings
ball_width = 15
ball_height = 15
ball_x = (screen_width / 2) - (ball_width / 2)
ball_y = (screen_height / 2) - (ball_height / 2)
ball_x_speed = 5 * random.choice((1, -1))
ball_y_speed = 5 * random.choice((1, -1))

# Game loop control
running = True
clock = pygame.time.Clock()

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_y < screen_height - paddle_height:
        paddle_y += paddle_speed
    
    # Ball movement
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    
    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y + ball_height >= screen_height:
        ball_y_speed *= -1
    
    # Ball collision with paddles
    if (ball_x <= player_paddle_x + paddle_width and player_paddle_x <= ball_x and paddle_y < ball_y + ball_height and paddle_y + paddle_height > ball_y) or \
       (ball_x + ball_width >= opponent_paddle_x and opponent_paddle_x + paddle_width >= ball_x + ball_width and paddle_y < ball_y + ball_height and paddle_y + paddle_height > ball_y):
        ball_x_speed *= -1
    
    # Reset ball position if out of bounds
    if ball_x < 0 or ball_x > screen_width:
        ball_x = (screen_width / 2) - (ball_width / 2)
        ball_y = (screen_height / 2) - (ball_height / 2)
        ball_x_speed = 5 * random.choice((1, -1))
        ball_y_speed = 5 * random.choice((1, -1))
    
    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (opponent_paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_width, ball_height))
    pygame.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
