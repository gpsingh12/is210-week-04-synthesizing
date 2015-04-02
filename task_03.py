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
Prequalified = raw_input('Are you pre-qualified for this loan? ')
PRE_Q = (Prequalified == 'Yes') or (Prequalified == 'y')
PRE_QL = Prequalified == 'No' or 'n'
Comp_Int = 12
TOTAL = None
#Interest_Rate = None

if PRN and DUR:
    if PRE_Q:
        Interest_Rate =decimal.Decimal('0.0363')
    elif PRE_QL:
        Interest_Rate = decimal.Decimal('0.0465')
    else:
        Interest_Rate = None

if PRN and DRN:
    if PRE_Q:
        Interest_Rate =decimal.Decimal('0.0404')
    elif PRE_QL:
        Interest_Rate = decimal.Decimal('0.0498')
    else:
        Interest_Rate = None

if PRN and DRT:
    if PRE_Q:
        Interest_Rate =decimal.Decimal('0.0577')
    elif PRE_QL:
        Interest_Rate = decimal.Decimal('0.0639')
    else:
        Interest_Rate = None

if PRP and DUR:
    if PRE_Q:
        Interest_Rate =decimal.Decimal('0.0302')
    elif PRE_QL:
        Interest_Rate = decimal.Decimal('0.0398')
    else:
        Interest_Rate = None

if PRP and DRN:
    if PRE_Q:
        Interest_Rate =decimal.Decimal('0.0327')
    elif PRE_QL:
        Interest_Rate = decimal.Decimal('0.0408')
    else:
        Interest_Rate = None


if PRP and DRT and PRE_Q:
    Interest_Rate = decimal.Decimal('0.0466')
else:
    Interest_Rate = None
    
            
if PRL and DUR and PRE_Q:
    Interest_Rate = decimal.Decimal('.0205')
else:
    Interest_Rate = None
    
if PRL and DRN and PRE_Q:
    Interest_Rate = decimal.Decimal(' .0262')
else:
    Interest_Rate = None
if Interest_Rate:
    AMOUNT = PRINCIPAL * (1 + Interest_Rate/Comp_Int)**(Comp_Int*DURATION)  
    TOTAL = int(AMOUNT)
    TOTAL = int(round(TOTAL))
    
REPORT = 'Loan Report for:  {}'.format(NAME)
REPORT += '----------------------------------------'  + '\n'
REPORT += 'Principal: {}'.format(PRINCIPAL)
REPORT += 'Duration:   {}'.format(DURATION)
REPORT += 'Prequalified: {}'.format(Prequalified)
                                        

print REPORT
