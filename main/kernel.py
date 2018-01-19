#!/bin/env python3

import sys, os
import os.path as path


# Define function to go back to menu [clear screen & move cursor up ]
def back_to_menu():
      os.system("tput reset")
      parent_path = path.abspath(path.join(__file__ ,"../.."))
      os.system(parent_path + "/start.py")


# Define function to set kernel parameters
def kernel_parameters():
      os.system("sysctl -w net.ipv4.conf.all.send_redirects=0 && sysctl -w net.ipv4.conf.default.accept_redirects=0")
      os.system("sysctl -w net.ipv4.conf.default.send_redirects=0 && sysctl -w net.ipv4.icmp_echo_ignore_all=1")
      os.system("sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1 && sysctl -w net.ipv4.icmp_echo_ignore_all=1")
      os.system("sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1 && sysctl -w net.ipv4.tcp_syncookies=1")
      os.system("sysctl -w net.ipv4.conf.all.accept_redirects=0 && sysctl -w net.ipv4.conf.all.log_martians=1")
      os.system("sysctl -w net.ipv4.conf.default.log_martians=1 && sysctl -w net.ipv4.tcp_timestamps=0")
      os.system("sysctl -w kernel.randomize_va_space=2 && sysctl -w net.ipv4.conf.all.rp_filter=1")
      os.system("sysctl -w kernel.dmesg_restrict=1 && sysctl -w kernel.kptr_restrict=2")
      os.system("sysctl -w kernel.ctrl-alt-del=0 && sysctl -w net.ipv4.ip_forward=0")
      os.system("sysctl -w kernel.sysrq=0 && sysctl -w kernel.core_uses_pid=1")
      os.system("sysctl -w net.ipv6.conf.default.accept_redirects=0")
      os.system("sysctl -w net.ipv4.conf.all.accept_source_route=0")
      os.system("sysctl -w net.ipv6.conf.all.accept_redirects=0")


# Ask if user wants to set kernel parameters
print("{}{}{}{}{}".format(chr(27), "[1m", "Kernel Setup Option Tool", chr(27), "[0m"))
while 1:
    inp = input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      kernel_parameters()
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
    inp = input("[M]enu [Q]uit ").lower()
    if inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue

