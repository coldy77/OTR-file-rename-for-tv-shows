#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Search for mp4 files and move them in the right folder
"""

import os
from otr_rename import OTR_Rename

files = [f for f in os.listdir(".") if f.endswith('.mp4')]

for filename in files:
    print filename
    tv_show = OTR_Rename(filename)
    tv_show.copy_and_sort()





