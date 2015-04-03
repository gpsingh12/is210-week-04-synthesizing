#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

DAY = raw_input('What day is it? ').lower().strip()[:3]
WEEKDAY = (DAY == 'sat') or (DAY == 'sun')
TIME = int(raw_input('What time is it? '))
DISPLAY_TIME = (TIME < 600)

SNOOZE = False
if WEEKDAY or DISPLAY_TIME:
    SNOOZE = True

if SNOOZE:
    print 'Beep! Beep! Beep! Beep! Beep!'
