import sys
import pygame as py
import configs

py.init()

money = 0
money_counter_font = py.font.SysFont(None, 55)

# Load the static background image and define the base fill colour
background_image = py.image.load('background.bmp')
tree_img = py.image.load('tree-fix.bmp')
parliment_button = py.image.load('parliment.bmp')
coal_plant = py.image.load('coal.bmp')

TRANSPARENT_COLOUR = (0, 0, 0)
tree_img.set_colorkey(TRANSPARENT_COLOUR)
parliment_button.set_colorkey(TRANSPARENT_COLOUR)
# Scale the tree down to 30% so its smaller (Why did this say 0?)
tree_scale = 0.3
tree_img = py.transform.scale(
    tree_img,
    (int(tree_img.get_width() * tree_scale), int(tree_img.get_height() * tree_scale)),
)
parliment_scale = 0.3
parliment_button = py.transform.scale(
    parliment_button,
    (int(parliment_button.get_width() * parliment_scale), int(parliment_button.get_height() * parliment_scale)),
)
background_colour = (255,255,255)

# Read screen dimensions from configs so they can be tweaked in one place
(width, height) = (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)

# Create the window, set its title, then paint the background + image
screen = py.display.set_mode((width, height))
py.display.set_caption('ENDBRINGER.exe')

tree_x = width - 529
tree_y = 50

parliment_x = width - 1000
parliment_y = 500

#building button
coal_scale = 0.5
coal_button_img = py.transform.scale(
    coal_plant,
    (int(coal_plant.get_width() * coal_scale), int(coal_plant.get_height() * coal_scale)),
)
coal_button_img.set_colorkey(TRANSPARENT_COLOUR)
coal_button_rect = coal_button_img.get_rect(topleft=(5, 100))

tree_button_rect = tree_img.get_rect(topleft=(tree_x, tree_y))
parliment_button_rect = parliment_button.get_rect(topleft=(parliment_x, parliment_y))
coal_plant_rect = coal_plant.get_rect(topleft=(width - 800, 300))
running = True

# Menu graphics
menu_open = False
menu = py.Rect((width // 4, height // 4, width // 2, height // 2))
menu_close_button = py.Rect(menu.right - 120, menu.bottom - 60, 100, 40)

# Handler for inputs
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

            # Handler for mouse button down events
            # Use this to handler clicks by checking the coordinantes here
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                # Menu subsection for inputs
                if menu_open:
                    if menu_close_button.collidepoint(event.pos):
                        menu_open = False

                if tree_button_rect.collidepoint(event.pos):
                    money += 1

                if parliment_button_rect.collidepoint(event.pos):
                    menu_open = True

                if coal_button_rect.collidepoint(event.pos):
                    pass
        
    screen.fill(background_colour)

    screen.blit(background_image, (width -679, 0))

    screen.blit(tree_img, tree_button_rect)

    screen.blit(parliment_button, parliment_button_rect)

    screen.blit(coal_button_img, coal_button_rect)

    py.draw.line(screen, (0, 0, 0), (width // 3.1, 0), (width // 3.1, height), 20)

    money_counter = money_counter_font.render(f"Money: {money}", True, (0, 0, 0))
    screen.blit(money_counter, (20, 50))

    if menu_open:
        py.draw.rect(screen, (255, 255, 255), menu)
        py.draw.rect(screen, (0, 0, 0), menu, 5)

        menu_title = money_counter_font.render("Parliment", True, (0, 0, 0))
        screen.blit(menu_title, (menu.x + 20, menu.y + 20))

        py.draw.rect(screen, (255, 100, 100), menu_close_button)
        py.draw.rect(screen, (0, 0, 0), menu_close_button, 2)

    py.display.flip()

py.quit()
sys.exit()