#!/bin/env python

import sys, os, commands, time
import os.path as path


# Define function to go back to menu [clear screen & move cursor up ]
def back_to_menu():
    os.system("tput reset")
    parent_path = path.abspath(path.join(__file__ ,"../.."))
    os.system(parent_path + "/start.py")


# Define main function to disable multicasting
def multicast_disable():
    stack = commands.getoutput("ifconfig | grep 'MULTICAST' | awk -F: '{print $1;}'").splitlines()
    if len(stack) != 0:
      for index, item in enumerate(stack, start=1):
         for count in range(index):
            os.system("{}{}{}".format('ifconfig ', item, ' -multicast'))
            count+=1
            time.sleep(0.3)
            if count == index:
              print("{}{}{}".format("Success! Interface ", item, " changed!"))
    else:
      print("Nothing changed!")


# Userinput
print("{}{}{}{}{}".format(chr(27),"[1m", "Disable [MULTICAST] establishment?", chr(27), "[0m"))
while 1:
    inp = raw_input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      multicast_disable()
      break
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
    inp = raw_input("[S]how [M]enu [Q]uit ").lower()
    if inp.strip() == "s":
      os.system("ifconfig")
      break
    if inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue


while 1:
    inp = raw_input("[M]enu [Q]uit ").lower()
    if inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue

