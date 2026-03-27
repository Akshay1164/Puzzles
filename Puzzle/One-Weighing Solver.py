'''This script identifies a fake machine among five identical machines based on a single weighing.'''

def find_fake_machine(measured_weight):
    expected_weight = 1500
    difference = expected_weight - measured_weight

    if 1 <= difference <= 5:
        return f"Machine {difference} is fake"
    return "No fake machine detected"


# Example usage
measured = 1497  # suppose scale shows this
print(find_fake_machine(measured))
