from configuration_parameters import difficulty, mode, max_iterations
from modules import actions_general, actions_act3, interaction

def log_state(iteration):
    print(f"Iteration: {iteration + 1}")

current_iteration = 0
while current_iteration < max_iterations:
    log_state(current_iteration)
    actions_general.start_game(difficulty)
    interaction.check_if_started()
    actions_general.retrieve_corpse()
    if mode == "travincal":
        actions_act3.go_to_stash_and_open()
        actions_general.save_gold()
        actions_general.save_inventory()
        actions_general.close_stash()
        actions_act3.go_to_travincal()
        interaction.check_if_started()
        # actions_act3.travincal_teleports()
    # actions_general.kill()
    # actions_general.pickup_loot()
    # actions_general.go_to_main_screen()
    current_iteration += 1