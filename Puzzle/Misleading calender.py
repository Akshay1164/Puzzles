days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

# Helper functions
def yesterday(day):
    return days[(days.index(day) - 1) % 7]

def tomorrow(day):
    return days[(days.index(day) + 1) % 7]

# Statements
def A(day):
    return day == "Monday"

def B(day):
    return tomorrow(day) == "Sunday"

def C(day):
    return yesterday(day) == "Thursday"


# Check each day
for day in days:
    statements = [A(day), B(day), C(day)]

    if all(statements):
        print(f"✅ Truth day found: {day}")
    elif not any(statements):
        print(f"🤥 Lying day found: {day}")
