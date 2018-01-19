#!/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time


def terminal_reset():
    os.system("tput reset")


# Check if user is root
if not os.getuid() == 0:
  print("{}{}{}{}{}".format(chr(27), "[1m", "You must be root to change systemsettings!", chr(27), "[0m"))
  sys.exit(2)


# Resize Terminal
print("{}{}".format(chr(27), "[8;20;85t"))

# Clear screen
os.system("tput reset")


# Graphical Intro
w=sys.stdout.write
f=sys.stdout.flush
t=time.sleep
t(0.2); w("\n ZZ   ZZ \n"); t(0.1); w("  ZZ ZZ  "); f(); t(0.1); w("  ANTI"); f(); w("\n   ZZZ   "); f(); t(0.1); w("  X"); f(); t(0.1); w("S"); f(); t(0.1); w("PLOI"); f(); t(0.1); w("T"); f(); t(0.1); w("\n  ZZ ZZ  "); f(); t(0.1); w("  BY PINKYBOO 2017"); f(); t(0.1); w("\n ZZ "); f(); t(0.1); w("  ZZ   "); f()


i=0
while i < 16:
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.05)
    i+=1


w("\n\n"); f(); w(" [ 1 :Hardening Kernel     ]═══════╗\n"); t(0.1); f(); t(0.1); w(" [ 2 :Blacklist Modules    ]═╦═════╩═╗\n"); f(); t(0.1); w(" [ 3 :Disable Multicast    ]═╩══╗    ║\n"); f(); t(0.1); w(" [ 4 :Setup Iptables       ]════╝    ╚╦═╗\n"); f(); t(0.1); w(" [ 5 :README               ]═════════╦╝ ║\n"); f(); t(0.1); w(" [ 6 :Quit                 ]═════════╝  ╚═"); f(); t(0.1)


# Ask for processnumber to execute
while 1:
    inp = raw_input("[root@machine ~]# ").lower()
    if inp.strip() == "1":
      terminal_reset()
      os.system('./main/kernel.py')
      sys.exit()
    elif inp.strip() == "2":
      terminal_reset()
      os.system('./blacklib/blacklist.py')
      sys.exit()
    elif inp.strip() == "3":
      terminal_reset()
      os.system('./main/multicast.py')
      sys.exit()
    elif inp.strip() == "4":
      terminal_reset()
      os.system('./main/iptables.py')
      sys.exit()
    elif inp.strip() == "5":
      os.system("less ./main/README.txt")
      w("{}{}{}{}{}".format(chr(27), "[1A", chr(27), "[2K", " [ 6 :Quit                 ]═════════╝  ╚═"))
    elif inp.strip() == "6":
      terminal_reset()
      sys.exit()
    else:
      w("{}{}{}{}{}".format(chr(27), "[1A", chr(27), "[2K", " [ 6 :Quit                 ]═════════╝  ╚═"))
      continue

