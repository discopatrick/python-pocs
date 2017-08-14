import datetime
import time
import os
from unittest import TestCase

from freezegun import freeze_time
from tzlocal import get_localzone

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

    def test_set_TZ_environment_variable(self):

        # ensure the TZ environment variable does not exist
        if os.environ.get('TZ'):
            del os.environ['TZ']

        # call tzset to set timezone to system default
        time.tzset()

        # get the system default tzname so we can check it gets set back to
        # its original value at the end of this test
        original_tzname = time.tzname

        os.environ['TZ'] = 'Europe/London'
        time.tzset()
        self.assertEqual(time.tzname, ('GMT', 'BST'))

        os.environ['TZ'] = 'US/Pacific'
        time.tzset()
        self.assertEqual(time.tzname, ('PST', 'PDT'))

        # reset timezone back to original value
        del os.environ['TZ']
        time.tzset()

        self.assertEqual(time.tzname, original_tzname)
