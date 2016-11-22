##Program Name:     OfficeStatus.py
##Purpose:          Use python datetime module to determine whether a business branch
##                  in different timezones open or closed based on current time.
##Program Language: Python
##Language Version: 2.7.9
##Platform Tested:  Windows 8.1 on x86
##Author:           Matt Kozlowski
##Date Created:     October 13, 2016


import datetime
import time
import os
from datetime import datetime, tzinfo, timedelta
    
dt=datetime.now()


def opencl(hh):                                          ## function to determine if branch open or closed
    if hh>9 and hh<21:
        print('open'+'\n')          
    else:
        print('closed'+'\n')
          
class BST(tzinfo):                                       ## create class object for London time offset, DST
    def utcoffset(self, dt):
        return timedelta(hours=0)+self.dst(dt)
    def dst(self, dt):
        return timedelta(hours=1)
    def tzname(self, dt):
        return "London Office: BST(British Summer Time)"


class EST(tzinfo):                                       ## create class object for New York time offset, DST
    def utcoffset(self, dt):                             
        return timedelta(hours=-4)
    def dst(self, dt):
        return timedelta(hours=0)
    def tzname(self, dt):
        return "New York Office: EST"


class PST(tzinfo):                                       ## create class object for Portland Branch offset, DST
    def utcoffset(self, dt):
        return timedelta(hours=-7)
    def dst(self, dt):
        return timedelta(hours=0)
    def tzname(self, dt):
        return "PDX Office: PST"
pst=PST()
bst=BST()
est=EST()

for zone in [pst, est, bst]:                                  ## loop to print time/status info for each Branch
    print(zone.tzname(dt))
    z=(datetime.now(tz=zone).strftime('%a,%b %d, %Y %H:%M'))  # format and print Branch Local time
    print(z)
    h=(datetime.now(tz=zone).strftime('%H'))                  # get the 'hour' parameter of relative TZ
    hh=int(h)
    opencl(hh)                                                ## closed/open function call
    


    
       
    
    

