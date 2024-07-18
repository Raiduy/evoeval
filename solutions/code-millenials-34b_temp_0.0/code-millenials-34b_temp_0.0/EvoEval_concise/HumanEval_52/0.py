

def below_threshold(l: list, t: int) -> bool:
    for i in l:
        if i >= t:
            return False
    return True