from configuration import mode, max_restarts_1, max_restarts_2
from configuration.available_modes import modes
from logic import logic_mode1, logic_mode2
from modules.actions_general import found_loot


def log_state(iteration):
    print(f"Iteration: {iteration + 1}")

def log_loot():
    print(f"Found loot: \n {found_loot}")

if __name__ == "__main__":
    current_restarts = 0
    if mode == 1:
        while current_restarts < max_restarts_1:
            log_state(current_restarts)
            try:
                logic_mode1.mode1_iteration()
            except Exception as exc:
                print(f"Error found, restarting {modes[mode]}: {exc}")
            log_loot()
            current_restarts += 1
    elif mode == 2:
        while current_restarts < max_restarts_2:
            log_state(current_restarts)
            try:
                logic_mode2.act_5_iteration()
            except Exception as exc:
                print(f"Error found, restarting {modes[mode]}: {exc}")
            current_restarts += 1
    else:
        print(f"Choose a mode available in {modes}")
