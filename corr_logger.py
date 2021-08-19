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
