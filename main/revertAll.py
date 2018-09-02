#!/bin/env python3

import shutil, os, sys
import os.path as path

def kernel_parameters():
      os.system("sysctl -w net.ipv4.conf.all.send_redirects=1 && sysctl -w net.ipv4.conf.default.accept_redirects=1")
      os.system("sysctl -w net.ipv4.conf.default.send_redirects=1 && sysctl -w net.ipv4.icmp_echo_ignore_all=0")
      os.system("sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=0 && sysctl -w net.ipv4.icmp_echo_ignore_all=0")
      os.system("sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=0 && sysctl -w net.ipv4.tcp_syncookies=0")
      os.system("sysctl -w net.ipv4.conf.all.accept_redirects=1 && sysctl -w net.ipv4.conf.all.log_martians=0")
      os.system("sysctl -w net.ipv4.conf.default.log_martians=0 && sysctl -w net.ipv4.tcp_timestamps=1")
      os.system("sysctl -w kernel.randomize_va_space=2 && sysctl -w net.ipv4.conf.all.rp_filter=0")
      os.system("sysctl -w kernel.dmesg_restrict=0 && sysctl -w kernel.kptr_restrict=2")
      os.system("sysctl -w kernel.ctrl-alt-del=1 && sysctl -w net.ipv4.ip_forward=1")
      os.system("sysctl -w kernel.sysrq=1 && sysctl -w kernel.core_uses_pid=0")
      os.system("sysctl -w net.ipv6.conf.default.accept_redirects=1")
      os.system("sysctl -w net.ipv4.conf.all.accept_source_route=1")
      os.system("sysctl -w net.ipv6.conf.all.accept_redirects=1")

print("{}{}{}{}{}".format(chr(27), "[1m", "Are you sure you want to revert all changes?", chr(27), "[0m"))
files = ["/etc/modprobe.d/blacklist-firewire.conf", "/etc/modprobe.d/blacklist-auto-usb.conf", "/etc/modprobe.d/blacklist-raw-connections.conf"]
while 1:
    inp = input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      os.system("iptables -F && iptables -X") 
      os.system("ip6tables -F && ip6tables -X")
      kernel_parameters()
      for filename in files:
      	if os.path.exists(filename):
         os.remove(filename)
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
    inp = raw_input("[M]enu [Q]uit ").lower()
    if inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit()
    else:
      continue
