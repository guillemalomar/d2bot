from configuration.configuration_parameters import difficulty, mode, max_iterations_travincal, max_iterations_anya
from modules import actions_general, actions_act3, interaction, actions_act5
from modules.actions_general import found_loot


def log_state(iteration):
    print(f"Iteration: {iteration + 1}")

if __name__ == "__main__":
    if mode == "travincal":
        current_iteration = 0
        while current_iteration < max_iterations_travincal:
            log_state(current_iteration)
            try:
                actions_general.start_game(difficulty)
                interaction.check_if_started()
                actions_general.retrieve_corpse()
                actions_act3.go_to_stash()
                actions_general.save_in_stash()
                actions_act3.go_to_travincal()
                interaction.check_if_started()
                # actions_act3.travincal_teleports()
                # actions_general.kill()
                # actions_general.pickup_loot()
                # actions_general.go_to_main_screen()
            except Exception:
                print("Error found, restarting travincal")
            print(f"Found loot: \n {found_loot}")
            current_iteration += 1
    elif mode == "anya":
        while True:
            try:
                actions_general.start_game(difficulty)
                interaction.check_if_started()
                actions_act5.go_to_stash_from_start()
                actions_general.save_in_stash()
                actions_act5.go_to_anya_portal_from_stash()
                current_iteration = 0
                while current_iteration < max_iterations_anya:
                    log_state(current_iteration)
                    actions_act5.go_to_anya_portal_and_back()
                    actions_act5.go_to_anya()
                    current_iteration += 1
            except Exception:
                print("Error found, restarting anya")
