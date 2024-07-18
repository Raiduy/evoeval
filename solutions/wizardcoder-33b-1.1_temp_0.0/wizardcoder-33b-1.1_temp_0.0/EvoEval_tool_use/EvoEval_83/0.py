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
    valid_bookings = [booking for booking in bookings if is_valid(booking)]
    room_bookings = {}
    for booking in valid_bookings:
        room = booking['room']
        if room not in room_bookings:
            room_bookings[room] = [booking['id']]
        else:
            for other_booking in valid_bookings:
                if other_booking['id'] != booking['id'] and other_booking['room'] == room:
                    for date in booking['dates']:
                        if date in other_booking['dates']:
                            if booking['id'] not in room_bookings[room]:
                                room_bookings[room].append(booking['id'])
                            if other_booking['id'] not in room_bookings[room]:
                                room_bookings[room].append(other_booking['id'])
    return [id for ids in room_bookings.values() for id in ids]