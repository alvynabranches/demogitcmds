import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 700  # Increased dimensions
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)

# Calculator variables
input_str = ""

def draw_buttons():
    buttons = [
        ('7', 50, 150), ('8', 150, 150), ('9', 250, 150), ('/', 350, 150),
        ('4', 50, 250), ('5', 150, 250), ('6', 250, 250), ('*', 350, 250),
        ('1', 50, 350), ('2', 150, 350), ('3', 250, 350), ('-', 350, 350),
        ('0', 50, 450), ('C', 150, 450), ('=', 250, 450), ('+', 350, 450)
    ]
    for (text, x, y) in buttons:
        pygame.draw.rect(screen, GRAY, (x, y, 80, 80))
        label = font.render(text, True, BLACK)
        screen.blit(label, (x + 30, y + 20))

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"

# Main loop
while True:
    screen.fill(WHITE)
    draw_buttons()
    
    # Display current input
    input_label = font.render(input_str, True, BLACK)
    screen.blit(input_label, (50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() or event.unicode in "+-*/":
                input_str += event.unicode
            elif event.unicode == 'C':
                input_str = ""
            elif event.unicode == '=':
                input_str = calculate(input_str)

    pygame.display.update()  # Update the display