import random

class Person:
    def __init__(self, name, is_hero=False):
        self.name = name
        self.is_hero = is_hero

    def answer(self, people):
        """
        Everyone is asked: 'Who is the hero?'
        """
        if self.is_hero:
            # Hero tells the truth
            return self.name
        else:
            # Villain lies: never says the real hero
            choices = [p.name for p in people if not p.is_hero]
            return random.choice(choices)


def find_hero_one_move(people):
    """
    Finds the hero in one move
    """
    print("Asking everyone: 'Who is the hero?'\n")

    responses = {}

    for person in people:
        response = person.answer(people)
        responses[person.name] = response
        print(f"{person.name} says: {response}")

    print("\nResult:")
    for name, response in responses.items():
        if name == response:
            print(f"✅ HERO FOUND: {name}")
            return name

    print("❌ Hero not found")
    return None


# ---------------- MAIN ----------------
if __name__ == "__main__":
    names = ["A", "B", "C", "D", "E"]

    # Randomly select hero
    hero_name = random.choice(names)

    people = []
    for name in names:
        people.append(Person(name, is_hero=(name == hero_name)))

    print("People:", names)
    print("(Hidden) Actual Hero:", hero_name)
    print("-" * 40)

    find_hero_one_move(people)
