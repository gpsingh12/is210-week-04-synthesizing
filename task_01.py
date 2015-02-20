#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

COLOR = raw_input('Which base color?, "Seattle Gray" or "Mantee"? ')
BASE = '{}'.format(COLOR)

if BASE == 'Mantee':
    ACCENT = raw_input('Which accent color, "Platinum Mist" or "Spartan Sage"')
else:
    ACCENT = raw_input('Which accent color "Cumulus Nimbus" or "Ceramic Glaze"')

if ACCENT == 'Platinum Mist':
    HIGHLIGHT = raw_input('Which Highlight color, "Bone white" or "Just White')
elif ACCENT == 'Spartan Sage':
    HIGHLIGHT = raw_input('Which Highlight color, "Fractal White" or Not White')
elif ACCENT == 'Cumulus Nimbus':
    HIGHLIGHT = raw_input('Which Highlight color, "Paper White" or "Off White')
else:
    HIGHLIGHT = raw_input('Which Highlight color, "White" or "Basically White')

print 'Your selected colors are {} {} {}'.format(BASE, ACCENT, HIGHLIGHT)
