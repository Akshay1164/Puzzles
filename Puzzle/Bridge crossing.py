'''Send the two fastest first to set up torch shuttling, then send the two slowest together, minimizing slow crossings.'''
def bridge_and_torch():
    # Crossing times
    times = {
        "A": 1,
        "B": 2,
        "C": 7,
        "D": 10
    }

    total_time = 0
    steps = []

    # Step 1: A & B cross
    steps.append(("A", "B"))
    total_time += max(times["A"], times["B"])

    # Step 2: A returns
    steps.append(("A",))
    total_time += times["A"]

    # Step 3: C & D cross
    steps.append(("C", "D"))
    total_time += max(times["C"], times["D"])

    # Step 4: B returns
    steps.append(("B",))
    total_time += times["B"]

    # Step 5: A & B cross
    steps.append(("A", "B"))
    total_time += max(times["A"], times["B"])

    # Output
    print("Bridge and Torch Solution")
    print("-" * 40)

    for i, step in enumerate(steps, 1):
        if len(step) == 2:
            print(f"Step {i}: {step[0]} and {step[1]} cross "
                  f"(time = {max(times[step[0]], times[step[1]])})")
        else:
            print(f"Step {i}: {step[0]} returns "
                  f"(time = {times[step[0]]})")

    print("-" * 40)
    print("Minimum total time:", total_time, "minutes")


# Run the program
if __name__ == "__main__":
    bridge_and_torch()
