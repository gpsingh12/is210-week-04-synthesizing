#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

import decimal
import fractions
import math
NAME = raw_input('What is your name? ')

PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = int(PRINCIPAL)
PRN = PRINCIPAL <= 199,999
PRP = (2000,000 <= PRINCIPAL <= 999,999)
PRL = (PRINCIPAL >= 1000000)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
DUR =  (DURATION <= 15)
DRN = (16 <= DURATION <=20)
DRT = (21 <= DURATION <= 30)
Prequalified = raw_input('Are you pre-qualified for this loan? ')
PRE_Q = Prequalified == 'Yes' or Prequalified == 'y'
PRE_QL = Prequalified == 'No' or 'n'

if PRN and DUR and PRE_Q:
    InterestRate = 3.63
else:
    InterestRate = 4.65

if PRN and DRN and PRE_Q :
    InterestRate = 4.04
else:
    InterestRate = 4.98

if PRN and PRE_Q and DRT:
    InterestRate = 5.77
else:
    Interestrate = 6.39

if PRP and PRE_Q and DUR:
    InterestRate = 3.02 
else:
    InterestRate = 3.98

if PRP and DRN and PRE_Q:
    InterestRate = 3.27
else:
    InterestRate = 4.08

if PRP and DRT and PRE_Q:
    InterestRate = 4.66


if PRL and DUR and PRE_Q:
    InterestRate = 2.05

if PRL and DRN and PRE_Q:
    InterestRate = 2.62

    
AMOUNT = PRINCIPAL *( 1 + (InterestRate/12))**float(12*DURATION)
AM = format(AMOUNT, '.5f')
print InterestRate   
print '                                    '               
print 'Loan Report for: ' '{}'.format(NAME)
print '--------------------------------------'
print 'Principal : ''{}'.format(PRINCIPAL)
print 'Duration: ' '{}'.format(DURATION)
print 'Prequalified: ' '{}'.format(Prequalified)
print '                                          '
print 'Total: ''{}'.format(AM)



