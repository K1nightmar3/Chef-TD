# Example file showing a basic pygame "game loop"
import pygame
from Button import Button
# pygame setup
pygame.init()
# Width and Height
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TD Game")
pygame.init()
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
def get_font(size):
    return pygame.font.Font('freesansbold.ttf', size)
# insert_image=pygame.image.load(os.path.join())
def drawMenu_window():
    # location of mouse

    MenuMousePOS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("Gourmand", True, "#FFA500")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    screen.blit(MENU_TEXT, MENU_RECT)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Black")
    # RENDER YOUR GAME HERE
    # This is to add text or images
    # screen.blit()
    drawMenu_window()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit()

