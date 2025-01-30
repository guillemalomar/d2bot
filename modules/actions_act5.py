from modules.actions_general import found_loot
from modules.interaction import click, move_mouse, check_if_started
from configuration.click_locations_act5 import (
    stash_from_start,
    anya_portal_from_stash,
    anya_portal_open,
    anya_portal_back,
    anya_from_portal,
)
from modules.screen_analyzer import take_screenshot, detect_loot, find_vendor_good_loot


def go_to_stash_from_start():
    for location in stash_from_start:
        click(x=location[0], y=location[1], time_low=3, time_high=4)

def go_to_anya_portal_from_stash():
    for location in anya_portal_from_stash:
        click(x=location[0], y=location[1], time_low=3, time_high=4)

def go_to_anya_portal_and_back():
    move_mouse(anya_portal_open[0], anya_portal_open[1])
    click()
    check_if_started()
    move_mouse(anya_portal_back[0], anya_portal_back[1])
    click()
    check_if_started()

def go_to_anya_and_check_her_stuff():
    move_mouse(anya_from_portal[0], anya_from_portal[1])
    click()
    for x_position in range(150, 1500, 80):  # placeholder, needs to be calculated
        for y_position in range(150, 1500, 80):  # placeholder, needs to be calculated
            screenshot = take_screenshot()
            loot_locations = detect_loot(screenshot)
            if find_vendor_good_loot(loot_locations):
                click(x=x_position, y=y_position, button="right")
