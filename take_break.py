"""
This program opens a Youtube video (I get knocked down by Chumbawamba)
every 2 hours to encourage you to take a break from the computer
and dance for a couple of minutes :-)
"""

import webbrowser
import time

count = 0
print("This program started on " + time.ctime())
while (count<3):
    time.sleep(1*3600)
    webbrowser.open("https://youtu.be/kS-zK1S5Dws?t=12s")
    count = count + 1

