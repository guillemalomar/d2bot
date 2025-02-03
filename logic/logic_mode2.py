from configuration import difficulty, max_iterations_2
from modules import actions_general, actions_mode2, interaction

def act_5_iteration():
    actions_general.start_game(difficulty)
    interaction.check_if_started()
    actions_mode2.go_to_stash_from_start()
    actions_general.save_in_stash()
    actions_mode2.go_to_anya_portal_from_stash()
    current_iterations = 0
    while current_iterations < max_iterations_2:
        actions_mode2.go_to_anya_portal_and_back()
        actions_mode2.go_to_anya_and_check_her_stuff()
        current_iterations += 1
    actions_general.go_to_main_screen()
    interaction.check_if_started()
