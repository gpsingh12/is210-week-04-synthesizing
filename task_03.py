#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = int(PRINCIPAL)
PRN = PRINCIPAL <= 199999
PRP = (200000 <= PRINCIPAL <= 999999)
PRL = (PRINCIPAL >= 1000000)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
DUR = (1 <= DURATION <= 15)
DRN = (16 <= DURATION <= 20)
DRT = (21 <= DURATION <= 30)
pre-qualified = raw_input('Are you pre-qualified for this loan? ')
#PRE_Q = (pre-qualified == 'Yes') or (pre-qualified == 'y')
#PRE_QL = pre-qualified == 'No' or 'n'
Comp_Int = 12
TOTAL = int()
rate = None

if PRN and DUR:
    if (pre-qualified == 'Yes') or (pre-qualified == 'y') :
        rate = decimal.Decimal('0.0363')
    elif pre-qualified == 'No' or 'n':
        rate = decimal.Decimal('0.0465')
    else:
        rate = None

if PRN and DRN:
    if (pre-qualified == 'Yes') or (pre-qualified == 'y'):
        rate = decimal.Decimal('0.0404')
    elif pre-qualified == 'No' or 'n':
        rate = decimal.Decimal('0.0498')
    else:
        rate = None

if PRN and DRT:
    if (pre-qualified == 'Yes') or (pre-qualified == 'y'):
        rate = decimal.Decimal('0.0577')
    elif pre-qualified == 'No' or 'n':
        rate = decimal.Decimal('0.0639')
    else:
        rate = None

if PRP and DUR:
    if (pre-qualified == 'Yes') or (pre-qualified == 'y'):
        rate = decimal.Decimal('0.0302')
    elif pre-qualified == 'No' or 'n':
        rate = decimal.Decimal('0.0398')
    else:
        rate = None

if PRP and DRN:
    if (pre-qualified == 'Yes') or (pre-qualified == 'y'):
        rate = decimal.Decimal('0.0327')
    elif pre-qualified == 'No' or 'n':
        rate = decimal.Decimal('0.0408')
    else:
        rate = None


if PRP and DRT and (pre-qualified == 'Yes') or (pre-qualified == 'y'):
    rate = decimal.Decimal('0.0466')
else:
    rate = None
    
            
if PRL and DUR and (pre-qualified == 'Yes') or (pre-qualified == 'y'):
    rate = decimal.Decimal('.0205')
else:
    rate = None
if PRL and DRN and (pre-qualified == 'Yes') or (pre-qualified == 'y'):
    rate = decimal.Decimal(' .0262')
else:
    rate = None
if rate != None:
    AMOUNT = PRINCIPAL * (1 + rate/Comp_Int)**(Comp_Int*DURATION)  
    TOTAL = int(AMOUNT)
    TOTAL = int(round(TOTAL))
REPORT = 'Loan Report for:  {}\n'.format(NAME)
REPORT += '----------------------------------------\n'
REPORT += 'Principal:$ {}\n'.format(PRINCIPAL)
REPORT += 'Duration:  {}\n'.format(DURATION)
REPORT += 'Pre-qualified ? : {}\n'.format(prequalified)
REPORT += 'TOTAL:  {}'.format(TOTAL)

print REPORT


