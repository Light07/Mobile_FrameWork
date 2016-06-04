from DateTime import DateTime

SECONDS_IN_ONE_DAY = 60 * 60 * 24
MINUTES_IN_ONE_DAY = 60 * 24

class MONTH_ABBREVIATION_LIST:
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

    @staticmethod
    def get_month_value(month):
        return str(getattr(MONTH_ABBREVIATION_LIST, month)).rjust(2, '0')

class MONTH_LIST:
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

    @staticmethod
    def get_month_value(month):
        return str(getattr(MONTH_LIST, month)).rjust(2, '0')

'''
This function is used to decide the year of the date for the incoming month.
The year return is either current year or next year
'''
def get_year_by_month(month):
    input_month = int(getattr(MONTH_LIST, month))
    current_month = int(DateTime().month())
    current_year = DateTime().year()
    if input_month < current_month:
        return str(current_year + 1)

    return str(current_year)

def convert_date_time_format(date_time, from_fmt, to_fmt):
    original_date = DateTime(date_time, date_format=from_fmt)
    return original_date.strftime(to_fmt)

def get_diff_in_seconds(time1, time2):
    return (time2 - time1) * SECONDS_IN_ONE_DAY

def get_diff_in_minutes(time1, time2):
    return (time2 - time1) * MINUTES_IN_ONE_DAY

if __name__ == '__main__':
    d1 = DateTime('2015-11-1 13:00')
    d2 = DateTime('2015-11-1 14:00')
    print get_diff_in_seconds(d1, d2)
    print get_diff_in_minutes(d1, d2)
