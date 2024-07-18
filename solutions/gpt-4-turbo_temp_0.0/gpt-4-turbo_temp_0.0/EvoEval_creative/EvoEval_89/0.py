def space_invaders(aliens, ray):
    remaining_aliens = []
    for position in aliens:
        if position == ray or position == ray - 1 or position == ray + 1:
            continue
        else:
            remaining_aliens.append(position)
    return remaining_aliens