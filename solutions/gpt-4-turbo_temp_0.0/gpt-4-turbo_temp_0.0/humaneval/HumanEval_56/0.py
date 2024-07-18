

def correct_bracketing(brackets: str) -> bool:
    counter = 0
    for bracket in brackets:
        if bracket == "<":
            counter += 1
        elif bracket == ">":
            counter -= 1
        # If counter goes below zero, it means there's a closing bracket without an opening
        if counter < 0:
            return False
    # If counter is zero, all brackets are correctly paired
    return counter == 0
