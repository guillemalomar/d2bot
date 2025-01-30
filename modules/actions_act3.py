from modules.interaction import click, move_mouse
from configuration.click_locations_act3 import (
    act_three_stash,
    act_three_stash_open,
    act_three_waypoint_from_stash,
    travincal_waypoint_click,
    travincal_teleports,
)

def go_to_stash_and_open():
    for location in act_three_stash:
        click(x=location[0], y=location[1], time_low=3, time_high=4)
    move_mouse(act_three_stash_open[0], act_three_stash_open[1])
    click(time_low=1, time_high=2)

def go_to_travincal():
    move_mouse(act_three_waypoint_from_stash[0], act_three_waypoint_from_stash[1])
    click()
    click(x=travincal_waypoint_click[0], y=travincal_waypoint_click[1])

def go_to_council():
    for location in travincal_teleports:
        click(x=location[0], y=location[1])