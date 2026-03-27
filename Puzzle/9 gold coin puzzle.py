import random

NORMAL = 100

def weigh(left, right, weights):
    lw = sum(weights[c] for c in left)
    rw = sum(weights[c] for c in right)
    if lw > rw:
        return "LEFT"
    elif lw < rw:
        return "RIGHT"
    else:
        return "EQUAL"


def solve_9_coin_puzzle():
    coins = list(range(1, 10))
    weights = {c: NORMAL for c in coins}

    fake_coin = random.choice(coins)
    fake_type = random.choice(["HEAVY", "LIGHT"])
    weights[fake_coin] = 101 if fake_type == "HEAVY" else 99

    print(f"(Hidden) Fake coin: {fake_coin}, Type: {fake_type}")
    print("-" * 50)

    A = [1, 2, 3]
    B = [4, 5, 6]
    C = [7, 8, 9]

    # Weighing 1
    w1 = weigh(A, B, weights)
    print(f"Weighing 1 (A vs B): {w1}")

    # CASE 1: Fake in C
    if w1 == "EQUAL":
        w2 = weigh([7], [8], weights)
        print(f"Weighing 2 (7 vs 8): {w2}")

        if w2 == "EQUAL":
            detected_coin = 9
            detected_type = "HEAVY or LIGHT"
        elif w2 == "LEFT":
            detected_coin = 7
            detected_type = "HEAVY"
        else:
            detected_coin = 7
            detected_type = "LIGHT"

    # CASE 2: Fake in A or B
    else:
        # Compare 1 from A + 1 from B vs two known-good coins
        w2 = weigh([1, 4], [7, 8], weights)
        print(f"Weighing 2 (1+4 vs 7+8): {w2}")

        if w1 == "LEFT":  # A > B
            if w2 == "LEFT":
                detected_coin = 1
                detected_type = "HEAVY"
            elif w2 == "RIGHT":
                detected_coin = 4
                detected_type = "LIGHT"
            else:
                detected_coin = 2 if weights[2] != NORMAL else 3
                detected_type = fake_type
        else:  # B > A
            if w2 == "LEFT":
                detected_coin = 4
                detected_type = "HEAVY"
            elif w2 == "RIGHT":
                detected_coin = 1
                detected_type = "LIGHT"
            else:
                detected_coin = 5 if weights[5] != NORMAL else 6
                detected_type = fake_type

    print(f"\nDetected fake coin: {detected_coin}")
    print(f"Detected type: {detected_type}")

    print("\nVerification:")
    if detected_coin == fake_coin:
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")


if __name__ == "__main__":
    solve_9_coin_puzzle()
