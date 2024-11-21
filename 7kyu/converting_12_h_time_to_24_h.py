# https://www.codewars.com/kata/59b0a6da44a4b7080300008a
def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    if period == 'pm' and hour == 12 and (minute == 00 or minute == 0):
        return '1200'
    if period == 'am' and hour == 12 and (minute == 00 or minute == 0):
        return '0000'

    if period == 'pm':
        if hour == 12:
            ohour = '12'
        else:
            ohour = hour + 12
            ohour = str(ohour)

    if period == 'am':
        if hour == 12:
            ohour = '00'
        elif hour < 10:
            ohour = '0' + str(hour)
        else:
            ohour = str(hour)

    if minute < 10:
        ominute = '0' + str(minute)
    else:
        ominute = str(minute)

    return ohour + ominute
