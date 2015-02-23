#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """
import decimal
NAME = raw_input('What is your name? ')

PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = float(PRINCIPAL)
PRN = PRINCIPAL <= 199999
PRP = (2000000 <= PRINCIPAL <= 999999)
PRL = (PRINCIPAL >= 1000000)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
DUR = (DURATION <= 15)
DRN = (16 <= DURATION <= 20)
DRT = (21 <= DURATION <= 30)
Pre_qualified = raw_input('Are you pre-qualified for this loan? ')
PRE_Q = Pre_qualified == 'Yes' or Pre_qualified == 'y'
PRE_QL = Pre_qualified == 'No' or 'n'

if PRN and DUR and PRE_Q:
    Interest_Rate = 3.63
else:
    Interest_Rate = 4.65

if PRN and DRN and PRE_Q :
    Interest_Rate = 4.04
else:
    Interest_Rate = 4.98

if PRN and PRE_Q and DRT:
    Interest_Rate = 5.77
else:
    Interest_Rate = 6.39

if PRP and PRE_Q and DUR:
    Interest_Rate = 3.02 
else:
    Interest_Rate = 3.98

if PRP and DRN and PRE_Q:
    Interest_Rate = 3.27
else:
    Interest_Rate = 4.08

if PRP and DRT and PRE_Q:
    Interest_Rate = 4.66


if PRL and DUR and PRE_Q:
    Interest_Rate = 2.05

if PRL and DRN and PRE_Q:
    Interest_Rate = 2.62

    
AMOUNT = PRINCIPAL *(1 + (Interest_Rate/12))**float(12*DURATION)
#print Interest_Rate   
#print '                                    '               
print 'Loan Report for: ' '{}'.format(NAME)
print '--------------------------------------'
print 'Principal : ''{}'.format(PRINCIPAL)
print 'Duration: ' '{}'.format(DURATION)
print 'Prequalified: ' '{}'.format(Pre_qualified)
print '                                          '
TOTAL = (AMOUNT)
print 'Total: ''{}'.format(TOTAL)
