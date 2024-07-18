def find_legendary_item(player_input):
    if 5 in player_input:
        player_input.remove(5)
        if not player_input:
            return (True, -1)
        return (True, max(player_input))
    return (False, None)