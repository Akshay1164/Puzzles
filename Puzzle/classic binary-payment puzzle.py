'''This code solves the classic puzzle of paying an employee with a gold rod
over a series of days using the minimum number of cuts. The rod is cut into'''

def optimized_gold_payment(days=7):
    pieces = [1, 2, 4]   # after 2 cuts
    employee = set()

    for day in range(1, days + 1):
        required = set()
        remaining = day

        # Binary-style greedy selection
        for p in reversed(pieces):
            if p <= remaining:
                required.add(p)
                remaining -= p

        # Update employee holdings
        employee = required

        print(f"Day {day}: Rods = {sorted(employee)}, Total = {sum(employee)}")


optimized_gold_payment()
