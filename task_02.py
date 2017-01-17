#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

phrase = inquisition.SPANISH
pattern = 'Spanish'
replace = 'Flemish'

FLEMISH = phrase[:phrase.index(pattern)] + replace + \
          phrase[phrase.index(pattern) + len(pattern):]
