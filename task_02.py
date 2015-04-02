#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

DAY = raw_input('What day is it? ').lower()
WEEKDAY = (DAY == 'Sat' or DAY == 'Sun' or DAY == 'Saturday' or DAY == 'Sunday')
TIME = int(raw_input('What time is it? '))
#TIME = int(TIME)
DISPLAY_TIME = (TIME < 600)

if (WEEKDAY or DISPLAY_TIME):
    SNOOZE = True
else:
    SNOOZE = False

if not SNOOZE:
    print 'Beep! Beep! Beep! Beep! Beep!'
