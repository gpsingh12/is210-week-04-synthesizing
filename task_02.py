#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

DAY = raw_input('What day is it? ')
WEEKDAY = DAY == 'Sat' or DAY == 'Sun' or DAY == ' Saturday' or DAY == 'Sunday'
TIME = raw_input('What time is it, enter 4 digits format? ')
TIME = int(TIME)
DISPLAY_TIME = TIME < '0600'


if WEEKDAY and DISPLAY_TIME:
    SNOOZE = 'True'

else:
    SNOOZE = 'False'


if SNOOZE is 'False':

    print 'Beep! Beep! Beep! Beep! Beep!'
