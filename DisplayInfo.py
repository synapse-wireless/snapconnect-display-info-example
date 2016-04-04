"""
DisplayInfo.py - an example for the SNAP Connect User Manual

Simply displays some info, then exits.
"""

import logging
import sys

from snapconnect import snap

def main():
    global comm

    print "Python version is " + sys.version

    comm = snap.Snap(funcs={})
    print "SNAP Connect version number " + str(comm.get_info(5)) + "." + str(comm.get_info(6)) + "." + str(comm.get_info(7))

    addr = comm.load_nv_param(2)
    print "My SNAP Address is " + "%02X.%02X.%02X" % (ord(addr[-3]), ord(addr[-2]), ord(addr[-1]))
    
    encryption_setting = comm.load_nv_param(snap.NV_AES128_ENABLE_ID)
    print "Encryption is set to " + str(encryption_setting)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    main()
