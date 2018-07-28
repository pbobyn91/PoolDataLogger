# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:52:11 2018

@author: Pat

This is a key logger for pool pressure. It is meant as a tool to determine if 
the pool needs more water. When the pool needs water the pressure of the pool 
should be lower than the normal. 
"""

# import method to collect date and time
import datetime

# get the pressure and the date
pressure = int(input('What is the pools pressure? '))
date = datetime.datetime.now()

# appends newly collected date to the log
with open('poolLog.txt', mode = 'a') as poolLog:
    # printed as:
    # date time pressure
    poolLog.write(f'\n{date} {pressure}')

# determines if the pool needs water and sends message if it does    
if pressure <= 15:
    print('Pool needs water')
