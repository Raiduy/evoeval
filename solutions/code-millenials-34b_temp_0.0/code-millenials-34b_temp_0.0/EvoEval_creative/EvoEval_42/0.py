def find_legendary_item(player_input):
    legendary_acquired = False
    second_most_valuable_item = None
    for item in player_input:
        if item == 5:
            legendary_acquired = True
        elif not legendary_acquired and (second_most_valuable_item is None or item > second_most_valuable_item):
            second_most_valuable_item = item
    return (legendary_acquired, second_most_valuable_item if not legendary_acquired else -1)