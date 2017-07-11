import math
#This function takes the frequency of the signal in MHz and outputs the SARAS threshold in dBm/Hz
def SARAS(f = 600.00):
    if(f < 2E3):
        saras = -17.2708*math.log10(f)-192.0714
        print "I am in the part smaller than 2 000 MHz"
    else:
        saras = -0.065676*math.log10(f)-248.8661
        print "I am in the part larger than 2 000 MHz"
    return saras
