def space_invaders(aliens, ray):
    aliens.sort()
    remaining_aliens = []
    for alien in aliens:
        if alien % 2 == 1 and abs(alien - ray) > 1:
            remaining_aliens.append(alien)
    return remaining_aliens