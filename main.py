# how to update
# 0) save the files normally in the editor tab
# 1) git add .
# 2) git commit -m "put update notes here"
# 3) git push
# pull if it tells you to its just git pull
import sys
import json
import pygame as py
import configs
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / 'models'

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
nuclear_meltdown = False
uranium_neutral = True
uranium_surplus = False
uranium_deficit = False
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
pop_up_alert_timer = 10
replaced_building = "coal power plants"
removed_count = 1
wind_turbine_count = 0
nuclear_plant_count = 0
nuclear_reactor_cost = 1000
uranium = 0
exploited_african_nations = 0
environmental_destruction = 0
information_page = 1
clock = py.time.Clock()
# Default for replaced building

wind_turbine_cleaning = py.USEREVENT + 13
py.time.set_timer(wind_turbine_cleaning, 1000)
african_nation_income = py.USEREVENT + 12
py.time.set_timer(african_nation_income, 1000)
nuclear_plant_income = py.USEREVENT + 11
py.time.set_timer(nuclear_plant_income, 1000)
nuclear_meltdown_event = py.USEREVENT + 10
pop_up_descision_timer = py.USEREVENT + 9
pop_up_timer = py.USEREVENT + 8
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
small_font = py.font.SysFont(None, configs.SMALLER_FONT_SIZE)
font = py.font.SysFont(None, configs.SMALL_FONT_SIZE)
large_font = py.font.SysFont(None, configs.LARGE_FONT_SIZE)

# Load the static background image and define the base fill colour
background_image = py.image.load(str(MODELS_DIR / 'background.bmp'))
tree_img = py.image.load(str(MODELS_DIR / 'tree-fix.bmp'))
parliment_button = py.image.load(str(MODELS_DIR / 'parliment.bmp'))
coal_plant = py.image.load(str(MODELS_DIR / 'coal.bmp'))
minecart_img = py.image.load(str(MODELS_DIR / 'minecart.bmp'))
information_img = py.image.load(str(MODELS_DIR / 'information.bmp'))
datacenter_button_img = py.image.load(str(MODELS_DIR / 'datacenter.bmp'))
arrow_img = py.image.load(str(MODELS_DIR / 'arrow.bmp'))
other_arrow_img = py.image.load(str(MODELS_DIR / 'otherarrow.bmp'))
oil_refinery_img = py.image.load(str(MODELS_DIR / 'oil refinery.bmp'))
wind_turbine_img = py.image.load(str(MODELS_DIR / 'Wind_turbine_icon.bmp'))
nuclear_reactor_img = py.image.load(str(MODELS_DIR / 'Nuclear plant icon.bmp'))
meltdown_alert = py.image.load(str(MODELS_DIR / 'meltdown.bmp'))
save_img = py.image.load(str(MODELS_DIR / 'save.bmp'))

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

nuclear_plant_scale = 0.15
nuclear_reactor_img = py.transform.scale(
    nuclear_reactor_img,
    (int(nuclear_reactor_img.get_width() * nuclear_plant_scale), int(nuclear_reactor_img.get_height() * nuclear_plant_scale))
)

meltdown_alert_scale = 1
meltdown_alert = py.transform.scale(
    meltdown_alert,
    (int(meltdown_alert.get_width() * meltdown_alert_scale), int(meltdown_alert.get_height() * meltdown_alert_scale))
)
oil_refinery_img.set_colorkey((255, 0, 0))
# Read screen dimensions from configs so they can be tweaked in one place
(width, height) = (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)

# Create the window, set its title, then paint the background + image
screen = py.display.set_mode((width, height))
py.display.set_caption('Environment Clicker')

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
datacenter_img = py.image.load(str(MODELS_DIR / 'datacenter.bmp'))

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

little_wind_turbine_scale = 0.035
little_wind_turbine_button_img = py.transform.scale(
    wind_turbine_img,
    (int(wind_turbine_img.get_width() * little_wind_turbine_scale), int(wind_turbine_img.get_height() * little_wind_turbine_scale)),
)
little_wind_turbine_button_img.set_colorkey((255, 0, 0))

# Where the background image sits on screen, so plants only spawn on top of it
background_rect = background_image.get_rect(topleft=(configs.SCREEN_WIDTH - 679, 0))

# Lillte icons calculations
little_coal_max_x = background_rect.right - little_coal_button_img.get_width()
little_coal_max_y = background_rect.bottom - little_coal_button_img.get_height()

little_datacenter_max_x = background_rect.right - little_datacenter_button_img.get_width()
little_datacenter_max_y = background_rect.bottom - little_datacenter_button_img.get_height()

little_oil_refinery_max_x = background_rect.right - little_oil_refinery_button_img.get_width()
little_oil_refinery_max_y = background_rect.bottom - little_oil_refinery_button_img.get_height()

little_wind_turbine_max_x = background_rect.right - little_wind_turbine_button_img.get_width()
little_wind_turbine_max_y = background_rect.bottom - little_wind_turbine_button_img.get_height()

# Holding posistions of the little icons 
coal_plant_positions = []

datacenter_positions = []

oil_refinery_positions = []

wind_turbine_positions = []

coal_button_img.set_colorkey((255, 0, 0))
coal_button_rect = coal_button_img.get_rect(topleft=(5, 100))

information_scale = 0.36
information_img = py.transform.scale(
    information_img,
    (int(information_img.get_width() * information_scale), int(information_img.get_height() * information_scale)),
)
information_img.set_colorkey((255, 0, 0))
information_button_rect = information_img.get_rect(bottomright=(width - 10, height + 2))

save_scale = 0.11
save_img = py.transform.scale(
    save_img,
    (int(save_img.get_width() * save_scale), int(save_img.get_height() * save_scale)),
)
save_img.set_colorkey((255, 0, 0))
save_button_rect = save_img.get_rect(bottomright=(information_button_rect.left - 10, height - 10))

tree_button_rect = tree_img.get_rect(topleft=(tree_x, tree_y))
parliment_button_rect = parliment_button.get_rect(topleft=(parliment_x, parliment_y))
arrow_button_rect = arrow_img.get_rect(topleft=(arrow_x, arrow_y))
other_arrow_button_rect = other_arrow_img.get_rect(topleft=(other_arrow_x, arrow_y))
coal_plant_rect = coal_plant.get_rect(topleft=(width - 800, 300))
oil_refinery_rect = oil_refinery_img.get_rect(topleft=(coal_button_rect.x, coal_button_rect.y))
meltdown_alert_rect = meltdown_alert.get_rect()
meltdown_alert_rect.center = screen.get_rect().center

# Save file location
save_directory = Path.home() / 'Library' / 'Application Support' / 'Clicker Game'
save_directory.mkdir(parents=True, exist_ok=True)
save_file = save_directory / 'savegame.json'

# Function to save game stats into a json file
def save_game():
    global save_feedback
    # Pack game variables into a dictionary
    save_data = {
        'money': money,
        'coal': coal,
        'oil': oil,
        'electricity': electricity,
        'middile_eastern_nations': middile_eastern_nations,
        'deforestation_laws': deforestation_laws,
        'apposed': apposed,
        'supporting': supporting,
        'coal_plant_count': coal_plant_count,
        'coal_plant_cost': coal_plant_cost,
        'coal_mine_count': coal_mine_count,
        'oil_refinery_count': oil_refinery_count,
        'oil_refinery_cost': oil_refinery_cost,
        'datacenter_count': datacenter_count,
        'datacenter_cost': datacenter_cost,
        'lobbying_efforts': lobbying_efforts,
        'page': page,
        'wind_turbine_count': wind_turbine_count,
        'nuclear_plant_count': nuclear_plant_count,
        'nuclear_reactor_cost': nuclear_reactor_cost,
        'environmental_destruction': environmental_destruction,
        'exploited_african_nations': exploited_african_nations,
        'uranium': uranium
    }
    # Write dictionary to json file
    with save_file.open('w', encoding='utf-8') as f:
        json.dump(save_data, f, indent=4)
    save_feedback = "Game saved!"

# Function to load game stats from the json file
def load_game():
    global money, coal, oil, electricity, middile_eastern_nations, deforestation_laws
    global apposed, supporting, coal_plant_count, oil_refinery_count, oil_refinery_cost
    global coal_mine_count, coal_plant_cost, datacenter_count, datacenter_cost, save_feedback
    global lobbying_efforts, page, wind_turbine_count, nuclear_plant_count, nuclear_reactor_cost
    global environmental_destruction, exploited_african_nations, uranium
    try:
        # Read the dictionary from the json file
        with save_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
        # Restore all the stats
        money = data['money']
        coal = data['coal']
        oil = data['oil']
        electricity = data['electricity']
        middile_eastern_nations = data['middile_eastern_nations']
        deforestation_laws = data['deforestation_laws']
        apposed = data['apposed']
        supporting = data['supporting']
        coal_plant_count = data['coal_plant_count']
        coal_plant_cost = data['coal_plant_cost']
        coal_mine_count = data['coal_mine_count']
        oil_refinery_count = data['oil_refinery_count']
        oil_refinery_cost = data['oil_refinery_cost']
        datacenter_count = data['datacenter_count']
        datacenter_cost = data['datacenter_cost']
        lobbying_efforts = data['lobbying_efforts']
        page = data['page']
        wind_turbine_count = data['wind_turbine_count']
        nuclear_plant_count = data['nuclear_plant_count']
        nuclear_reactor_cost = data['nuclear_reactor_cost']
        environmental_destruction = data['environmental_destruction']
        exploited_african_nations = data['exploited_african_nations']
        uranium = data['uranium']
        save_feedback = "Game loaded!"
    except:
        # If the file doesn't exist yet
        save_feedback = "No save file found!"

running = True

# Menu graphics
menu_open = False
menu = py.Rect((width // 6, height // 6, 800, 600))
menu_close_button = py.Rect(menu.right - 120, menu.bottom - 60, 100, 40)
lobbying_button = py.Rect(menu.x + 20, menu.y + 160, 200, 40)
war_button = py.Rect(menu.x + 240, menu.y + 160, 340, 40)
deforestation_law_button = py.Rect(menu.x + 20, menu.y + 200, 300, 40)
exploit_african_nation_button = py.Rect(menu.x + 340, menu.y + 200, 300, 40)

# Information menu graphics
information_open = False
information = py.Rect((width // 6, height // 6, 800, 600))
information_close_button = py.Rect(information.right - 120, information.bottom - 60, 100, 40)
information_arrow_button_rect = arrow_img.get_rect(topleft=(information.left + 500, information.top + 500))
information_other_arrow_button_rect = other_arrow_img.get_rect(topleft=(information.left + 10, information.top + 500))

# Save/Load menu graphics
save_open = False
save_menu = py.Rect((width // 6, height // 6, 800, 600))
save_close_button = py.Rect(save_menu.right - 120, save_menu.bottom - 60, 100, 40)
save_game_button = py.Rect(save_menu.x + 20, save_menu.y + 160, 200, 40)
load_game_button = py.Rect(save_menu.x + 240, save_menu.y + 160, 200, 40)
save_feedback = ""

# pop up graphics
pop_up_alert_open = False
pop_up_alert = py.Rect((width // 6, height // 6, 800, 600))
pop_up_close_button = py.Rect(pop_up_alert.left + 20, pop_up_alert.bottom - 70, 150, 50)
pop_up_pay_button = py.Rect(pop_up_alert.right - 220, pop_up_alert.bottom - 70, 200, 50)

minecart_scale = 0.13
minecart_img = py.transform.scale(
    minecart_img,
    (int(minecart_img.get_width() * minecart_scale), int(minecart_img.get_height() * minecart_scale)),
)
minecart_img.set_colorkey((255, 0, 0))
minecart_rect = minecart_img.get_rect(topleft=(coal_button_rect.x + 8, coal_button_rect.y + coal_button_rect.height - 30))
nuclear_plant_rect = nuclear_reactor_img.get_rect(topleft=(minecart_rect.x, minecart_rect.y - 40))
datacenter_rect = datacenter_button_img.get_rect(topleft=(10, 350))
parliment_information_scale = 0.025
parliment_information_image = py.transform.scale(
    parliment_button,
    (int(parliment_button.get_width() * parliment_scale), int(parliment_button.get_height() * parliment_scale)),
)
# Handler for inputs
while running:
    if money < 0:
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
    if environmental_destruction >= 100 and money > -1:
        paused = True
        screen.fill((0, 225, 0))
        winning_text = large_font.render("You Win!", True, (0, 0, 0))
        winning_text_rect = winning_text.get_rect(midtop=(width // 2, 20))
        play_again_button = py.Rect(0, 0, 400, 100)
        play_again_button.midtop = (width // 2, 640)
        play_again_button_text = font.render("Play Again", True, (0, 0, 0))        
        play_again_text_rect = play_again_button_text.get_rect(center=play_again_button.center)
        py.draw.rect(screen, (255, 0, 0), play_again_button)
        screen.blit(winning_text, winning_text_rect)
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
                coal = min(999, coal)
                environmental_destruction += (coal_plant_count / 100)

        if event.type == coal_mine_income_event:
            if not paused:
                coal += coal_mine_count
                coal = min(999, coal)

        if event.type == datacenter_income_event:
            if not paused:
                money += datacenter_count * 10
                environmental_destruction += (datacenter_count / 70)

        if event.type == electricity_income_event:
            if not paused:
                electricity += (coal_plant_count + (oil_refinery_count * 10) + (nuclear_plant_count * 100)) 
                electricity -= datacenter_count
                electricity = min(999, electricity)

        if event.type == oil_refinery_income_event:
            if not paused:
                money += oil_refinery_count * 5
                oil -= oil_refinery_count
                oil = min(999, oil)
                environmental_destruction += (oil_refinery_count / 30)

        if event.type == middile_eastern_income_event:
            if not paused:
                oil += middile_eastern_nations
                oil = min(999, oil)

        if event.type == lobbying_timer:
            if not paused:
                money -= (lobbying_efforts * 1000)
                supporting = min(435, supporting + (10 * lobbying_efforts))
                apposed = max(0, apposed - (10 * lobbying_efforts))
                if lobbying_efforts == 0:
                    supporting = max(0, supporting - 10)
                    apposed = min(435, apposed + 10)

        if event.type == pop_up_timer:
            if not paused:
                random_options = ["coal power plants", 'oil refineries', 'coal mines', 'datacenters', 'uranium mines', 'oil mines']
                replaced_building = random.choice(random_options)
                if replaced_building == 'coal power plants':
                    removed_count = random.randint(0, coal_plant_count)
                elif replaced_building == 'oil refineries':
                    removed_count = random.randint(0, oil_refinery_count)
                elif replaced_building == 'coal mines':
                    removed_count = random.randint(0, coal_mine_count)
                elif replaced_building == 'datacenters':
                    removed_count = random.randint(0, datacenter_count)
                elif replaced_building == 'uranium mines':
                    removed_count = random.randint(0, exploited_african_nations)
                elif replaced_building == 'oil mines':
                    removed_count = random.randint(0, middile_eastern_nations)
                pop_up_alert_open = True
                menu_open = False
                information_open = False
                pop_up_alert_timer = 10
                py.time.set_timer(pop_up_descision_timer, 1000)
                # Its intentional that it can sometimes ask to replace 0 buildings
                # This means you have to read the alerts otherwise you can pay for nothing
        
        if event.type == pop_up_descision_timer:
            if not paused:
                if pop_up_alert_open:
                    pop_up_alert_timer -= 1

                if pop_up_alert_timer <= 0:
                    pop_up_alert_timer = 0

                    if replaced_building == 'coal power plants':
                        coal_plant_count -= removed_count
                    elif replaced_building == 'oil refineries':
                        oil_refinery_count -= removed_count
                    elif replaced_building == 'coal mines':
                        coal_mine_count -= removed_count
                    elif replaced_building == 'datacenters':
                        datacenter_count -= removed_count
                    elif replaced_building == 'uranium mines':
                        exploited_african_nations -= removed_count
                    elif replaced_building == 'oil mines':
                        middile_eastern_nations -= removed_count

                    wind_turbine_count += removed_count
                    pop_up_alert_open = False
                    py.time.set_timer(pop_up_descision_timer, 0)

        if event.type == nuclear_meltdown_event:
            if not paused:
                money -= 100000
                nuclear_plant_count = 0
                datacenter_count = 0
                coal_mine_count = 0
                coal_plant_count = 0
                oil_refinery_count = 0
                uranium = 0
                environmental_destruction += 50
                py.time.set_timer(nuclear_meltdown_event, 0)
                nuclear_meltdown = False
        if event.type == nuclear_plant_income:
            if not paused:
                money += (nuclear_plant_count * 120)
                uranium -= nuclear_plant_count

        if event.type == african_nation_income:
            if not paused:
                uranium += exploited_african_nations

        if event.type == wind_turbine_cleaning:
            if not paused:
                money -= (wind_turbine_count * 10)
                environmental_destruction = max(0, environmental_destruction - (wind_turbine_count / 10))
                # supposed to make it so environmental destruction cant go below 0 
        
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                # Menu subsection for inputs
                
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
                        pop_up_alert_open = False
                        pop_up_alert_timer = 10
                        menu_open = False
                        information_open = False
                        save_open = False
                        wind_turbine_count = 0
                        coal_plant_positions.clear()
                        datacenter_positions.clear()
                        oil_refinery_positions.clear()
                        wind_turbine_positions.clear()
                        py.time.set_timer(pop_up_descision_timer, 0)
                        py.time.set_timer(pop_up_timer, 0)
                        py.time.set_timer(lobbying_timer, 0)
                        py.time.set_timer(nuclear_meltdown_event, 0)
                        nuclear_plant_count = 0
                        nuclear_reactor_cost = 1000
                        uranium = 0
                        nuclear_meltdown = False
                        exploited_african_nations = 0
                        environmental_destruction = 0
                        information_page = 1

                elif pop_up_alert_open:
                    if pop_up_pay_button.collidepoint(event.pos):
                        if money >= 10000:
                            money -= 10000
                            pop_up_alert_open = False
                            py.time.set_timer(pop_up_descision_timer, 0)
                    elif pop_up_close_button.collidepoint(event.pos):
                            if replaced_building == 'coal power plants':
                                coal_plant_count -= removed_count
                            elif replaced_building == 'oil refineries':
                                oil_refinery_count -= removed_count
                            elif replaced_building == 'coal mines':
                                coal_mine_count -= removed_count
                            elif replaced_building == 'datacenters':
                                datacenter_count -= removed_count
                            elif replaced_building == 'uranium mines':
                                exploited_african_nations -= removed_count
                            elif replaced_building == 'oil mines':
                                middile_eastern_nations -= removed_count
                            
                            wind_turbine_count += removed_count
                            pop_up_alert_open = False
                            py.time.set_timer(pop_up_descision_timer, 0)

                elif menu_open:
                    if menu_close_button.collidepoint(event.pos):
                        menu_open = False
                    if lobbying_button.collidepoint(event.pos) and money >= 1000 and lobbying_efforts < 44:
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
                    if deforestation_law_button.collidepoint(event.pos) and supporting >= 10 and deforestation_laws < 5:
                        deforestation_laws += 1
                        supporting = max(0, supporting - 5)
                        apposed = min(435, apposed + 5)
                    if exploit_african_nation_button.collidepoint(event.pos) and supporting >= 200:
                        exploited_african_nations += 1
                        supporting = max(0, supporting - 100)
                        apposed = min(435, apposed + 100)

                elif information_open:
                    if information_close_button.collidepoint(event.pos):
                        information_open = False
                    if information_arrow_button_rect.collidepoint(event.pos):
                        if information_page < 4:
                            information_page += 1
                    if information_other_arrow_button_rect.collidepoint(event.pos):
                        if information_page > 1:
                            information_page -= 1

                elif save_open:
                    if save_close_button.collidepoint(event.pos):
                        save_open = False
                    if save_game_button.collidepoint(event.pos):
                        save_game()
                    if load_game_button.collidepoint(event.pos):
                        load_game()

                else:
                    if tree_button_rect.collidepoint(event.pos):
                        if deforestation_laws > 0:
                            money += deforestation_laws * (10 * deforestation_laws) 
                        money += 1
                        # theres no reason to add a trigger here to avoid += 1 money

                    if arrow_button_rect.collidepoint(event.pos):
                        if page >= 1:
                            if page < 2:
                                page += 1

                    if other_arrow_button_rect.collidepoint(event.pos):
                        if page > 1:
                            page -= 1

                    if parliment_button_rect.collidepoint(event.pos):
                        menu_open = True
                        information_open = False
                    
                    if information_button_rect.collidepoint(event.pos):
                        information_open = True
                        menu_open = False

                    if save_button_rect.collidepoint(event.pos):
                        save_open = True
                        menu_open = False
                        information_open = False
                        save_feedback = ""

                    if page == 1:
                        if coal_button_rect.collidepoint(event.pos):
                            if money >= coal_plant_cost and coal >= 1:
                                money -= coal_plant_cost
                                #CRUCIAL COAL FUNCTIONALITY FOR COAL IMPLEMENTATION
                                coal_plant_count += 1
                                coal_plant_cost = round(coal_plant_cost * 1.4)

                    if page == 1:
                        if minecart_rect.collidepoint(event.pos):
                            if money >= 5:
                                money -= 5
                                if coal_mine_count == 0:
                                    py.time.set_timer(pop_up_timer, 90000)
                                coal_mine_count += 1
                            
                    if page == 1:  
                        if datacenter_rect.collidepoint(event.pos):
                            if money >= datacenter_cost and electricity > 0:
                                money -= datacenter_cost
                                datacenter_count += 1
                                datacenter_cost = round(datacenter_cost * 1.4)

                    if page == 2:
                        if oil_refinery_rect.collidepoint(event.pos):
                            if money >= oil_refinery_cost and oil > 0:
                                money -= oil_refinery_cost
                                oil_refinery_count += 1
                                oil_refinery_cost = round(oil_refinery_cost * 1.4)

                    if page == 2:
                        if nuclear_plant_rect.collidepoint(event.pos):
                            if money >= nuclear_reactor_cost and uranium > 0:
                                money -= nuclear_reactor_cost
                                nuclear_plant_count += 1
                                nuclear_reactor_cost = round(nuclear_reactor_cost * 1.4)

        # Handler for keyboard inputs
        if event.type == py.KEYDOWN:
            if configs.DEVELOPER_MODE == True:
                # Developer cheatcode for money increasing
                if event.key == py.K_9:
                    money += 10000
                
                # Developer cheatcode for testing money decreasig 
                if event.key == py.K_8:
                    money -= 10000

                # Developer cheatcode for adding coal
                if event.key == py.K_7:
                    coal = min(999, coal + 1)

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

                # Developer cheatcode for triggering pop up
                if event.key == py.K_1:
                    random_options = ["coal power plants", 'oil refineries', 'coal mines', 'datacenters', 'uranium mines', 'oil mines']
                    replaced_building = random.choice(random_options)
                    if replaced_building == 'coal power plants':
                        removed_count = random.randint(0, coal_plant_count)
                    elif replaced_building == 'oil refineries':
                        removed_count = random.randint(0, oil_refinery_count)
                    elif replaced_building == 'coal mines':
                        removed_count = random.randint(0, coal_mine_count)
                    elif replaced_building == 'datacenters':
                        removed_count = random.randint(0, datacenter_count)
                    elif replaced_building == 'uranium mines':
                        removed_count = random.randint(0, exploited_african_nations)
                    elif replaced_building == 'oil mines':
                        removed_count = random.randint(0, middile_eastern_nations)
                    pop_up_alert_open = True
                    pop_up_alert_timer = 10
                    py.time.set_timer(pop_up_descision_timer, 1000)

                # Developer cheatcode for triggering victory
                if event.key == py.K_w:
                    environmental_destruction += 100

                # Developer cheatcode for triggering losing
                if event.key == py.K_l:
                    money -= 1999999999999999999999

    if paused == False:
        screen.fill(background_colour)

        screen.blit(background_image, (width -679, 0))

        screen.blit(tree_img, tree_button_rect)

        screen.blit(arrow_img, arrow_button_rect)

        screen.blit(parliment_button, parliment_button_rect)

        screen.blit(information_img, information_button_rect)

        screen.blit(save_img, save_button_rect)

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

        #little wind turbines
        # Give any brand new wind turbine a random spot on the background image
        while len(wind_turbine_positions) < wind_turbine_count:
            wind_turbine_positions.append((
                random.randint(
                    background_rect.left,
                    max(background_rect.left, little_wind_turbine_max_x)
                ),
                random.randint(
                    background_rect.top,
                    max(background_rect.top, little_wind_turbine_max_y)
                ),
            ))

        while len(wind_turbine_positions) > max(0, wind_turbine_count):
            wind_turbine_positions.pop()

        for position in wind_turbine_positions:
            screen.blit(little_wind_turbine_button_img, position)

        money_counter = font.render(f"Money: {money}", True, (0, 0, 0))
        environmental_destruction_counter = small_font.render(f"Environmental Destruction: {environmental_destruction:.2f}/100", True, (0, 0, 0))
        screen.blit(environmental_destruction_counter, (340, 20))
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
        coal = min(999, coal)

        # Reset flags so only one alert displays at a time
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
        elif electricity >= 2 or (coal_plant_count + (oil_refinery_count * 10) + (nuclear_plant_count * 100)) == datacenter_count:
            electricity_shortage = False
        electricity = min(999, electricity)

        # Reset electricity status flags before determining the current alert.
        electricity_surplus = False
        electricity_deficit = False
        electricity_neutral = False

        if electricity_shortage:
            pass 
        elif (coal_plant_count + (oil_refinery_count * 10) + (nuclear_plant_count * 100)) == datacenter_count:
            electricity_neutral = True
        elif datacenter_count > (coal_plant_count + (oil_refinery_count * 10) + (nuclear_plant_count * 100)):
            electricity_deficit = True
        elif (coal_plant_count + (oil_refinery_count * 10) + (nuclear_plant_count * 100)) > datacenter_count:
            electricity_surplus = True
        
        electricity_shortage_alert = font.render("Electricity Shortage!", True, (255, 0, 0))
        electricity_neutral_alert = font.render("Electricity Neutral!", True, (0, 0, 0))
        electricity_deficit_alert = font.render("Electricity Deficit!", True, (255, 165, 0))
        electricity_surplus_alert = font.render("Electricity Surplus!", True, (0, 255, 0))
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
        oil = min(999, oil)

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

        if uranium <= -1 and not nuclear_meltdown:
            nuclear_meltdown = True
            py.time.set_timer(nuclear_meltdown_event, 2000)

        if nuclear_meltdown:
            screen.blit(meltdown_alert, meltdown_alert_rect)
            # meltdown instantly destroys all nuclear reactors and costs money
            # Also causes enviromental destruction
        elif exploited_african_nations >= nuclear_plant_count:
            nuclear_meltdown = False

        uranium_surplus = False
        uranium_deficit = False
        uranium_neutral = False

        if nuclear_meltdown:
            pass 
        elif exploited_african_nations == nuclear_plant_count:
            uranium_neutral = True
        elif nuclear_plant_count > exploited_african_nations:
            uranium_deficit = True
        elif exploited_african_nations > nuclear_plant_count:
            uranium_surplus = True

        uranium_count_text = font.render(f"Uranium: {uranium}", True, (0, 0, 0))
        nuclear_meltdown_alert = font.render("MELTDOWN!", True, (255, 0, 0))
        uranium_neutral_alert = font.render("Uranium Neutral!", True, (0, 0, 0))
        uranium_deficit_alert = font.render("Uranium Deficit!", True, (255, 165, 0))
        uranium_surplus_alert = font.render("Uranium Surplus!", True, (0, 255, 0))
        screen.blit(uranium_count_text, (resources_x, resources_y + 180))
        if nuclear_meltdown == True:
            screen.blit(nuclear_meltdown_alert, (resources_x + 290, resources_y + 180))
        if uranium_deficit == True:
            screen.blit(uranium_deficit_alert, (resources_x + 290, resources_y + 180))
        if uranium_neutral == True:
            screen.blit(uranium_neutral_alert, (resources_x + 290, resources_y + 180))
        if uranium_surplus == True:
            screen.blit(uranium_surplus_alert, (resources_x + 290, resources_y + 180))

        wind_turbine_count_text = font.render(f"Wind Turbine Count: {wind_turbine_count}", True, (0, 0, 0))
        screen.blit(wind_turbine_count_text, (resources_x, resources_y + 240))

        if page == 1:
            #coal plant text
            coal_plant_info = extrasmall_font.render(f"Coal Plants: {coal_plant_count}", True, (0, 0, 0))
            coal_plant_cost_info = extrasmall_font.render(f"Cost: {coal_plant_cost}", True, (0, 0, 0))
            coal_cost = extrasmall_font.render("Coal Consumption: 1", True, (0, 0, 0))
            datacenter_info = extrasmall_font.render(f"Datacenters: {datacenter_count}", True, (0, 0, 0))
            datacenter_cost_info = extrasmall_font.render(f"Datacenter Cost: {datacenter_cost}", True, (0, 0, 0))
            coal_mine_count_info = extrasmall_font.render(f"Coal Mine Count {coal_mine_count}", True, (0, 0, 0))
            coal_mine_cost_info = extrasmall_font.render("Coal Mine Cost: 5", True, (0, 0, 0))
            datacenter_electricity = extrasmall_font.render(f"Electricty Cost: 1", True, (0, 0, 0))
            screen.blit(coal_plant_info, (140, 180))
            screen.blit(coal_plant_cost_info, (140, 210))
            screen.blit(coal_cost, (140, 240))
            screen.blit(coal_mine_count_info, (140, 300))
            screen.blit(coal_mine_cost_info, (140, 330))
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
            screen.blit(nuclear_reactor_img, nuclear_plant_rect)
            nuclear_reactor_info = extrasmall_font.render(f"Nuclear Plant: {nuclear_plant_count}", True, (0, 0, 0))
            nuclear_reactor_cost_info = extrasmall_font.render(f"Nuclear Plant Cost: {nuclear_reactor_cost}", True, (0, 0, 0))
            nuclear_reactor_upkeep = extrasmall_font.render(f"Uranium Consumption: 1", True, (0, 0, 0))
            screen.blit(nuclear_reactor_info, (140, 275))
            screen.blit(nuclear_reactor_cost_info, (140, 305))
            screen.blit(nuclear_reactor_upkeep, (140, 335))
        if menu_open:
            py.draw.rect(screen, (255, 255, 255), menu)
            py.draw.rect(screen, (0, 0, 0), menu, 5)

            menu_title = font.render("Parliment", True, (0, 0, 0))
            negative_influence_counter = font.render(f"Opposed: {apposed}", True, (0, 0, 0))
            positive_influence_counter = font.render(f"Supporting: {supporting}", True, (0, 0, 0))
            middile_eastern_nations_counter = font.render(f"Middile eastern nations: {middile_eastern_nations}", True, (0, 0, 0))
            deforestation_laws_counter = font.render(f"Deforestation laws: {deforestation_laws}/5", True, (0, 0, 0))
            exploited_african_nations_counter = font.render(f"Exploited african nations: {exploited_african_nations}", True, (0, 0, 0))
            screen.blit(menu_title, (menu.x + 20, menu.y + 20))
            screen.blit(middile_eastern_nations_counter, (menu.x + 20, menu.y + 240))
            screen.blit(deforestation_laws_counter, (menu.x + 20, menu.y + 280))
            screen.blit(exploited_african_nations_counter, (menu.x + 20, menu.y + 320))
            screen.blit(positive_influence_counter, (menu.x + 20, menu.y + 55))
            screen.blit(negative_influence_counter, (menu.x + 20, menu.y + 90))

            py.draw.rect(screen, (100, 200, 255), lobbying_button)
            py.draw.rect(screen, (0, 0, 0), lobbying_button, 2)
            py.draw.rect(screen, (100, 100, 255), war_button)
            py.draw.rect(screen, (0, 0, 0), war_button, 2)
            py.draw.rect(screen, (50, 255, 50), deforestation_law_button)
            py.draw.rect(screen, (0, 0, 0), deforestation_law_button, 2)
            py.draw.rect(screen, (255, 50, 50), exploit_african_nation_button)
            py.draw.rect(screen, (0, 0, 0), exploit_african_nation_button, 2)
            lobbying_text = button_text = extrasmall_font.render(f"Lobbying efforts: {lobbying_efforts}", True, (0, 0, 0))
            lobbying_text_rect = button_text.get_rect(center=lobbying_button.center)
            war_text = war_button_text = extrasmall_font.render("Invade middile eastern nation, requires 100 support", True, (0, 0, 0))
            war_text_rect = war_button_text.get_rect(center=war_button.center)
            deforestation_text = deforestation_button_text = extrasmall_font.render("Deforestation law, requires 10 support", True, (0, 0, 0))
            deforestation_text_rect = deforestation_text.get_rect(center=deforestation_law_button.center)
            exploit_africa_text = exploit_african_nation_button_text = extrasmall_font.render("Exploit african nation, requires 200 support", True, (0, 0, 0))
            exploit_african_nation_button_text_rect = exploit_africa_text.get_rect(center=exploit_african_nation_button.center)
            screen.blit(button_text, lobbying_text_rect)
            screen.blit(war_button_text, war_text_rect)
            screen.blit(deforestation_text, deforestation_text_rect)
            screen.blit(exploit_africa_text, exploit_african_nation_button_text_rect)
            py.draw.rect(screen, (255, 100, 100), menu_close_button)
            py.draw.rect(screen, (0, 0, 0), menu_close_button, 2)
            py.draw.line(screen, (0, 0, 0), (menu.x + 20, menu.y + 140), (menu.right - 20, menu.y + 140), 3)
            close_text = extrasmall_font.render("Close", True, (0, 0, 0))
            close_rect = close_text.get_rect(center=menu_close_button.center)
            screen.blit(close_text, close_rect)
        if information_open:
            py.draw.rect(screen, (255, 255, 255), information)
            py.draw.rect(screen, (0, 0, 0), information, 5)

            py.draw.rect(screen, (255, 100, 100), information_close_button)
            py.draw.rect(screen, (0, 0, 0), information_close_button, 2)
            information_close_text = extrasmall_font.render("Close", True, (0, 0, 0))
            information_close_rect = information_close_text.get_rect(center=information_close_button.center)
            screen.blit(information_close_text, information_close_rect)
            screen.blit(arrow_img, information_arrow_button_rect)
            screen.blit(other_arrow_img, information_other_arrow_button_rect)
            if information_page == 1:
                information_title_2 = font.render("Information: General", True, (0, 0, 0))
                general_information_1 = small_font.render("Victory: Victory is achived by reaching 100 environmental destruction", True, (0, 0, 0))
                general_information_2 = small_font.render("Defeat: You lose by your money going under 0", True, (0, 0, 0))
                general_information_3 = small_font.render("Money: You gain money through clicking the tree, or from buildings", True, (0, 0, 0))
                general_information_4 = small_font.render("Environmental Destruction: You gain environmental destruction from", True, (0, 0, 0))
                general_information_4_2 = small_font.render("buildings", True, (0, 0, 0))
                general_information_5 = small_font.render("Pop Up Events: Pop up events replace a certain number of your buildings or", True, (0, 0, 0))
                general_information_5_2 = small_font.render("none of them with wind turbines every 90 secconds, you can stop this by", True, (0, 0, 0))
                general_information_5_3 = small_font.render("paying $10000", True, (0, 0, 0))
                general_information_6 = small_font.render("Wind Turbines: Wind turbines make you lose money and decrease", True, (0, 0, 0))
                general_information_6_2 = small_font.render("environmental destruction", True, (0, 0, 0))
                screen.blit(information_title_2, (information.x + 20, information.y + 20))
                screen.blit(general_information_1, (information.x + 20, information.y + 60))
                screen.blit(general_information_2, (information.x + 20, information.y + 100))
                screen.blit(general_information_3, (information.x + 20, information.y + 140))
                screen.blit(general_information_4, (information.x + 20, information.y + 180))
                screen.blit(general_information_4_2, (information.x + 20, information.y + 200))
                screen.blit(general_information_5, (information.x + 20, information.y + 240))
                screen.blit(general_information_5_2, (information.x + 20, information.y + 260))
                screen.blit(general_information_5_3, (information.x + 20, information.y + 280))
                screen.blit(general_information_6, (information.x + 20, information.y + 320))
                screen.blit(general_information_6_2, (information.x + 20, information.y + 340))
            if information_page == 2:
                information_title_2 = font.render("Information: Buildings", True, (0, 0, 0))
                screen.blit(information_title_2, (information.x + 20, information.y + 20))
                information_coal_rect = coal_button_img.get_rect(topleft=(information.left + 10, information.top + 30))
                information_minecart_rect = minecart_img.get_rect(topleft=(information.left + 20, information.top + 180))
                information_datacenter_rect = datacenter_img.get_rect(topleft=(information.left + 20, information.top + 255))
                information_oil_rect = oil_refinery_img.get_rect(topleft=(information.left + 400, information.top + 30))
                information_nuclear_rect = nuclear_reactor_img.get_rect(topleft=(information.left + 400, information.top + 150))
                screen.blit(coal_button_img, information_coal_rect)
                screen.blit(minecart_img, information_minecart_rect)
                screen.blit(datacenter_button_img, information_datacenter_rect)
                screen.blit(oil_refinery_img, information_oil_rect)
                screen.blit(nuclear_reactor_img, information_nuclear_rect)
                building_information_1 = extrasmall_font.render("Coal Power Plant", True, (0, 0 ,0))
                building_information_1_2 = extrasmall_font.render("Causes 0.01 Environmental Destruction", True, (0, 0, 0))
                building_information_1_3 = extrasmall_font.render("per building", True, (0, 0, 0))
                building_information_1_4 = extrasmall_font.render("Produces 1 electricty", True, (0, 0, 0))
                screen.blit(building_information_1, (information.x + 140, information.y + 100))
                screen.blit(building_information_1_2, (information.x + 140, information.y + 120))
                screen.blit(building_information_1_3, (information.x + 140, information.y + 140))
                screen.blit(building_information_1_4, (information.x + 140, information.y + 160))
                building_information_2 = extrasmall_font.render("Coal Mine", True, (0, 0, 0))
                building_information_2_1 = extrasmall_font.render("Produces 1 coal", True, (0, 0, 0))
                screen.blit(building_information_2, (information.x + 140, information.y + 210))
                screen.blit(building_information_2_1, (information.x + 140, information.y + 240))
                building_information_3 = extrasmall_font.render("Datacenter", True, (0, 0, 0))
                building_information_3_1 = extrasmall_font.render("Causes 0.014 Environmental Destruction", True, (0, 0, 0))
                building_information_3_2 = extrasmall_font.render("Per building", True, (0, 0, 0))
                screen.blit(building_information_3, (information.x + 160, information.y + 295))
                screen.blit(building_information_3_1, (information.x + 160, information.y + 315))
                screen.blit(building_information_3_2, (information.x + 160, information.y + 335))
                building_information_4 = extrasmall_font.render("Oil Refinery", True, (0, 0, 0))
                building_information_4_1 = extrasmall_font.render("Causes 0.033 Environmental Destruction", True, (0, 0, 0))
                building_information_4_2 = extrasmall_font.render("Per building", True, (0, 0, 0))
                building_information_4_3 = extrasmall_font.render("Produces 10 electricty", True, (0, 0, 0))
                screen.blit(building_information_4, (information.x + 520, information.y + 80))
                screen.blit(building_information_4_1, (information.x + 520, information.y + 100))
                screen.blit(building_information_4_2, (information.x + 520, information.y + 120))
                screen.blit(building_information_4_3, (information.x + 520, information .y + 140))
                building_information_5 = extrasmall_font.render("Nuclear reactor", True, (0, 0, 0,))
                building_information_5_1 = extrasmall_font.render("Causes 0 environmental destruction", True, (0, 0, 0))
                building_information_5_2 = extrasmall_font.render("Per building", True, (0, 0, 0))
                building_information_5_3 = extrasmall_font.render("Produces 100 electricity", True, (0, 0, 0))
                screen.blit(building_information_5, (information.x + 500, information.y + 193))
                screen.blit(building_information_5_1, (information.x + 500, information.y + 213))
                screen.blit(building_information_5_2, (information.x + 500, information.y + 233))
                screen.blit(building_information_5_3, (information.x + 500, information .y + 253))
            if information_page == 3:
                information_title_3 = font.render("Information: Resources", True, (0, 0, 0))
                resource_information_1 = small_font.render("Resources: Some buildings require resources to run and will consume one of", True, (0, 0, 0))
                resource_information_1_2 = small_font.render("their specified resource per seccond", True, (0, 0, 0))
                resource_information_2 = small_font.render("Resources have 4 states; Surplus, neutral, deficit, and shortage", True, (0, 0, 0))
                resource_information_3 = small_font.render("Surplus: Gaining more resource than your using", True, (0, 0, 0))
                resource_information_3_2 = small_font.render("Neutral: Gaining same amount of resource as your using", True, (0, 0, 0))
                resource_information_3_3 = small_font.render("Deficit: Using more resource than youre gaining", True, (0, 0, 0))
                resource_information_3_4 = small_font.render("Shortage: Having 0 resources and still losing resources", True, (0, 0, 0))
                resource_information_4 = small_font.render("Being in a shortage will make you lose buildings until your neutral", True, (0, 0, 0))
                resource_information_5 = small_font.render("Being in a uranium shortage will trigger a meltdown", True, (0, 0, 0))
                resource_information_6 = small_font.render('Meltdowns: Meltdowns make you lose $100000 and all of your buildings',  True, (0, 0, 0))
                resource_information_6_2 = small_font.render("however they add 50 environmental destruction", True, (0, 0, 0))
                screen.blit(information_title_3, (information.x + 20, information.y + 20))
                screen.blit(resource_information_1, (information.x + 20, information.y + 60))
                screen.blit(resource_information_1_2, (information.x + 20, information.y + 80))
                screen.blit(resource_information_3, (information.x + 20, information.y + 120))
                screen.blit(resource_information_3_2, (information.x + 20, information.y + 160))
                screen.blit(resource_information_3_3, (information.x + 20, information.y + 200))
                screen.blit(resource_information_3_4, (information.x + 20, information.y + 240))
                screen.blit(resource_information_4, (information.x + 20, information.y + 280))
                screen.blit(resource_information_5, (information.x + 20, information.y + 320))
                screen.blit(resource_information_6, (information.x + 20, information.y + 360))
                screen.blit(resource_information_6_2, (information.x + 20, information.y + 380))
            if information_page == 4:
                information_title_4 = font.render("Information: Parliment", True, (0, 0, 0))
                information_parliment_rect = parliment_information_image.get_rect(topleft=(information.left + 440, information.top))
                screen.blit(parliment_information_image, information_parliment_rect)
                screen.blit(information_title_4, (information.x + 20, information.y + 20))
                parliment_information = small_font.render("Support and opposistion: There are 435 seats in parliment you need a certain", True, (0, 0, 0))
                parliment_information_2 = small_font.render("amount of support to perform certain things when performing them you lose", True, (0, 0, 0))
                parliment_information_2_2 = small_font.render("half of the support required to do them", True, (0, 0, 0))
                parliment_information_3 = small_font.render("Lobbying efforts: lobbying costs $1000 and adds 10 support immediatley this", True, (0, 0, 0))
                parliment_information_3_2 = small_font.render("can be repeated 44 times, on top of this every 100 secconds youll lose $1000", True, (0, 0, 0))
                parliment_information_3_3 = small_font.render("and gain 10 support", True, (0, 0, 0))
                parliment_information_4 = small_font.render("Deforestation Laws: Deforestation laws increase how much money you gain", True, (0, 0, 0))
                parliment_information_4_2 = small_font.render("from cicking the tree and can be stacked 5 times", True, (0, 0, 0))
                parliment_information_5 = small_font.render("Invade Middile Eastern Nation: Invading a middile eastern nations gives you", True, (0, 0, 0))
                parliment_information_5_2 = small_font.render("+1 oil per seccond and can be repeated infinitly", True, (0, 0, 0))
                parliment_information_6 = small_font.render("Exploit African Nation: Exploiting an african nations gives you +1 uranium", True, (0, 0, 0))
                parliment_information_6_2 = small_font.render("per seccond and can be repeated infinitly", True, (0, 0, 0))
                screen.blit(parliment_information, (information.x + 20, information.y + 85))
                screen.blit(parliment_information_2, (information.x + 20, information.y + 105))
                screen.blit(parliment_information_2_2, (information.x + 20, information.y + 125))
                screen.blit(parliment_information_3, (information.x + 20, information.y + 165))
                screen.blit(parliment_information_3_2, (information.x + 20, information.y + 185))
                screen.blit(parliment_information_3_3, (information.x + 20, information.y + 205))
                screen.blit(parliment_information_4, (information.x + 20, information.y + 245))
                screen.blit(parliment_information_4_2, (information.x + 20, information.y + 265))
                screen.blit(parliment_information_5, (information.x + 20, information.y + 305))
                screen.blit(parliment_information_5_2, (information.x + 20, information.y + 325))
                screen.blit(parliment_information_6, (information.x + 20, information.y + 365))
                screen.blit(parliment_information_6_2, (information.x + 20, information.y + 385))

        if save_open:
            py.draw.rect(screen, (255, 255, 255), save_menu)
            py.draw.rect(screen, (0, 0, 0), save_menu, 5)

            save_title = font.render("Save / Load", True, (0, 0, 0))
            screen.blit(save_title, (save_menu.x + 20, save_menu.y + 20))

            py.draw.rect(screen, (100, 255, 100), save_game_button)
            py.draw.rect(screen, (0, 0, 0), save_game_button, 2)
            save_game_text = extrasmall_font.render("Save Game", True, (0, 0, 0))
            save_game_rect = save_game_text.get_rect(center=save_game_button.center)
            screen.blit(save_game_text, save_game_rect)

            py.draw.rect(screen, (100, 200, 255), load_game_button)
            py.draw.rect(screen, (0, 0, 0), load_game_button, 2)
            load_game_text = extrasmall_font.render("Load Game", True, (0, 0, 0))
            load_game_rect = load_game_text.get_rect(center=load_game_button.center)
            screen.blit(load_game_text, load_game_rect)

            save_feedback_text = font.render(save_feedback, True, (0, 0, 0))
            screen.blit(save_feedback_text, (save_menu.x + 20, save_menu.y + 240))

            py.draw.rect(screen, (255, 100, 100), save_close_button)
            py.draw.rect(screen, (0, 0, 0), save_close_button, 2)
            close_text = extrasmall_font.render("Close", True, (0, 0, 0))
            close_rect = close_text.get_rect(center=save_close_button.center)
            screen.blit(close_text, close_rect)
        if pop_up_alert_open:
            py.draw.rect(screen, (255, 255, 255), pop_up_alert)
            py.draw.rect(screen, (0, 0, 0), pop_up_alert, 5)

            py.draw.rect(screen, (255, 100, 100), pop_up_close_button)
            py.draw.rect(screen, (0, 0, 0), pop_up_close_button, 2)
            pop_up_close_text = extrasmall_font.render("Replace Building", True, (0, 0, 0))
            pop_up_close_rect = pop_up_close_text.get_rect(center=pop_up_close_button.center)
            screen.blit(pop_up_close_text, pop_up_close_rect)

            py.draw.rect(screen, (100, 255, 100), pop_up_pay_button)
            py.draw.rect(screen, (0, 0, 0), pop_up_pay_button, 2)
            pop_up_pay_text = extrasmall_font.render("Lobby parliment, cost: 10000", True, (0, 0, 0))
            pop_up_pay_rect = pop_up_pay_text.get_rect(center=pop_up_pay_button.center)
            screen.blit(pop_up_pay_text, pop_up_pay_rect)

            alert_title = font.render(f"Parliment demands {removed_count} {replaced_building}", True, (0, 0, 0))
            alert_info = font.render("replaced with wind turbines", True, (0, 0, 0))
            alert_timer = font.render(f"You have {pop_up_alert_timer} seconds to respond", True, (0, 0, 0))
            screen.blit(alert_title, (pop_up_alert.x + 20, pop_up_alert.y + 20))
            screen.blit(alert_info, (pop_up_alert.x + 20, pop_up_alert.y + 50))
            screen.blit(alert_timer, (pop_up_alert.x + 20, pop_up_alert.y + 80))
    py.display.flip()
    clock.tick(configs.CLOCK_SPEED)

py.quit()
sys.exit()
