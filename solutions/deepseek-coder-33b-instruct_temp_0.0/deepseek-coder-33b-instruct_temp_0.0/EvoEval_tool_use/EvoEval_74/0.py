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
    Write a function that accepts a list of car license plates and returns a list of cars that are not following the license plate format.
    
    The license plate format is "AA-NNNN-AA" where "A" represents an uppercase alphabet character and "N" represents a digit. The alphabets cannot be "I", "O", or "Q". 
    
    The license plates are separated by commas in the string.

    Examples
    check_plates("AB-1234-CD,EF-5678-GH,IJ-9012-KL") ➞ ['IJ-9012-KL']
    check_plates("AB-1234-CD,EF-5678-GH,IJ-9012-KL,MN-3456-OP") ➞ ['IJ-9012-KL', 'MN-3456-OP']
    check_plates("AB-1234-CD,EF-5678-GH,IJ-9012-KL,MN-3456-OP,QR-7890-ST,UV-2345-WX,YZ-6789-ZA") ➞ [['IJ-9012-KL', 'MN-3456-OP', 'QR-7890-ST']
    """
    plates = plates.split(',')
    invalid_plates = []
    for plate in plates:
        if not check_format(plate) or check_invalid_alphabets(plate):
            invalid_plates.append(plate)
    return invalid_plates