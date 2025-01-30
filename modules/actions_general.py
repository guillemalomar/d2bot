import random
import time

from configuration.configuration_loot_act3 import good_loot
from modules.interaction import click, keyboard_press, control_click, move_mouse
from configuration.click_locations_general import (
    menu_first_char,
    menu_normal_difficulty,
    menu_nightmare_difficulty,
    menu_hell_difficulty,
    corpse_location,
    stash_open,
    char_gold_deposit,
    char_gold_deposit_confirm,
    tab1, tab2, tab3, tab4,
    inventory_slots,
    exit_location,
    play_button,
)
from modules.screen_analyzer import take_screenshot, detect_loot, find_good_loot

found_loot = {}
for entry in good_loot:
    found_loot[entry] = 0

def start_game(difficulty):
    click(x=menu_first_char[0], y=menu_first_char[1])
    click(x=play_button[0], y=play_button[1])
    match difficulty:
        case "normal":
            click(x=menu_normal_difficulty[0], y=menu_normal_difficulty[1])
        case "nightmare":
            click(x=menu_nightmare_difficulty[0], y=menu_nightmare_difficulty[1])
        case "hell":
            click(x=menu_hell_difficulty[0], y=menu_hell_difficulty[1])

def retrieve_corpse():
    move_mouse(corpse_location[0], corpse_location[1])
    click(time_low=1, time_high=2)

def save_in_stash():
    move_mouse(stash_open[0], stash_open[1])
    click(time_low=1, time_high=2)
    save_gold()
    save_inventory()
    close_stash()

def save_gold():
    click(x=tab2[0], y=tab2[1])
    click(x=char_gold_deposit[0], y=char_gold_deposit[1])
    click(x=char_gold_deposit_confirm[0], y=char_gold_deposit_confirm[1])
    click(x=tab3[0], y=tab3[1])
    click(x=char_gold_deposit[0], y=char_gold_deposit[1])
    click(x=char_gold_deposit_confirm[0], y=char_gold_deposit_confirm[1])
    click(x=tab4[0], y=tab4[1])
    click(x=char_gold_deposit[0], y=char_gold_deposit[1])
    click(x=char_gold_deposit_confirm[0], y=char_gold_deposit_confirm[1])

def save_inventory():
    click(x=tab1[0], y=tab1[1])
    random.shuffle(inventory_slots)
    for slot in inventory_slots:
        control_click(x=slot[0], y=slot[1])

def close_stash():
    keyboard_press("esc")

def kill():
    keyboard_press("f1")  # hammers
    current_attacks = 0
    while current_attacks < 10:
        click(button="right")
        time.sleep(random.uniform(1, 1.5))
    keyboard_press("f2")  # teleport

def pickup_loot():
    done_with_loot = False
    while not done_with_loot:
        screenshot = take_screenshot()
        loot_locations = detect_loot(screenshot)
        found_good_loot = find_good_loot(loot_locations)
        if found_good_loot:
            click(x=found_good_loot[0]["x"], y=found_good_loot[0]["y"])
            found_loot[found_good_loot[0]["name"]] += 1
        else:
            done_with_loot = True

def go_to_main_screen():
    keyboard_press("esc")
    click(x=exit_location[0], y=exit_location[1])
