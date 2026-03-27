import random

def simulate():
    doors = ["Left", "Right"]
    freedom_door = random.choice(doors)

    # Assign guards
    guards = {
        "truth": True,
        "liar": False
    }

    # Randomly choose which guard you ask
    asked_guard = random.choice(list(guards.keys()))
    other_guard = "liar" if asked_guard == "truth" else "truth"

    print(f"Freedom door is: {freedom_door}")
    print(f"You asked the: {asked_guard} guard")

    # What would the other guard say?
    if guards[other_guard]:  # truth teller
        other_guard_answer = freedom_door
    else:  # liar
        other_guard_answer = "Left" if freedom_door == "Right" else "Right"

    # Asked guard answers the question
    if guards[asked_guard]:  # truth teller
        heard_answer = other_guard_answer
    else:  # liar
        heard_answer = "Left" if other_guard_answer == "Right" else "Right"

    print(f"Guard points to: {heard_answer}")

    # You choose the opposite
    chosen_door = "Left" if heard_answer == "Right" else "Right"
    print(f"You choose: {chosen_door}")

    if chosen_door == freedom_door:
        print("✅ You are FREE!\n")
    else:
        print("❌ You are doomed!\n")

# Run multiple times
for _ in range(5):
    simulate()
'''This code solves the classic puzzle of paying an employee with a gold rod    over a series of days using the minimum number of cuts. The rod is cut into'''