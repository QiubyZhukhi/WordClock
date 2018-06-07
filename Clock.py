# -*- coding: utf-8 -*-
# wordclock_gui.py -- A simple python word clock made with love

import os
import sys
import android
import time
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, "WordClock"))

from layout import *
from wmap import *

textSize = 14
textBackground = "#ff000000"
textColor = "#ff616161"
droid = android.Android()

def clearer():
  for x in WORD.items():
    for y in x[1]:
      droid.fullSetProperty(y, "textColor", textColor)

def timer(h, m, s):
  a, i = False, False
  if s > 30:
    m += 1
  if m <= 3:
    o = ["IT", "IS"]
    a = True
  elif m <= 8:
    o = ["IT", "IS", "M_FIVE", "PAST"]
  elif m <= 13:
    o = ["IT", "IS", "M_TEN", "PAST"]
  elif m <= 18:
    o = ["IT", "IS", "A", "QUARTER", "PAST"]
  elif m <= 23:
    o = ["IT", "IS", "TWENTY", "PAST"]
  elif m <= 28:
    o = ["IT", "IS", "TWENTY", "M_FIVE", "PAST"]
  elif m < 33:
    o = ["IT", "IS", "HALF", "PAST"]
  elif m < 38:
    o = ["IT", "IS", "TWENTY", "M_FIVE", "TO"]
    i = True
  elif m < 43:
    o = ["IT", "IS", "TWENTY", "TO"]
    i = True
  elif m < 48:
    o = ["IT", "IS", "A", "QUARTER", "TO"]
    i = True
  elif m < 53:
    o = ["IT", "IS", "M_TEN", "TO"]
    i = True
  elif m < 58:
    o = ["IT", "IS", "M_FIVE", "TO"]
    i = True
  else:
    o = ["IT", "IS"]
    a = True
    i = True
  if i:
    h += 1
  if h == 1:
    o.append("ONE")
  elif h == 2:
    o.append("TWO")
  elif h == 3:
    o.append("THREE")
  elif h == 4:
    o.append("FOUR")
  elif h == 5:
    o.append("H_FIVE")
  elif h == 6:
    o.append("SIX")
  elif h == 7:
    o.append("SEVEN")
  elif h == 8:
    o.append("EIGHT")
  elif h == 9:
    o.append("NINE")
  elif h == 10:
    o.append("H_TEN")
  elif h == 11:
    o.append("ELEVEN")
  else:
    o.append("TWELVE")
  if a:
    o.append("OCLOCK")
  return o

def main():
    minStart = 61
    droid.fullShow(RES.format(tb=textBackground, tc=textColor, ts=textSize), 'grid')
    droid.wakeLockAcquireBright()
    while 1:
        droid.eventPost("showTime","",True)
        sign = droid.eventWait().result
        if sign['name'] == 'key' and sign['data']['key'] == '4':
            break
        if sign['name'] == 'showTime':
            (hh, mm, ss) = time.strftime("%I, %M, %S").split(",")
            if minStart != int(mm):
                c = timer(int(hh), int(mm), int(ss))
                clearer()
                for x in c:
                    for y in WORD[x]:
                        droid.fullSetProperty(y, "textColor", "#ffffffff")
                minStart = int(mm)
            time.sleep(500/1000.0)
    droid.wakeLockRelease()
    droid.fullDismiss()
    sys.exit("Exit key pressed...")

if __name__ == '__main__':
    main()