def find_legendary_item(player_input):
    if 5 in player_input:
        player_input.remove(5)
        if player_input:
            return (True, max(player_input))
        else:
            return (True, -1)
    else:
        return (False, None)