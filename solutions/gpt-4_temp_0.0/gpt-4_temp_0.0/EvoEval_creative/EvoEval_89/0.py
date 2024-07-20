def space_invaders(aliens, ray):
    """
    A space invader game is being designed. There are n aliens represented by an array where each alien is at a certain position. 
    You are given a ray gun that can destroy an alien at a position in one shot. But the ray gun can also destroy all 
    the aliens in the positions adjacent to it. 

    The space_invaders function takes two parameters: an array of integers where each integer represents an alien's position 
    and an integer representing the position to aim the ray gun.

    The function should return an array of the remaining aliens' positions after the ray gun has been fired. 

    Assume that the position of aliens and the ray are always positive integers. 

    Remember: The ray gun destroys the alien at its aimed position as well as any alien in the adjacent positions. 
    The ray gun does not destroy any aliens that live in odd positions unless they are directly aimed at

    Examples:

    assert space_invaders([1, 2, 3, 4, 5], 3) == [1, 5]
    assert space_invaders([1, 2, 4, 5, 6], 4) == [1, 2, 5, 6]
    assert space_invaders([2, 3, 5, 6, 7, 9, 10], 6) == [2, 3, 5, 7, 9, 10]
    assert space_invaders([1, 2, 3, 5, 6, 7], 1) == [3, 5, 6, 7]
    """
    remaining_aliens = []
    for alien in aliens:
        if alien not in [ray, ray - 1, ray + 1]:
            remaining_aliens.append(alien)
    return remaining_aliens