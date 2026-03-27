import random
import time

class Bulb:
    def __init__(self):
        self.is_on = False
        self.temperature = "cold"

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        if self.is_on:
            self.temperature = "warm"
        self.is_on = False


class SwitchPuzzle:
    def __init__(self):
        # Randomly assign which switch controls the bulb
        self.correct_switch = random.randint(1, 3)
        self.bulb = Bulb()
        print(f"(Hidden) Bulb is connected to Switch {self.correct_switch}")

    def toggle(self, switch_number, state):
        if switch_number == self.correct_switch:
            if state == "on":
                self.bulb.turn_on()
            else:
                self.bulb.turn_off()

    def wait(self):
        # Simulate time passing
        time.sleep(1)  # symbolic wait

    def enter_room(self):
        return self.bulb.is_on, self.bulb.temperature


def solve_puzzle():
    puzzle = SwitchPuzzle()

    # Step 1: Turn ON switch 1
    puzzle.toggle(1, "on")
    puzzle.wait()

    # Step 2: Turn OFF switch 1
    puzzle.toggle(1, "off")

    # Step 3: Turn ON switch 3
    puzzle.toggle(3, "on")

    # Step 4: Enter room (only once)
    is_on, temperature = puzzle.enter_room()

    print("\n--- Inside the Room ---")
    print(f"Bulb ON: {is_on}")
    print(f"Bulb Temperature: {temperature}")

    # Deduction
    if is_on:
        print("👉 Switch 3 controls the bulb")
    elif temperature == "warm":
        print("👉 Switch 1 controls the bulb")
    else:
        print("👉 Switch 2 controls the bulb")


if __name__ == "__main__":
    solve_puzzle()
