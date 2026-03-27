'''12 balls, one is fake (heavier or lighter). Find the fake ball in 3 weighings.
The fake ball can be either light or heavy'''

def weigh(left, right, fake_ball, fake_type):
    """
    Simulates a balance weighing.
    """
    def weight(ball):
        if ball == fake_ball:
            return 99 if fake_type == "light" else 101
        return 100

    left_weight = sum(weight(b) for b in left)
    right_weight = sum(weight(b) for b in right)

    if left_weight > right_weight:
        return "left"
    elif left_weight < right_weight:
        return "right"
    else:
        return "equal"


def find_fake_ball(fake_ball, fake_type):
    balls = list(range(1, 13))

    # ---------- WEIGHING 1 ----------
    w1 = weigh([1,2,3,4], [5,6,7,8], fake_ball, fake_type)

    # CASE 1: Balanced
    if w1 == "equal":
        # fake is in 9,10,11,12
        w2 = weigh([9,10,11], [1,2,3], fake_ball, fake_type)

        if w2 == "equal":
            # ball 12 is fake
            w3 = weigh([12], [1], fake_ball, fake_type)
            nature = "heavy" if w3 == "left" else "light"
            return 12, nature

        else:
            # fake is in 9,10,11
            w3 = weigh([9], [10], fake_ball, fake_type)
            if w3 == "equal":
                return 11, fake_type
            return (9 if w3 == "left" else 10), fake_type

    # CASE 2: Unbalanced
    else:
        heavy_side = [1,2,3,4] if w1 == "left" else [5,6,7,8]
        light_side = [5,6,7,8] if w1 == "left" else [1,2,3,4]

        w2 = weigh([heavy_side[0], heavy_side[1], light_side[0]],
                   [heavy_side[2], 9, 10],
                   fake_ball, fake_type)

        if w2 == "equal":
            # heavy_side[3] or light_side[1]
            w3 = weigh([heavy_side[3]], [9], fake_ball, fake_type)
            if w3 != "equal":
                return heavy_side[3], "heavy"
            return light_side[1], "light"

        elif w2 == "left":
            # heavy_side[0] heavy OR light_side[0] light
            w3 = weigh([heavy_side[0]], [9], fake_ball, fake_type)
            if w3 == "left":
                return heavy_side[0], "heavy"
            return light_side[0], "light"

        else:
            # heavy_side[1] heavy OR heavy_side[2] heavy
            w3 = weigh([heavy_side[1]], [heavy_side[2]], fake_ball, fake_type)
            if w3 == "left":
                return heavy_side[1], "heavy"
            return heavy_side[2], "heavy"


# ---------- TEST ----------
ball, nature = find_fake_ball(fake_ball=7, fake_type="light")
print(f"Fake ball is: {ball}, Nature: {nature}")
