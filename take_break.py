"""
This program opens a Youtube video (I get knocked down by Chumbawamba)
every 2 hours to encourage you to take a break from the computer
and dance for a couple of minutes :-)
"""

import webbrowser
import time

nbreaks = 0
print "This program started on " + time.ctime()
while nbreaks < 3:
    time.sleep(3600)
    webbrowser.open("https://youtu.be/kS-zK1S5Dws?t=12s")
    nbreaks = nbreaks + 1

