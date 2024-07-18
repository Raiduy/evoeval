def find_legendary_item(player_input):
    if not player_input:
        return (False, None)
    if 5 in player_input:
        sorted_items = sorted(player_input, reverse=True)
        legendary_index = sorted_items.index(5)
        if legendary_index == 0:
            return (True, -1)
        else:
            return (True, sorted_items[legendary_index - 1])
    else:
        return (False, None)