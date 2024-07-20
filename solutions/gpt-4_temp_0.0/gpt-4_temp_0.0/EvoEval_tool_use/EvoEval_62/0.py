def parse_record(record):
    """ parse a record into tuple (item, price, quantity)
    >>> parse_record("apple,1.2,3")
    ('apple', 1.2, 3)
    """
    parts = record.split(',')
    return parts[0], float(parts[1]), int(parts[2])


def is_valid_record(record):
    """ verify if a record is valid
    >>> is_valid_record("apple,1.2,3")
    True
    >>> is_valid_record("apple,1.2")
    False
    """
    parts = record.split(',')
    return len(parts) == 3 and parts[1].replace(".", "", 1).isdigit() and parts[2].isdigit()
def compile_report(records: list):
    """ records is a list of strings where each string is a transaction record in the format "item,price,quantity".
    The function should return a dictionary where keys are items and values are total revenues of each item. (skip any transaction records which do not follow the format)
    >>> compile_report(["apple,1.2,3", "banana,0.5,6", "apple,1.2,2"])
    {'apple': 6.0, 'banana': 3.0}
    >>> compile_report(["orange,1.3,10", "banana,0.5,5", "orange,1.3,5"])
    {'orange': 19.5, 'banana': 2.5}
    """
    report = {}
    for record in records:
        if is_valid_record(record):
            (item, price, quantity) = parse_record(record)
            if item in report:
                report[item] += price * quantity
            else:
                report[item] = price * quantity
    return report