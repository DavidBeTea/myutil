# -*- coding: utf-8 -*-
"""
DateUtil
@date 2017/11/8
@author: Dai Wei
================

"""
import calendar

from datetime import datetime, timedelta, date


class DateUtil(object):
    def __init__(self):
        self.day_format = "%Y-%m-%d"
        self.time_format = "%Y-%m-%d %H:%M:%S"
        self.now = datetime.now()
        self.today = datetime.strptime(datetime.today().strftime(self.day_format), self.day_format)
        self.daydelta = timedelta(days=1)

    def get_interval(self, begin, end):
        """(begin: str, end: str) ->int:"""
        t1 = datetime(int(begin[0:4]), int(begin[5:7]), int(begin[8:10]))
        t2 = datetime(int(end[0:4]), int(end[5:7]), int(end[8:10]))
        return (t2 - t1).days

    def get_date_list(self, begin, end):
        """(begin:str,end:str)->list[str]"""
        interval = self.get_interval(begin, end)
        return [self.get_last_days(begin, -x) for x in range(interval + 1)]

    def get_date_list_string(self, begin, end, connnector=',', str_format=None):
        if not str_format:
            str_format = self.day_format
        date_list = self.get_date_list(begin, end)
        return connnector.join(map(lambda x: datetime.strptime(x, self.day_format).strftime(str_format), date_list))

    def get_last_days(self, begin, interval, str_format=True):
        """(begin:str,interval:int)->str or datetime"""
        start = datetime(int(begin[0:4]), int(begin[5:7]), int(begin[8:10]))
        delta = timedelta(days=1)
        if interval < 0:
            for _ in range(0, -interval):
                start = start + delta
        else:
            for _ in range(0, interval):
                start = start - delta
        if str_format:
            return start.strftime("%Y-%m-%d")
        else:
            return start

    def get_before_month(self, year, month, day, n):
        """(year:int,month:int,day:int,n:int)->datetime.time"""
        for i in range(0, n):
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        day = min(day, calendar.monthrange(year, month)[1])
        return date(year, month, day)

    def get_month_list(self, begin, end):
        """(begin:str,end:str)->list[str]"""
        begin_date = datetime.strptime(begin, "%Y-%m").date()
        end_date = datetime.strptime(end, '%Y-%m').date()
        temp = end_date
        month_list = []
        while temp >= begin_date:
            month_list.append(temp.strftime('%Y-%m'))
            temp = self.get_before_month(temp.year, temp.month, 1, 1)
        month_list.reverse()
        return month_list

    def get_n_month_ago_begin(self, begin, n):
        """(begin:str,n:int)->str"""
        year = int(begin[:4])
        month = int(begin[5:7])
        if n > 0:
            for i in range(0, n):
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
        else:
            for i in range(0, -n):
                if month == 12:
                    month = 0
                    year += 1
                month += 1
        return date(year, month, 1).strftime('%Y-%m')

    def get_today(self, format=None):
        """(format:str)->str"""
        if not format:
            return self.today.strftime(self.day_format)
        else:
            return self.today.strftime(format)

    def get_now(self, format=None):
        """(format:str)->str"""
        if not format:
            return self.now.strftime(self.time_format)
        else:
            return self.now.strftime(format)

    def get_n_month_ago(self, n=1, str_format=True):
        """(n:int,str_format:boolean)->str or datetime"""
        date_str = self.get_n_month_ago_begin(self.get_today(), n)
        return date_str if str_format else datetime.strptime(date_str, self.day_format)

    def get_n_week_ago(self, n=1, str_format=True):
        """(n:int,str_format:boolean)->str or datetime"""
        r = self.today - timedelta(weeks=n)
        return r.strftime(self.day_format) if str_format else r

    def get_n_day_ago(self, n=1, str_format=True):
        """(n:int,str_format:boolean)->str or datetime"""
        r = self.today - timedelta(days=n)
        return r.strftime(self.day_format) if str_format else r

    def get_n_hours_ago(self, n=1, str_format=True, remove_last=False):
        """(n:int,str_format:boolean)->str or datetime"""
        r = self.now - timedelta(hours=n)
        if str_format:
            return r.strftime("%Y-%m-%d %H:00:00") if remove_last else r.strftime(self.time_format)
        else:
            return r

    def get_n_minutes_ago(self, n=1, str_format=True, remove_last=False):
        """(n:int,str_format:boolean)->str or datetime"""
        r = self.now - timedelta(minutes=n)
        if str_format:
            return r.strftime("%Y-%m-%d %H:%M∂:00") if remove_last else r.strftime(self.time_format)
        else:
            return r


if __name__ == '__main__':
    model = DateUtil()
    begin = '2017-10-11'
    end = '2017-10-16'
    print ('today : %s' % model.get_today())
    print ('3 month age : %s ' % model.get_n_month_ago(3))
    print ('yesterday : %s ' % model.get_n_day_ago())
    print (model.get_date_list_string(begin, end, "','", '%y-%m-%d'))
