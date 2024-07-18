def is_valid(booking):
    """
    Helper function to check if a booking is valid.
    
    A booking is valid if it has the following fields:
    - `id`: a unique integer identifier
    - `dates`: a list of strings representing the dates of the booking
    - `room`: an integer representing the room number

    Variables:
        @booking: dict
            A dictionary representing a booking.

    Output:
        boolean
            Returns True if the booking is valid, False otherwise.
    """

    if 'id' not in booking or type(booking['id']) != int:
        return False
    if 'dates' not in booking or type(booking['dates']) != list:
        return False
    if 'room' not in booking or type(booking['room']) != int:
        return False

    for date in booking['dates']:
        if type(date) != str:
            return False

    return True
def get_conflicting_bookings(bookings):
    """
    Given a list of bookings, return a list of booking ids that have conflicts.

    A conflict occurs when two or more bookings have the same room and at least one overlapping date.
    Ignore any invalid bookings

    Example:
        For bookings = [
            {'id': 1, 'dates': ['2022-01-01', '2022-01-02'], 'room': 101},
            {'id': 2, 'dates': ['2022-01-02', '2022-01-03'], 'room': 101},
            {'id': 3, 'dates': ['2022-01-01', '2022-01-02'], 'room': 102},
        ], the output should be [1, 2] because bookings 1 and 2 conflict.

    Variables:
        @bookings: list of dict
            A list of dictionaries where each dictionary represents a hotel booking. Each dictionary must have the following keys:
            - 'id' (int): The unique identifier for the booking.
            - 'dates' (list): A list of strings representing the booked dates in the format 'YYYY-MM-DD'.
            - 'room' (int): The room number for the booking.
            Constraints: 1 ≤ bookings.length ≤ 10000, 1 ≤ bookings[i].length ≤ 365, all bookings are valid

    Output:
         list of integer
            Returns the list of booking ids that have conflicts.
    """