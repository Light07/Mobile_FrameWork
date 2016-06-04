import time
from DateTime import DateTime

from common import date_time_utils

date1 = DateTime()
time.sleep(2)
date2 = DateTime()

print date_time_utils.get_diff_in_seconds(date1, date2)