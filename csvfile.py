#!/usr/bin/env python
import sys
import numpy
import math
try:
    csvfilename=sys.argv[1]
except:
    print "CSV file not mentioned"
    sys.exit()
f = open(csvfilename,"r")
#Read first 34 rows
for i in range(0,35):
    c = f.readline
#Need to read the number of samples, for the number of samples read the values.
#Extract the frequency
#StartHz = 
#StopHz =
#Samples = 
#Span = StopHz - StartHz
for i in range(0,samples):
    value = f.readline
    hz = 
