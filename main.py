import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)  # Gray for the display
BUTTON_COLORS = {
    "7": (255, 0, 0),  # Red
    "8": (0, 255, 0),  # Green
    "9": (0, 0, 255),  # Blue
    "/": (255, 128, 0),  # Yellow
    "4": (255, 165, 0),  # Orange
    "5": (75, 0, 130),  # Indigo
    "6": (238, 130, 238),  # Violet
    "*": (0, 255, 255),  # Cyan
    "1": (255, 192, 203),  # Pink
    "2": (128, 0, 128),  # Purple
    "3": (255, 55, 55),  # White
    "-": (128, 128, 0),  # Olive
    "0": (0, 128, 0),  # Dark Green
    "C": (255, 0, 255),  # Magenta
    "=": (0, 0, 0),  # Black
    "+": (192, 192, 192),  # Light Gray
}

# Font
font = pygame.font.Font(None, 36)

# Calculator variables
input_str = ""


def draw_buttons():
    buttons = [
        ("7", 50, 150),
        ("8", 150, 150),
        ("9", 250, 150),
        ("/", 350, 150),
        ("4", 50, 250),
        ("5", 150, 250),
        ("6", 250, 250),
        ("*", 350, 250),
        ("1", 50, 350),
        ("2", 150, 350),
        ("3", 250, 350),
        ("-", 350, 350),
        ("0", 50, 450),
        ("C", 150, 450),
        ("=", 250, 450),
        ("+", 350, 450),
    ]
    for text, x, y in buttons:
        pygame.draw.rect(
            screen, BUTTON_COLORS[text], (x, y, 80, 80), border_radius=10
        )  # Rounded buttons
        label = font.render(text, True, WHITE)  # White text on buttons
        screen.blit(label, (x + 30, y + 20))


def calculate(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"


# Main loop
while True:
    screen.fill(WHITE)  # Fill the background with white

    # Display area
    pygame.draw.rect(
        screen, GRAY, (50, 50, 400, 80), border_radius=10
    )  # Gray display background
    input_label = font.render(input_str, True, BLACK)  # Black text for input
    screen.blit(input_label, (60, 60))  # Display current input

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() or event.unicode in "+-*/":
                input_str += event.unicode
            elif event.unicode == "C":
                input_str = ""
            elif event.unicode == "=":
                input_str = calculate(input_str)

    pygame.display.update()  # Update the display
