import datetime
import jdatetime
from dateutil import parser


def gregorian_to_jalali(_date, format_split='-'):
    """
        Convert Gregorian date to Jalali date into Template
    """
    if format_split == '-':
        text_date = "{0:04d}-{1:02d}-{2:02d}"

    elif format_split == '/':
        text_date = "{0:04d}/{1:02d}/{2:02d}"

    if isinstance(_date, str):
        _date = _date.strip()

        if len(_date) <= 11:
            _date = parser.parse(_date).date()

        else:
            _date = parser.parse(_date)

    if isinstance(_date, unicode):
        _date = str(_date).strip()

        if len(_date) <= 11:
            _date = parser.parse(_date).date()

        else:
            _date = parser.parse(_date)

    if isinstance(_date, datetime.datetime):
        with_time = True

    elif isinstance(_date, datetime.date):
        with_time = False

    year = _date.year
    month = _date.month
    day = _date.day
    date = jdatetime.GregorianToJalali(year, month, day)

    if with_time:
        _datetime = text_date.format(date.jyear, date.jmonth, date.jday)
        _datetime += ' {0:02d}:{1:02d}:{2:02d}'.format(
            _date.hour,
            _date.minute,
            _date.second
        )

        return _datetime

    else:
        _date = text_date.format(date.jyear, date.jmonth, date.jday)

        return _date


def jalali_to_gregorian(year, month, day):
    gregorian = jdatetime.JalaliToGregorian(year, month, day)
    gyear, gmonth, gday = gregorian.getGregorianList()
    _date = datetime.date(gyear, gmonth, gday)
    return _date

