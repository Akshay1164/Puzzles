def bridge_and_torch(times):
    times.sort()
    total_time = 0
    steps = []

    while len(times) > 3:
        a = times[0]
        b = times[1]
        y = times[-2]
        z = times[-1]

        # Two strategies
        strategy1 = a + z + a + y
        strategy2 = a + b + z + b

        if strategy1 <= strategy2:
            # Strategy 1
            steps.append(f"{a} & {z} cross → {z}")
            total_time += z

            steps.append(f"{a} returns → {a}")
            total_time += a

            steps.append(f"{a} & {y} cross → {y}")
            total_time += y

            steps.append(f"{a} returns → {a}")
            total_time += a
        else:
            # Strategy 2 (optimal here)
            steps.append(f"{a} & {b} cross → {b}")
            total_time += b

            steps.append(f"{a} returns → {a}")
            total_time += a

            steps.append(f"{y} & {z} cross → {z}")
            total_time += z

            steps.append(f"{b} returns → {b}")
            total_time += b

        # Remove the two slowest
        times.pop()
        times.pop()

    # Final handling
    if len(times) == 3:
        a, b, c = times
        steps.append(f"{a} & {b} cross → {b}")
        total_time += b

        steps.append(f"{a} returns → {a}")
        total_time += a

        steps.append(f"{a} & {c} cross → {c}")
        total_time += c

    elif len(times) == 2:
        steps.append(f"{times[0]} & {times[1]} cross → {times[1]}")
        total_time += times[1]

    return total_time, steps
times = [1, 2, 7, 10]
total, steps = bridge_and_torch(times)

print("Steps:")
for step in steps:
    print(step)

print("\nTotal Time:", total)
