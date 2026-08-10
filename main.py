# how to update
# 0) save the files normally in the editor tab
# 1) git add .
# 2) git commit -m "put update notes here"
# 3) git push
# pull if it tells you to its just git pull
import sys
import pygame as py
import configs
import random

py.init()

paused = False
money = 1
coal = 0
oil = 0
middile_eastern_nations = 0
electricity = 0
deforestation_laws = 0
coal_shortage = False
coal_neutral = True
coal_surplus = False
coal_deficit = False
electricity_shortage = False
electricity_neutral = True
electricity_surplus = False
electricity_deficit = False
oil_shortage = False
oil_neutral = True
oil_surplus = False
oil_deficit = False
apposed = 435
supporting = 0
coal_plant_count = 0
oil_refinery_count = 0
oil_refinery_cost = 50
coal_mine_count = 0
coal_plant_cost = 10
datacenter_count = 0
datacenter_cost = 100
lobbying_efforts = 0
page = 1

lobbying_timer = py.USEREVENT + 7
electricity_income_event = py.USEREVENT + 3
py.time.set_timer(electricity_income_event, 1000)
coal_income_event = py.USEREVENT + 1
py.time.set_timer(coal_income_event,  1000)
coal_mine_income_event = py.USEREVENT + 2
py.time.set_timer(coal_mine_income_event, 1000)
datacenter_income_event = py.USEREVENT + 4
py.time.set_timer(datacenter_income_event, 1000)
oil_refinery_income_event = py.USEREVENT + 5
py.time.set_timer(oil_refinery_income_event, 1000)
middile_eastern_income_event = py.USEREVENT + 6
py.time.set_timer(middile_eastern_income_event, 1000)
extrasmall_font = py.font.SysFont(None, configs.EXTRA_SMALL_FONT_SIZE)
font = py.font.SysFont(None, configs.SMALL_FONT_SIZE)
large_font = py.font.SysFont(None, configs.LARGE_FONT_SIZE)

# Load the static background image and define the base fill colour
background_image = py.image.load('background.bmp')
tree_img = py.image.load('tree-fix.bmp')
parliment_button = py.image.load('parliment.bmp')
coal_plant = py.image.load('coal.bmp')
minecart_img = py.image.load('minecart.bmp')
settings_img = py.image.load('settings.bmp')
datacenter_button_img = py.image.load('datacenter.bmp')
arrow_img = py.image.load('arrow.bmp')
other_arrow_img = py.image.load("otherarrow.bmp")
oil_refinery_img = py.image.load("oil refinery.bmp")

TRANSPARENT_COLOUR = (0, 0, 0)
tree_img.set_colorkey(TRANSPARENT_COLOUR)

# Scale the tree down to 30% so its smaller
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
arrow_scale = 0.3
arrow_img = py.transform.scale(
    arrow_img,
    (int(arrow_img.get_width() * arrow_scale), int(arrow_img.get_height() * arrow_scale))
)
other_arrow_img = py.transform.scale(
    other_arrow_img,
    (int(other_arrow_img.get_width() * arrow_scale), int(other_arrow_img.get_height() * arrow_scale))
)
arrow_img.set_colorkey((255, 0, 0))
other_arrow_img.set_colorkey((255, 0, 0))

oil_refinery_scale = 0.3
oil_refinery_img = py.transform.scale(
    oil_refinery_img,
    (int(oil_refinery_img.get_width() * oil_refinery_scale), int(oil_refinery_img.get_height() * oil_refinery_scale))
)
oil_refinery_img.set_colorkey((255, 0, 0))
# Read screen dimensions from configs so they can be tweaked in one place
(width, height) = (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)

# Create the window, set its title, then paint the background + image
screen = py.display.set_mode((width, height))
py.display.set_caption('Enviroment Clicker')

tree_x = width - 529
tree_y = 50

parliment_x = width - 1000
parliment_y = 520

arrow_x = width - 800
arrow_y = 440

other_arrow_x = width - 1000

#loading and scaling images for buttons
coal_scale = 0.5
coal_button_img = py.transform.scale(
    coal_plant,
    (int(coal_plant.get_width() * coal_scale), int(coal_plant.get_height() * coal_scale)),
)

little_coal_scale = 0.2
little_coal_button_img = py.transform.scale(
    coal_plant,
    (int(coal_plant.get_width() * little_coal_scale), int(coal_plant.get_height() * little_coal_scale)),
)
little_coal_button_img.set_colorkey((255, 0, 0))

# Keep an unscaled copy of the datacenter art around so we can also make a
# "little" version later, same as coal_plant is kept unscaled for little_coal_button_img
datacenter_img = py.image.load('datacenter.bmp')

little_datacenter_scale = 0.15
little_datacenter_button_img = py.transform.scale(
    datacenter_img,
    (int(datacenter_img.get_width() * little_datacenter_scale), int(datacenter_img.get_height() * little_datacenter_scale)),
)
little_datacenter_button_img.set_colorkey((255, 0, 0))

datacenter_scale = 0.35
datacenter_button_img = py.transform.scale(
    datacenter_button_img,
    (int(datacenter_button_img.get_width() * datacenter_scale), int(datacenter_button_img.get_height() * datacenter_scale)),
)

little_oil_refinery_scale = 0.2
little_oil_refinery_button_img = py.transform.scale(
    oil_refinery_img,
    (int(oil_refinery_img.get_width() * little_oil_refinery_scale), int(oil_refinery_img.get_height() * little_oil_refinery_scale)),
)
little_oil_refinery_button_img.set_colorkey((255, 0, 0))

# Where the background image sits on screen, so plants only spawn on top of it
background_rect = background_image.get_rect(topleft=(configs.SCREEN_WIDTH - 679, 0))

# The furthest right/down a little plant can start and still fit on the background
little_coal_max_x = background_rect.right - little_coal_button_img.get_width()
little_coal_max_y = background_rect.bottom - little_coal_button_img.get_height()

# The furthest right/down a little datacenter can start and still fit on the background
little_datacenter_max_x = background_rect.right - little_datacenter_button_img.get_width()
little_datacenter_max_y = background_rect.bottom - little_datacenter_button_img.get_height()

# The furthest right/down a little oil refinery can start and still fit on the background
little_oil_refinery_max_x = background_rect.right - little_oil_refinery_button_img.get_width()
little_oil_refinery_max_y = background_rect.bottom - little_oil_refinery_button_img.get_height()

# Holds one random (x, y) per built coal plant so they stay in the same spot each frame
coal_plant_positions = []

# Holds one (x, y) per built datacenter, spawned on top of the coal plants
datacenter_positions = []

# Holds one (x, y) per built oil refinery, spawned on top of the coal plants
oil_refinery_positions = []

coal_button_img.set_colorkey((255, 0, 0))
coal_button_rect = coal_button_img.get_rect(topleft=(5, 100))

settings_scale = 0.05
settings_img = py.transform.scale(
    settings_img,
    (int(settings_img.get_width() * settings_scale), int(settings_img.get_height() * settings_scale)),
)
settings_img.set_colorkey((255, 0, 0))
settings_button_rect = settings_img.get_rect(bottomright=(width - 10, height - 10))

tree_button_rect = tree_img.get_rect(topleft=(tree_x, tree_y))
parliment_button_rect = parliment_button.get_rect(topleft=(parliment_x, parliment_y))
arrow_button_rect = arrow_img.get_rect(topleft=(arrow_x, arrow_y))
other_arrow_button_rect = other_arrow_img.get_rect(topleft=(other_arrow_x, arrow_y))
coal_plant_rect = coal_plant.get_rect(topleft=(width - 800, 300))
oil_refinery_rect = oil_refinery_img.get_rect(topleft=(coal_button_rect.x, coal_button_rect.y))
running = True

# Menu graphics
menu_open = False
menu = py.Rect((width // 6, height // 6, 800, 600))
menu_close_button = py.Rect(menu.right - 120, menu.bottom - 60, 100, 40)
lobbying_button = py.Rect(menu.x + 20, menu.y + 160, 200, 40)
war_button = py.Rect(menu.x + 240, menu.y + 160, 340, 40)
deforestation_law_button = py.Rect(menu.x + 20, menu.y + 200, 300, 40)

# Settings menu graphics
settings_open = False
settings = py.Rect((width // 6, height // 6, 800, 600))
settings_close_button = py.Rect(settings.right - 120, settings.bottom - 60, 100, 40)


minecart_scale = 0.13
minecart_img = py.transform.scale(
    minecart_img,
    (int(minecart_img.get_width() * minecart_scale), int(minecart_img.get_height() * minecart_scale)),
)
minecart_img.set_colorkey((255, 0, 0))
minecart_rect = minecart_img.get_rect(topleft=(coal_button_rect.x + 8, coal_button_rect.y + coal_button_rect.height - 30))

datacenter_rect = datacenter_button_img.get_rect(topleft=(10, 350))
# Handler for inputs
while running:
    if money <= 0 or paused == True:
        paused = True
        screen.fill((255, 0, 0))
        losing_text = large_font.render("You lose!", True, (0, 0, 0))
        losing_text_rect = losing_text.get_rect(midtop=(width // 2, 20))
        play_again_button = py.Rect(0, 0, 400, 100)
        play_again_button.midtop = (width // 2, 640)
        play_again_button_text = font.render("Play Again", True, (0, 0, 0))
        play_again_text_rect = play_again_button_text.get_rect(center=play_again_button.center)
        py.draw.rect(screen, (0, 200, 0), play_again_button)
        screen.blit(losing_text, losing_text_rect)
        screen.blit(play_again_button_text, play_again_text_rect)
        py.display.flip()
        

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

            # Handler for mouse button down events
            # Use this to handler clicks by checking the coordinantes here
        if event.type == coal_income_event: 
            if not paused:
                money += coal_plant_count
                coal -= coal_plant_count

        if event.type == coal_mine_income_event:
            if not paused:
                coal += coal_mine_count

        if event.type == datacenter_income_event:
            if not paused:
                money += datacenter_count * 10

        if event.type == electricity_income_event:
            if not paused:
                electricity += (coal_plant_count + (oil_refinery_count * 10)) 
                electricity -= datacenter_count

        if event.type == oil_refinery_income_event:
            if not paused:
                money += oil_refinery_count * 5
                oil -= oil_refinery_count

        if event.type == middile_eastern_income_event:
            if not paused:
                oil += middile_eastern_nations

        if event.type == lobbying_timer:
            if not paused:
                money -= (lobbying_efforts * 1000)
                supporting = min(435, supporting + (10 * lobbying_efforts))
                apposed = max(0, apposed - (10 * lobbying_efforts))
                if lobbying_efforts == 0:
                    supporting = max(0, supporting - 10)
                    apposed = min(435, apposed + 10)

        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                # Menu subsection for inputs
                if menu_open:
                    if menu_close_button.collidepoint(event.pos):
                        menu_open = False
                    if lobbying_button.collidepoint(event.pos) and money > 1000 and lobbying_efforts < 44:
                        money -= 1000
                        supporting = min(435, supporting + 10)
                        apposed = max(0, apposed - 10)
                        if lobbying_efforts == 0:
                            py.time.set_timer(lobbying_timer, 100000)
                        lobbying_efforts += 1
                    if war_button.collidepoint(event.pos) and supporting >= 100:
                        middile_eastern_nations += 1
                        supporting = max(0, supporting - 50)
                        apposed = min(435, apposed + 50)
                    if deforestation_law_button.collidepoint(event.pos) and supporting >= 10:
                        deforestation_laws += 1
                        supporting = max(0, supporting - 5)
                        apposed = min(435, apposed + 5)

                if tree_button_rect.collidepoint(event.pos):
                    if deforestation_laws > 0:
                        money += deforestation_laws * (10 * deforestation_laws) 
                    money += 1
                    # theres no reason to add a trigger here to avoid += 1 money

                if arrow_button_rect.collidepoint(event.pos):
                    if page >= 1:
                        page += 1

                if other_arrow_button_rect.collidepoint(event.pos):
                    if page > 1:
                        page -= 1

                if parliment_button_rect.collidepoint(event.pos):
                    menu_open = True
                    settings_open = False
                
                if settings_button_rect.collidepoint(event.pos):
                    settings_open = True
                    menu_open = False

                if settings_open:
                    if settings_close_button.collidepoint(event.pos):
                        settings_open = False

                if page == 1:
                    if coal_button_rect.collidepoint(event.pos):
                        if money > coal_plant_cost and coal >= 1:
                            money -= coal_plant_cost
                            #CRUCIAL COAL FUNCTIONALITY FOR COAL IMPLEMENTATION
                            coal_plant_count += 1
                            coal_plant_cost = round(coal_plant_cost * 1.4)

                if page == 1:
                    if minecart_rect.collidepoint(event.pos):
                        if money > 5:
                            money -= 5
                            coal_mine_count += 1
                        
                if page == 1:  
                    if datacenter_rect.collidepoint(event.pos):
                        if money > datacenter_cost and electricity > 0:
                            money -= datacenter_cost
                            datacenter_count += 1
                            datacenter_cost = round(datacenter_cost * 1.4)

                if page == 2:
                    if oil_refinery_rect.collidepoint(event.pos):
                        if money > oil_refinery_cost and oil > 0:
                            money -= oil_refinery_cost
                            oil_refinery_count += 1
                            oil_refinery_cost = round(oil_refinery_cost * 1.4)

                if paused == True:
                    # The play_again button needs to be updated when we have more variables to reset everything back to step 1
                    if play_again_button.collidepoint(event.pos):
                        money = 1
                        apposed = 435
                        supporting = 0
                        coal_plant_count = 0
                        coal_plant_cost = 10
                        coal = 0
                        coal_shortage = False
                        paused = False
                        coal_mine_count = 0
                        datacenter_count = 0
                        datacenter_cost = 100
                        electricity = 0
                        oil = 0
                        middile_eastern_nations = 0
                        oil_refinery_count = 0
                        oil_refinery_cost = 50
                        page = 1
                        deforestation_laws = 0
                        lobbying_efforts = 0
        # Handler for keyboard inputs
        if event.type == py.KEYDOWN:

            # Developer cheatcode for testing money decreasing
            if event.key == py.K_9:
                money -= 1
            
            # Developer cheatcode for testing loseing 
            if event.key == py.K_8:
                paused = True

            # Developer cheatcode for adding coal
            if event.key == py.K_7:
                coal += 1

            # Developer cheatcode for adding coal powerplants
            if event.key == py.K_6:
                coal_plant_count += 1

            # Developer cheatcode for adding coal powerplants
            if event.key == py.K_5:
                coal_mine_count += 1
                
            #cheatcode for adding datacenters
            if event.key == py.K_4:
                datacenter_count += 1

            # Developer cheatcode for oil stuff
            if event.key == py.K_3:
                oil_refinery_count += 1

            # Adds middile eastern nations
            if event.key == py.K_2:
                middile_eastern_nations += 1

    if paused == False:
        screen.fill(background_colour)

        screen.blit(background_image, (width -679, 0))

        screen.blit(tree_img, tree_button_rect)

        screen.blit(arrow_img, arrow_button_rect)

        screen.blit(parliment_button, parliment_button_rect)

        screen.blit(settings_img, settings_button_rect)

        screen.blit(other_arrow_img, other_arrow_button_rect)

        py.draw.line(screen, (0, 0, 0), (width // 3.1, 0), (width // 3.1, height), 20)

        #little plants
        # Give any brand new plant a random spot on the background image
        while len(coal_plant_positions) < coal_plant_count:
            coal_plant_positions.append((
                random.randint(background_rect.left, little_coal_max_x),
                random.randint(background_rect.top, little_coal_max_y),
            ))

        # Forget spots for plants we lost (coal shortage or a game reset)
        while len(coal_plant_positions) > max(0, coal_plant_count):
            coal_plant_positions.pop()

        # Draw every plant at its saved spot
        for position in coal_plant_positions:
            screen.blit(little_coal_button_img, position)

        #little datacenters
        # Give any brand new datacenter a random spot on the background image
        while len(datacenter_positions) < datacenter_count:
            datacenter_positions.append((
                random.randint(background_rect.left, little_datacenter_max_x),
                random.randint(background_rect.top, little_datacenter_max_y),
            ))

        # Forget spots for datacenters we lost (game reset)
        while len(datacenter_positions) > datacenter_count:
            datacenter_positions.pop()

        # Draw every datacenter at its saved spot
        for position in datacenter_positions:
            screen.blit(little_datacenter_button_img, position)

        #little oil refineries
        # Give any brand new oil refinery a random spot on the background image
        while len(oil_refinery_positions) < oil_refinery_count:
            oil_refinery_positions.append((
                random.randint(background_rect.left, little_oil_refinery_max_x),
                random.randint(background_rect.top, little_oil_refinery_max_y),
            ))

        # Forget spots for oil refineries we lost (oil shortage or a game reset)
        while len(oil_refinery_positions) > max(0, oil_refinery_count):
            oil_refinery_positions.pop()

        # Draw every oil refinery at its saved spot
        for position in oil_refinery_positions:
            screen.blit(little_oil_refinery_button_img, position)

        money_counter = font.render(f"Money: {money}", True, (0, 0, 0))
        screen.blit(money_counter, (20, 50))

        # Resources go here:
        resources_x = int(width // 3.1) + 18  # Same programing as the line that runs down the middile 
        resources_y = 455 # just minus this by like 20 for new resources

        if coal <= -1:
            coal_shortage = True
            coal = 0
            coal_plant_count = max(0, coal_plant_count - 1)
        elif coal >= 2 or coal_mine_count == coal_plant_count:
            coal_shortage = False

        # 2. Reset flags so only one alert displays at a time
        coal_surplus = False
        coal_deficit = False
        coal_neutral = False

        if coal_shortage:
            pass 
        elif coal_plant_count == coal_mine_count:
            coal_neutral = True
        elif coal_plant_count > coal_mine_count:
            coal_deficit = True
        elif coal_mine_count > coal_plant_count:
            coal_surplus = True

        coal_count = font.render(f"Coal: {coal}", True, (0, 0, 0))
        electricity_count = font.render(f"Electricity: {electricity}", True, (0, 0, 0))
        oil_count = font.render(f"Oil: {oil}", True, (0, 0, 0))
        coal_shortage_alert = font.render("Coal Shortage!", True, (255, 0, 0))
        coal_neutral_alert = font.render("Coal Neutral!", True, (0, 0, 0))
        coal_deficit_alert = font.render("Coal Deficit!", True, (255, 165, 0))
        coal_surplus_alert = font.render("Coal Surplus!", True, (0, 255, 0))
        screen.blit(coal_count, (resources_x, resources_y))
        screen.blit(electricity_count, (resources_x , resources_y + 60))
        if coal_shortage == True:
            screen.blit(coal_shortage_alert, (resources_x + 290, resources_y))
        if coal_deficit == True:
            screen.blit(coal_deficit_alert, (resources_x + 290, resources_y))
        if coal_neutral == True:
            screen.blit(coal_neutral_alert, (resources_x + 290, resources_y))
        if coal_surplus == True:
            screen.blit(coal_surplus_alert, (resources_x + 290, resources_y))
            
            
        #electroicity deficit shit
        
        if electricity <= -1:
            electricity_shortage = True
            electricity = 0
            datacenter_count = max(0, datacenter_count - 1)
        elif electricity >= 2 or (coal_plant_count + (oil_refinery_count * 5)) == datacenter_count:
            electricity_shortage = False

        # Reset electricity status flags before determining the current alert.
        electricity_surplus = False
        electricity_deficit = False
        electricity_neutral = False

        if electricity_shortage:
            pass 
        elif (coal_plant_count + (oil_refinery_count * 5)) == datacenter_count:
            electricity_neutral = True
        elif datacenter_count > (coal_plant_count + (oil_refinery_count * 5)):
            electricity_deficit = True
        elif (coal_plant_count + (oil_refinery_count * 5)) > datacenter_count:
            electricity_surplus = True
        
        electricity_shortage_alert = font.render("Electricity Shortage!", True, (255, 0, 0))
        electricity_neutral_alert = font.render("Electricity Neutral!", True, (0, 0, 0))
        electricity_deficit_alert = font.render("Electricity Deficit!", True, (255, 165, 0))
        electricity_surplus_alert = font.render("Electricity Surplus!", True, (0, 255, 0))
        screen.blit(coal_count, (resources_x, resources_y))
        screen.blit(electricity_count, (resources_x , resources_y + 60))
        if electricity_shortage == True:
            screen.blit(electricity_shortage_alert, (resources_x + 290, resources_y + 60))
        if electricity_deficit == True:
            screen.blit(electricity_deficit_alert, (resources_x + 290, resources_y + 60))
        if electricity_neutral == True:
            screen.blit(electricity_neutral_alert, (resources_x + 290, resources_y + 60))
        if electricity_surplus == True:
            screen.blit(electricity_surplus_alert, (resources_x + 290, resources_y + 60))

        if oil <= -1:
            oil_shortage = True
            oil = 0
            oil_refinery_count = max(0, oil_refinery_count - 1)
        elif oil >= 2 or oil_refinery_count == middile_eastern_nations:
            oil_shortage = False

        # Reset electricity status flags before determining the current alert.
        oil_surplus = False
        oil_deficit = False
        oil_neutral = False

        if oil_shortage:
            pass 
        elif middile_eastern_nations == oil_refinery_count:
            oil_neutral = True
        elif oil_refinery_count > middile_eastern_nations:
            oil_deficit = True
        elif middile_eastern_nations > oil_refinery_count:
            oil_surplus = True

        oil_shortage_alert = font.render("Oil Shortage!", True, (255, 0, 0))
        oil_neutral_alert = font.render("Oil Neutral!", True, (0, 0, 0 ))
        oil_deficit_alert = font.render("Oil Deficit!", True, (255, 165, 0))
        oil_surplus_alert = font.render("Oil Surplus!", True, (0, 255, 0))
        screen.blit(oil_count, (resources_x, resources_y + 120))
        if oil_shortage == True:
            screen.blit(oil_shortage_alert, (resources_x + 290, resources_y + 120))
        if oil_deficit == True:
            screen.blit(oil_deficit_alert, (resources_x + 290, resources_y + 120))
        if oil_neutral == True:
            screen.blit(oil_neutral_alert, (resources_x + 290, resources_y + 120))
        if oil_surplus == True:
            screen.blit(oil_surplus_alert, (resources_x + 290, resources_y + 120))

        if page == 1:
            #coal plant text
            coal_plant_info = extrasmall_font.render(f"Coal Plants: {coal_plant_count}", True, (0, 0, 0))
            coal_plant_cost_info = extrasmall_font.render(f"Cost: {coal_plant_cost}", True, (0, 0, 0))
            coal_cost = extrasmall_font.render("Coal Consumption: 1", True, (0, 0, 0))
            datacenter_info = extrasmall_font.render(f"Datacenters: {datacenter_count}", True, (0, 0, 0))
            datacenter_cost_info = extrasmall_font.render(f"Datacenter Cost: {datacenter_cost}", True, (0, 0, 0))
            coal_mine_count_info = extrasmall_font.render(f"Coal Mine Count {coal_mine_count}", True, (0, 0, 0))
            datacenter_electricity = extrasmall_font.render(f"Electricty Cost: 1", True, (0, 0, 0))
            screen.blit(coal_plant_info, (140, 180))
            screen.blit(coal_plant_cost_info, (140, 210))
            screen.blit(coal_cost, (140, 240))
            screen.blit(coal_mine_count_info, (140, 300))
            screen.blit(datacenter_info, (160, 410))
            screen.blit(datacenter_cost_info, (160, 390))
            screen.blit(datacenter_electricity, (160, 430))
            screen.blit(coal_button_img, coal_button_rect)
            screen.blit(minecart_img, minecart_rect)
            screen.blit(datacenter_button_img, datacenter_rect)
        if page == 2:
            # Put buildings and text and stuff thats required for the next page here.
            screen.blit(oil_refinery_img, oil_refinery_rect)
            oil_plant_info = extrasmall_font.render(f"Oil Plants: {oil_refinery_count}", True, (0, 0, 0))
            oil_plant_cost_info = extrasmall_font.render(f"Cost: {oil_refinery_cost}", True, (0, 0, 0))
            oil_cost = extrasmall_font.render("Oil Consumption: 1", True, (0, 0, 0))
            screen.blit(oil_plant_info, (140, 160))
            screen.blit(oil_plant_cost_info, (140, 190))
            screen.blit(oil_cost, (140, 220))
        if menu_open:
            py.draw.rect(screen, (255, 255, 255), menu)
            py.draw.rect(screen, (0, 0, 0), menu, 5)

            menu_title = font.render("Parliment", True, (0, 0, 0))
            negative_influence_counter = font.render(f"Apposed: {apposed}", True, (0, 0, 0))
            positive_influence_counter = font.render(f"Supporting: {supporting}", True, (0, 0, 0))
            middile_eastern_nations_counter = font.render(f"Middile eastern nations: {middile_eastern_nations}", True, (0, 0, 0))
            deforestation_laws_counter = font.render(f"Deforestation laws: {deforestation_laws}", True, (0, 0, 0))
            screen.blit(menu_title, (menu.x + 20, menu.y + 20))
            screen.blit(middile_eastern_nations_counter, (menu.x + 20, menu.y + 240))
            screen.blit(deforestation_laws_counter, (menu.x + 20, menu.y + 280))
            screen.blit(positive_influence_counter, (menu.x + 20, menu.y + 55))
            screen.blit(negative_influence_counter, (menu.x + 20, menu.y + 90))

            py.draw.rect(screen, (100, 200, 255), lobbying_button)
            py.draw.rect(screen, (0, 0, 0), lobbying_button, 2)
            py.draw.rect(screen, (100, 100, 255), war_button)
            py.draw.rect(screen, (0, 0, 0), war_button, 2)
            py.draw.rect(screen, (50, 255, 50), deforestation_law_button)
            py.draw.rect(screen, (0, 0, 0), deforestation_law_button, 2)
            lobbying_text = button_text = extrasmall_font.render(f"Lobbying efforts: {lobbying_efforts}", True, (0, 0, 0))
            lobbying_text_rect = button_text.get_rect(center=lobbying_button.center)
            war_text = war_button_text = extrasmall_font.render("Invade middile eastern nation, requires 100 support", True, (0, 0, 0))
            war_text_rect = war_button_text.get_rect(center=war_button.center)
            deforestation_text = deforestation_button_text = extrasmall_font.render("Deforestation law, requires 10 support", True, (0, 0, 0))
            deforestation_text_rect = deforestation_text.get_rect(center=deforestation_law_button.center)
            screen.blit(button_text, lobbying_text_rect)
            screen.blit(war_button_text, war_text_rect)
            screen.blit(deforestation_text, deforestation_text_rect)
            py.draw.rect(screen, (255, 100, 100), menu_close_button)
            py.draw.rect(screen, (0, 0, 0), menu_close_button, 2)
            py.draw.line(screen, (0, 0, 0), (menu.x + 20, menu.y + 140), (menu.right - 20, menu.y + 140), 3)
            close_text = extrasmall_font.render("Close", True, (0, 0, 0))
            close_rect = close_text.get_rect(center=menu_close_button.center)
            screen.blit(close_text, close_rect)
        if settings_open:
            py.draw.rect(screen, (255, 255, 255), menu)
            py.draw.rect(screen, (0, 0, 0), menu, 5)

            settings_title = font.render("Settings", True, (0, 0, 0))
            screen.blit(settings_title, (settings.x + 20, settings.y + 20))

            py.draw.rect(screen, (255, 100, 100), settings_close_button)
            py.draw.rect(screen, (0, 0, 0), settings_close_button, 2)
    py.display.flip()

py.quit()
sys.exit()

