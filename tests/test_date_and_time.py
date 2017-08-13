import datetime
import time
import os
from unittest import TestCase

from freezegun import freeze_time

class DateTimeTest(TestCase):

    @freeze_time("2000-01-01")
    def test_datetime_now(self):
        now = datetime.datetime.now()

        self.assertEqual(now,
                         datetime.datetime(year=2000,
                                           month=1,
                                           day=1,
                                           hour=0,
                                           minute=0,
                                           second=0))

    def test_set_timezone(self):
        os.environ['TZ'] = 'Europe/London'
        time.tzset()
        self.assertEqual(time.tzname, ('GMT', 'BST'))

        os.environ['TZ'] = 'US/Pacific'
        time.tzset()
        self.assertEqual(time.tzname, ('PST', 'PDT'))
