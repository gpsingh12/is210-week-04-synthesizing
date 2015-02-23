#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

NAME = raw_input('What is your name? ')

PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = int(PRINCIPAL)
PRN = PRINCIPAL <= 199999
PRP = (2000000 <= PRINCIPAL <= 999999)
PRL = (PRINCIPAL >= 1000000)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
DUR = (DURATION <= 15)
DRN = (16 <= DURATION <= 20)
DRT = (21 <= DURATION <= 30)
Pre-qualified = raw_input('Are you pre-qualified for this loan? ')
PRE_Q = Pre-qualified == 'Yes' or Prequalified == 'y'
PRE_QL = Pre-qualified == 'No' or 'n'

if PRN and DUR and PRE_Q:
    Interest Rate = 3.63
else:
    Interest Rate = 4.65

if PRN and DRN and PRE_Q :
    Interest Rate = 4.04
else:
    Interest Rate = 4.98

if PRN and PRE_Q and DRT:
    Interest Rate = 5.77
else:
    Interest Rate = 6.39

if PRP and PRE_Q and DUR:
    Interest Rate = 3.02 
else:
    Interest Rate = 3.98

if PRP and DRN and PRE_Q:
    Interest Rate = 3.27
else:
    Interest Rate = 4.08

if PRP and DRT and PRE_Q:
    Interest Rate = 4.66


if PRL and DUR and PRE_Q:
    Interest Rate = 2.05

if PRL and DRN and PRE_Q:
    Interest Rate = 2.62

    
AMOUNT = PRINCIPAL *(1 + (InterestRate/12))**float(12*DURATION)
AM = format(AMOUNT, '.5f')
print Interest Rate   
#print '                                    '               
print 'Loan Report for: ' '{}'.format(NAME)
print '--------------------------------------'
print 'Principal : ''{}'.format(PRINCIPAL)
print 'Duration: ' '{}'.format(DURATION)
print 'Prequalified: ' '{}'.format(Prequalified)
print '                                          '
print 'Total: ''{}'.format(AM)
