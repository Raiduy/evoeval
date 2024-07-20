def spaceship_trajectory(spaceship_data):
    """Create a function which takes a list of tuples representing a spaceship's flight data,
    and returns a string indicating the spaceship's final status.
    Each tuple in the list represents a single action, where:
    - The first element is a string indicating the action ('Launch', 'Move', 'Land')
    - The second element is an integer indicating the distance moved in that action 
    (negative for backwards, positive for forwards)
    The spaceship's status is determined by the following rules:
    - Initially, the spaceship is 'On Ground'
    - 'Launch' action can only be performed when the spaceship is 'On Ground' and will change the status to 'In Space'
    - 'Move' action can only be performed when the spaceship is 'In Space' and will not change the status
    - 'Land' action can only be performed when the spaceship is 'In Space', it will change the status back to 'On Ground'
    - If any action is invalid according to these rules, return 'Invalid Action Sequence'. Otherwise, return the final status.
    Examples:
    spaceship_trajectory([('Launch', 1), ('Move', 2), ('Land', -1)]) # => 'On Ground'
    spaceship_trajectory([('Launch', 1), ('Move', 2), ('Land', -1), ('Move', 3)]) # => 'Invalid Action Sequence'
    """
    status = 'On Ground'
    for (action, distance) in spaceship_data:
        if action == 'Launch':
            if status == 'On Ground':
                status = 'In Space'
            else:
                return 'Invalid Action Sequence'
        elif action == 'Move':
            if status == 'In Space':
                continue
            else:
                return 'Invalid Action Sequence'
        elif action == 'Land':
            if status == 'In Space':
                status = 'On Ground'
            else:
                return 'Invalid Action Sequence'
    return status