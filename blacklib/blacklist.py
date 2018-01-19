#!/bin/env python3

import time, shutil, os, sys
import os.path as path

# Print what the program does
print("This tool will help you to blacklist vulnerable modules.")

time.sleep(0.5)

# Define function to go back to menu [clear screen & move cursor up ]
def back_to_menu():
      os.system("tput reset")
      parent_path = path.abspath(path.join(__file__ ,"../.."))
      os.system(parent_path + "/start.py")


# Ask if Firewire module shall be blocked
print("{}{}{}{}{}".format(chr(27), "[1m", "Disable the Firewire module?", chr(27), "[0m"))
while 1:
    inp = input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      shutil.copyfile("./blacklist-firewire.conf" "/etc/modprobe.d/blacklist-firewire.conf")
    elif inp.strip() == "n":
      break
    elif inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue


# Ask if auto detection of usb-sticks shall be blocked
print("{}{}{}{}{}".format(chr(27), "[1m", "Disable automatic detection of usb-sticks?", chr(27), "[0m"))
while 1:
    inp = input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      shutil.copyfile("./blacklist-auto-usb.conf" "/etc/modprobe.d/blacklist-auto-usb.conf")
    elif inp.strip() == "n":
      break
    elif inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue


# Ask if types of raw connections shall be blocked
print("{}{}{}{}{}".format(chr(27), "[1m", "Disable raw connection modules?", chr(27), "[0m"))
while 1:
    inp = input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      shutil.copyfile("./blacklist-raw-connections.conf" "/etc/modprobe.d/blacklist-raw-connections.conf")
    elif inp.strip() == "n":
      break
    elif inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()      
    else:
      continue


while 1:
    inp = input("[M]enu [Q]uit ").lower()
    if inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue

