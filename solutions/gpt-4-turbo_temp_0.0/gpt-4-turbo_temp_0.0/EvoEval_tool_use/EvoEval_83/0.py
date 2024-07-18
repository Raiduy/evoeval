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
    """
    conflicting_ids = set()
    for i in range(len(bookings)):
        booking1 = bookings[i]
        if not is_valid(booking1):
            continue
        for j in range(i + 1, len(bookings)):
            booking2 = bookings[j]
            if not is_valid(booking2):
                continue
            if booking1['room'] == booking2['room'] and has_date_overlap(booking1['dates'], booking2['dates']):
                conflicting_ids.add(booking1['id'])
                conflicting_ids.add(booking2['id'])
    return list(conflicting_ids)