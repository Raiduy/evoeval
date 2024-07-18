def check_format(plate):
    """checks if the plate follows the correct format "AA-NNNN-AA" where "A" represents an uppercase alphabet character and "N" represents a digit."""
    import re

    pattern = "[A-Z]{2}-\d{4}-[A-Z]{2}"
    return re.fullmatch(pattern, plate) is not None


def check_invalid_alphabets(plate):
    '''checks if the plate contains invalid alphabets "I", "O", or "Q"'''
    invalid_alphabets = ["I", "O", "Q"]
    return any(alphabet in plate for alphabet in invalid_alphabets)
def check_plates(plates):
    """
    Accepts a string of comma-separated car license plates and returns a list of plates that are not following the license plate format.
    """
    plate_list = plates.split(',')
    invalid_plates = []
    for plate in plate_list:
        if not check_format(plate) or check_invalid_alphabets(plate):
            invalid_plates.append(plate)
    return invalid_plates