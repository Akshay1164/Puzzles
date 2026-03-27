'''Simulate the 100 prisoners problem where each prisoner follows the cycle strategy to find their number in boxes. The simulation runs 
multiple trials to estimate the probability of all prisoners succeeding. '''
import random

NUM_PRISONERS = 100
MAX_OPENS = 50
TRIALS = 10000


def single_trial():
    # Step 1: Create random permutation of numbers 1..100
    boxes = list(range(1, NUM_PRISONERS + 1))
    random.shuffle(boxes)

    # Step 2: Each prisoner follows cycle strategy
    for prisoner in range(1, NUM_PRISONERS + 1):
        current_box = prisoner
        found = False

        for _ in range(MAX_OPENS):
            number_inside = boxes[current_box - 1]
            if number_inside == prisoner:
                found = True
                break
            current_box = number_inside

        if not found:
            return False  # One prisoner failed → everyone fails

    return True  # All prisoners succeeded


def simulate():
    success = 0

    for _ in range(TRIALS):
        if single_trial():
            success += 1

    probability = success / TRIALS
    print(f"Trials: {TRIALS}")
    print(f"Successful escapes: {success}")
    print(f"Estimated probability: {probability:.4f}")


if __name__ == "__main__":
    simulate()
