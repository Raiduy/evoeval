def zodiac_element(birthdays):
    if not birthdays:
        return None
    zodiac_elements = {'Fire': [('03-21', '04-19'), ('07-23', '08-22'), ('11-22', '12-21')], 'Earth': [('04-20', '05-20'), ('08-23', '09-22'), ('12-22', '01-19')], 'Air': [('05-21', '06-20'), ('09-23', '10-22'), ('01-20', '02-18')], 'Water': [('06-21', '07-22'), ('10-23', '11-21'), ('02-19', '03-20')]}
    result = {}
    for birthday in birthdays:
        month_day = birthday[5:]
        for (element, ranges) in zodiac_elements.items():
            for date_range in ranges:
                if date_range[0] <= month_day <= date_range[1] or (date_range[0] > date_range[1] and (month_day >= date_range[0] or month_day <= date_range[1])):
                    result[element] = result.get(element, 0) + 1
                    break
    return result