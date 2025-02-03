from configuration import difficulty
from modules import actions_general, actions_mode1, interaction

def mode1_iteration():
    actions_general.start_game(difficulty)
    interaction.check_if_started()
    actions_general.retrieve_corpse()
    actions_mode1.go_to_stash()
    actions_general.save_in_stash()
    actions_mode1.go_to_travincal()
    interaction.check_if_started()
    actions_mode1.go_to_council()
    actions_general.kill()
    actions_mode1.travincal_last_teleport()
    actions_general.kill()
    actions_general.pickup_loot()
    actions_general.go_to_main_screen()
    interaction.check_if_started()
