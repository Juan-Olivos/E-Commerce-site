def process_payment(order):
    import random

    if random.randint(1, 3) == 3:
        return False
    return True
