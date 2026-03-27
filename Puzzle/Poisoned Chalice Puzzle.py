''' the poisoned chalice puzzle simulation where prisoners use binary coding to identify the poisoned chalice.
Each prisoner drinks from a specific combination of chalices, and after a certain period, the dead prisoners indicate which chalice is poisoned.'''

import random

# Number of chalices and prisoners
NUM_CHALICES = 8
NUM_PRISONERS = 3


def to_binary(n, bits):
    """Convert number to binary string with fixed bits"""
    return format(n, f'0{bits}b')


def simulate_poisoned_chalice():
    # Step 1: Label chalices with binary codes
    chalice_labels = {i + 1: to_binary(i, NUM_PRISONERS) for i in range(NUM_CHALICES)}

    # Step 2: Randomly choose poisoned chalice
    poisoned_chalice = random.randint(1, NUM_CHALICES)

    print("Chalice Labels (Binary):")
    for k, v in chalice_labels.items():
        print(f"Chalice {k}: {v}")

    print(f"\n(Hidden) Poisoned Chalice: {poisoned_chalice}")
    print("-" * 40)

    # Step 3: Determine who drinks from the poisoned chalice
    deaths = [0] * NUM_PRISONERS  # 0 = alive, 1 = dead
    binary_code = chalice_labels[poisoned_chalice]

    for i in range(NUM_PRISONERS):
        if binary_code[NUM_PRISONERS - 1 - i] == '1':
            deaths[i] = 1  # prisoner dies

    # Step 4: Display prisoner outcomes
    print("Prisoner Outcomes:")
    for i, d in enumerate(deaths, start=1):
        status = "Dead" if d == 1 else "Alive"
        print(f"Prisoner {i}: {status}")

    # Step 5: Decode result
    decoded_binary = ''.join(str(deaths[NUM_PRISONERS - 1 - i]) for i in range(NUM_PRISONERS))
    decoded_chalice = int(decoded_binary, 2) + 1

    print("\nDecoded Binary:", decoded_binary)
    print("Identified Poisoned Chalice:", decoded_chalice)

    # Final verification
    print("\n✅ Correct!" if decoded_chalice == poisoned_chalice else "❌ Error")


if __name__ == "__main__":
    simulate_poisoned_chalice()
