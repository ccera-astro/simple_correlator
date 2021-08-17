# this module will be imported in the into your flowgraph
import time
import math

#
# Log a complex input value, with a computed filename, and a (UTC) timestamp
# Use a simple CSV format
#
def logval(val,fn):
    ltp = time.gmtime()
    filestr="%04d%02d%02d" % (ltp.tm_year, ltp.tm_mon, ltp.tm_mday)
    filestr = fn+"-"+filestr+".csv"
    fp = open(filestr, "a")
    fp.write("%02d,%02d,%02d," % (ltp.tm_hour, ltp.tm_min, ltp.tm_sec))
    fp.write("%-11.9f,%-11.9f\n" % (val.real, val.imag))
    fp.close()
    return None
    
def fperiod(freq,baseline,decln,latitude):
    C=299792000.0
    Lambda = C/freq
    #
    # Convert baseline into fringe-spacing in degrees
    #
    fwidth= (math.degrees(Lambda))/baseline
    
    #
    # 240 seconds (4 minutes) per degree on the celestial equator
    #
    fwidth *= (4.0 * 60.0)
    
    #
    # Adjust for declination and local latitude
    # Takes longer for source to transit through 'fwidth' at higher
    # declinations
    #
    fwidth /= math.cos(math.radians(decln))
    return fwidth

def getalpha(corner, srate):
    q = math.pow(math.e,-2.0*(corner/srate))
    alpha = 1.0 - q
    return alpha
