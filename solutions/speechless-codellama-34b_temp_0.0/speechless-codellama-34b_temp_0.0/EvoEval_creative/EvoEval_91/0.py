def spaceship_trajectory(spaceship_data):
    status = 'On Ground'
    for (action, distance) in spaceship_data:
        if action == 'Launch' and status == 'On Ground':
            status = 'In Space'
        elif action == 'Move' and status == 'In Space':
            pass
        elif action == 'Land' and status == 'In Space':
            status = 'On Ground'
        else:
            return 'Invalid Action Sequence'
    return status