from modules.interaction import click, move_mouse, keyboard_press
from configuration.click_locations_mode1 import (
    act_three_stash,
    act_three_waypoint_from_stash,
    travincal_waypoint_click,
    travincal_teleports,
    travincal_last_teleport_location,
)

def go_to_stash():
    for location in act_three_stash:
        click(x=location[0], y=location[1], time_low=4, time_high=5)

def go_to_travincal():
    move_mouse(act_three_waypoint_from_stash[0], act_three_waypoint_from_stash[1])
    click()
    click(x=travincal_waypoint_click[0], y=travincal_waypoint_click[1])

def go_to_council():
    keyboard_press("f2")  # teleport
    for location in travincal_teleports:
        click(x=location[0], y=location[1], time_low=1, time_high=2, button="right")

def travincal_last_teleport():
    keyboard_press("f2")  # teleport
    click(x=travincal_last_teleport_location[0], y=travincal_last_teleport_location[1], time_low=1, time_high=2, button="right")
