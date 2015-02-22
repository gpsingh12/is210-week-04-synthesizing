#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

import decimal
import fractions
NAME = raw_input('What is your name? ')

PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = int(PRINCIPAL)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
Prequalified = raw_input('Are you pre-qualified for this loan? ')

if (PRINCIPAL <= 199999) and (DURATION <= 15) and (Prequalified == 'Yes' or 'y'):
        #if Prequalified == 'Yes' or 'y':
         InterestRate = 3
        #elif Prequalified == 'No' or 'n':
         #InterestRate = 4
        #else : print 'Error'
elif (PRINCIPAL <= 199999) and (DURATION <= 15) and (Prequalified == 'No' or 'n'):
        InterestRate = 4

if (PRINCIPAL <= 199999) and (16 <= DURATION <= 20):
    if Prequalified == 'Yes' or 'y':
        InterestRate = 5
    else: InterestRate = 6
AMOUNT = PRINCIPAL *( 1 + (InterestRate/12))^(12*DURATION)
        
print '                                    '               
print 'Loan Report for: ' '{}'.format(NAME)
print '--------------------------------------'
print 'Principal : ''{}'.format(PRINCIPAL)
print 'Duration: ' '{}'.format(DURATION)
print 'Prequalified: ' '{}'.format(Prequalified)
print '                                          '
print 'Total: ''{}'.format(AMOUNT)



