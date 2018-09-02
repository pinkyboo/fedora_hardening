#!/bin/env python2.7

import os, sys
import os.path as path


# Define function to go back to menu [clear screen & move cursor up ]
def back_to_menu():
   os.system("tput reset")
   parent_path = path.abspath(path.join(__file__ ,"../.."))
   os.system(parent_path + "/start.py")


def iptables_establish(iface):
   ############<-- IPv4 -->###############
   # Delete all existing rules and classes
   os.system("iptables -F && iptables -X") 
   os.system("iptables -P INPUT DROP && iptables -P FORWARD DROP && iptables -P OUTPUT ACCEPT")

   # Drop all input let only conform packets trough
   os.system("iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")

   # Block [NULL] Packets
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags ALL FIN,URG,PSH -j DROP")
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags ALL ALL -j DROP")
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags ALL NONE -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix 'NULL Packets'")

   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags ALL NONE -j DROP")
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")

   # Block [XMAS] Packets
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags SYN,FIN SYN,FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix 'XMAS Packets'")
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")

   # Block [FIN] Packets Scan
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags FIN,ACK FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix 'FIN Packets Scan'")
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags FIN,ACK FIN -j DROP")

   # Block other common pits
   os.system("iptables -A INPUT -i " + iface + " -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP")


   # Enable logging for all IPv4 traffic
   os.system("iptables -A INPUT -j LOG && iptables -A FORWARD -j LOG && iptables -A OUTPUT -j LOG")


def ip6tables_establish():
   ############<-- IPv6 -->###############
   # Delete all existing rules and classes
   os.system("ip6tables -F && ip6tables -X")


   # Drop all IPv6 traffic
   os.system("ip6tables -P INPUT DROP && ip6tables -P FORWARD DROP && ip6tables -P OUTPUT DROP")


# Ask if common firewall shall be established
print("{}{}{}{}{}".format(chr(27), "[1m", "Setup Iptables Firewall against common attacks?", chr(27), "[0m"))
while 1:
    inp = raw_input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      intr = raw_input("On which interface I should setup Iptables? ")
      iptables_establish(intr)
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


# Ask if IPv6 shall be disabled
print("{}{}{}{}{}".format(chr(27), "[1m", "Disable IPv6 completely? [RECOMMENDED]", chr(27), "[0m"))
while 1:
    inp = raw_input("[Y/N] [M]enu [Q]uit ").lower()
    if inp.strip() == "y":
      ip6tables_establish()
      break
    elif inp.strip() == "n":
      break
    elif inp.strip() == "m":
      back_to_menu()
      sys.exit()
    elif inp.strip() == "q":
      os.system("tput reset")
      sys.exit
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

