'''This script simulates the classic "Poisoned Bottle" puzzle, 
where 10 prisoners are used to identify one poisoned bottle among 1000 bottles using binary representation. 
Each prisoner drinks from a specific combination of bottles, and after a certain period, the dead prisoners indicate which bottle is poisoned.'''

import random

# -----------------------------
# Step 1: Decode function
# -----------------------------
def find_poisoned_bottle(dead_prisoners):
    """
    dead_prisoners: list of prisoner numbers (1 to 10) who died
    returns: poisoned bottle number
    """
    bottle_number = 0
    for prisoner in dead_prisoners:
        bottle_number += 2 ** (prisoner - 1)
    return bottle_number


# -----------------------------
# Step 2: Simulation
# -----------------------------
def simulate_poison_test():
    """
    Simulates the poisoned bottle experiment
    """
    poisoned_bottle = random.randint(1, 1000)
    dead_prisoners = []

    # Each prisoner corresponds to a bit
    for prisoner in range(1, 11):
        if poisoned_bottle & (1 << (prisoner - 1)):
            dead_prisoners.append(prisoner)

    return poisoned_bottle, dead_prisoners


# -----------------------------
# Step 3: Main Execution
# -----------------------------
def main():
    print("Poisoned Bottle Puzzle Simulation")
    print("-" * 40)

    actual_bottle, dead_prisoners = simulate_poison_test()
    decoded_bottle = find_poisoned_bottle(dead_prisoners)

    print("Dead prisoners (bit positions):", dead_prisoners)
    print("Actual poisoned bottle:", actual_bottle)
    print("Decoded poisoned bottle:", decoded_bottle)

    if actual_bottle == decoded_bottle:
        print("✅ SUCCESS: Bottle identified correctly!")
    else:
        print("❌ ERROR: Something went wrong.")


# -----------------------------
# Run program
# -----------------------------
if __name__ == "__main__":
    main()
