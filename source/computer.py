import random

def pon():
    hand = random.randint(1, 3)
    if hand == 1:
       return "グー"
    elif hand == 2:
        return "チョキ"
    else:
        return "パー"