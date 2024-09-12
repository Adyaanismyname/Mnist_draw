import pygame
import tensorflow as tf
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
BLOCK_SIZE = 20  # Size of each block
BOARD_SIZE = 28   # Number of blocks in each row and column
SCREEN_SIZE = BLOCK_SIZE * BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_HEIGHT = 40
BUTTON_COLOR = (100, 100, 100)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_HOVER_COLOR = (150, 150, 150)

# Create the screen with extra space for the button
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + BUTTON_HEIGHT))
pygame.display.set_caption('28x2ter8 Drawable Board')

# Create a 2D list to keep track of the colors of the blocks
board = [[BLACK for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Font for the button text
font = pygame.font.Font(None, 36)

# Function to draw the "Predict" button
def draw_button(screen, button_rect, is_hovered):
    color = BUTTON_HOVER_COLOR if is_hovered else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)
    text_surface = font.render("Predict", True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

def draw_clear(screen , button_rect , is_hovered):
    color = BUTTON_HOVER_COLOR if is_hovered else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)
    text_surface = font.render("Clear", True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    predict_button_rect = pygame.Rect(0, SCREEN_SIZE, SCREEN_SIZE/2, BUTTON_HEIGHT)
    clear_button_rect = pygame.Rect(SCREEN_SIZE/2, SCREEN_SIZE, SCREEN_SIZE/2, BUTTON_HEIGHT)

    is_predict_button_hovered = predict_button_rect.collidepoint(mouse_x, mouse_y)
    is_clear_button_hovered = clear_button_rect.collidepoint(mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and is_predict_button_hovered:  # Left click on the button
                # Implement your prediction logic here
                # For now, it just saves the board as a PNG
                export_surface = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
                for row in range(BOARD_SIZE):
                    for col in range(BOARD_SIZE):
                        color = board[row][col]
                        export_surface.set_at((col, row), color)

                pygame.image.save(export_surface, "board_export.png")


                image = tf.keras.preprocessing.image.load_img('/Users/adyaanahmed/Documents/mnist_training+game/board_export.png', color_mode = 'grayscale' , target_size = (28 , 28))
                array = tf.keras.preprocessing.image.img_to_array(image)
                array = array / 255
                array = np.array(array).reshape(-1 , 28 , 28)

                model = tf.keras.models.load_model('/Users/adyaanahmed/Documents/mnist_training+game/mnist_model.h5')
                array_pred = model.predict(array)

                prediction = np.argmax(array_pred , axis = 1)
                print(prediction)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and is_clear_button_hovered:
                # Clear the board
                board = [[BLACK for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]



    # Handle drawing when the mouse is pressed and dragged
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # Left mouse button is held down
        col = mouse_x // BLOCK_SIZE
        row = mouse_y // BLOCK_SIZE
        if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
            board[row][col] = WHITE

    # Draw the grid
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, board[row][col], rect)

    # Draw the "Predict" button
    draw_button(screen, predict_button_rect, is_predict_button_hovered)
    draw_clear(screen, clear_button_rect, is_clear_button_hovered)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
