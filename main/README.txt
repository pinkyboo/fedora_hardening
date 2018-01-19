

	 	     +------------------------+
  		     |                       ||
                     |   |FEDORA HARDENING|  ||
                     |_________v.2.5_________||
                     +========================+


     Table Of Contents…
 +-------------------------+      
 |                         | 
 | 1 :Introduction         |                                  
 | 2 :View On Hardening    |    ZZZ   ZZZ                     
 | 3 :Strategies           |     ZZZ ZZZ   HARDENING SHELL       
 | 4 :Hardes               |       ZZZ                        
 | 5 :Programs             |     ZZZ ZZZ   ANTI SPLOIT 2.5…  
 | 6 :Details And Patterns |    ZZZ   ZZZ  BY PINKYBOO__  
 |                         |                                   
 +-------------------------+          



 |:INTRODUCTION|
 +-------------+

 This tool is made to strengthen security. With a special 
 focus on home computers. The actual implemented tools are 
 specifically built to harden the kernel, connections and
 blacklist modules. Don't use it on other distros then Fedora.

 NOTICE: This isn't a all in one solution!



 |:VIEW ON HARDENING|
 +------------------+

 It's very important to take a closer look on hardening strategies
 and securing connections. The provided scripts are aiming on 
 common exploits and maybe zero days.
 
 The definition of hardening includes different strategies.
 1: Successfull hardening includes deletion of unused software.
 2: Check outbounded and incoming connections
 3: Groups and users secured and dynamic.
 4: Avoid unauthorized access
 5: Clean the system weekly
 6: Hardening yourself
 7: Avoid startup infections
 8: Avoid loading of zero RAM


 |:3 Strategies|
 +-------------+

 Deletion of unused software…
 is always recommended but not easy everytime. Most programs have
 huge dependencies. That alone is enough to resign when looking 
 trough all packages multiple hours. So the strategy of purely 
 deleting needs to  be modified and will become more a 
 'Look of what needs to be newly installed'.

 NOTICE: Every installed software may build up new dependencies.
         Installing is always easy. Deleting is much more difficult.
         Sometimes empty folders will left behind. The system gets 
         automatically dirtier from time to time.
 

 Securing Connections…
 will happen with the main tool, in linux. Iptables makes a big 
 difference in securing the main weak points. Nothing is better 
 than a good firewall. There are no limits. Everything can be done. 
 From logging of packets, disabling ports, avoid spoofing, 
 banning scanners, ... . For deeper understanding of a very 
 important field of security one should read all about the Iptables 
 tool and it's tips and tricks.
  
 TIP: For browsing the Net, when only some textual information 
      is needed, use Lynx. This little browser comes as terminal 
      application and don't shows pictures nor uses Javascript. 
      Just work with it for some time it's lovely!


 Groups and users…
 need always be secured with strong passwords. In this aspect Fedora also comes
 with some very good tools itself, which don't need to be modified. Next to 
 strong passwords, there is the ability to change them after a period of
 time. When the password is expired a new one needs to be created. 
 The code for this option will listed down below.
 Never write down passwords or hand them over to others.
 
          +---------------------------------+
          |# chage -M <days> <user>         |
          +---------------------------------+
          +---------------------------------+
 Example: |# chage -M 3 pinkyboo            | This will force the user pinkyboo to
          +---------------------------------+ change the password every three days


 Unauthorized access…
 is dangerous. Such access could come over remote services like SSH or onboard 
 unsecured accounts. So every user needs a strong password and the option 
 'PermitRootLogin' in the SSH configuration file needs to be disabled if not used.
 In Fedora you ca do that, like showed below.
 
 +--------------------------------+
 |# vi /etc/ssh/sshd_config       |
 +--------------------------------+
 +--------------------------------+
 |# Authentication:               |
 |                                |
 |#LoginGraceTime 2m              |
 |PermitRootLogin yes  <--        | Change from yes to no and save
 |#StrictModes yes                | the new code.
 |MaxAuthTries 2                  |
 |MaxSessions 1                   |
 +--------------------------------+


                               +- Additional -+
                               +--------------+

 +--------------------------------------------------------------+
 |# vi /etc/ssh/sshd_config                                     |
 +--------------------------------------------------------------+
 +--------------------------------------------------------------+
 |# To disable tunneled clear text passwords, change to no here!|
 |#PasswordAuthentication yes                                   | Remove '#' to block
 |#PermitEmptyPasswords no    <--                               | clear passwords via
 |PasswordAuthentication yes                                    | tuneled connection
 +--------------------------------------------------------------+


 Cleaning the system…
 weekly is important when you remove software. The best is to locate packages
 via the command 'locate'. Never think it's enough to remove with 'dnf'. Often
 not all files and folders will be removed. To provide an example down below is
 a list of remaining firefox packets.
 
 Example: 
 +---------------------------------------------------------------------------------+
 |# dnf remove firefox					         		   |
 +---------------------------------------------------------------------------------+
 +---------------------------------------------------------------------------------+
 |Abhängigkeiten sind aufgelöst.				      	           |
 |=================================================================================|
 | Paket                  Arch          Version                 Paketquelle   Größe|
 |=================================================================================|
 |Entfernen:									   |
 | firefox                x86_64        57.0.1-1.fc27           @updates      197 M|
 |Entferne ungültige Abhängigkeiten:						   |
 | u2f-hidraw-policy      x86_64        1.0.2-5.fc27            @fedora        36 k|
 |										   |
 |Transaktionsübersicht								   |
 |=================================================================================|
 |Entfernen  2 Pakete								   |
 |                           							   |
 |Freigegebener Speicherplatz: 197 M                                               |
 +---------------------------------------------------------------------------------+
 +---------------------------------------------------------------------------------+
 |root@x~# locate -c firefox			 				   |
 |186 packages found!								   |
 +---------------------------------------------------------------------------------+

 Now the hard work begins on searching whats needed and what's not by other programs.
 To avoid this nasty part of administration don't install new programs. You know
 best what's really needed and not.
 See :3.1 Strategies (Deleting unused software…).


 Hardening yourself…
 includes steps to change the behaviour and interaction in terms of computers
 and software. Don't click on everything while online. Avoid JavaScript while
 browsing the internet. Avoid allowing guests to use the computer with root 
 privileges. Secure Bootloader and BIOS. Disallow booting from CD, DVD or Stick. 
 Disallow automatic detection of such mediums while the computer runs. 
 Think about  what is safe and what should never be done. Scan E-Mail attachments.


 Avoid startup exploiting…
 means to avoid clear passwords in BIOS, to start system services which aren't
 necessary for normal computing. This includes printer services, bluetooth,
 modemmanager, remote services, … . The command 'systemctl' is the tool,
 you need for that job. To list all running services…
 
 +----------------------------+
 |# systemctl list-unit-files |
 +----------------------------+
 +--------------------------------------------------------+
 |# systemctl list-unit-files | grep -e enabled -e static |
 +--------------------------------------------------------+

 Avoid loading of zero RAM…
 is disabled by default in Fedora 27. So there isn't anything to do. But learning
 something about zero RAM exploitation is recommended.



 | NOTEWORTHY LINKS|
 +-----------------+

Checklist to avoid common security risks
https://www.stigviewer.com/stig/red_hat_enterprise_linux_6


Fedora Security Wiki
https://www.fedoraproject.org/wiki/Security


Official Security PDF Document from Fedora
https://docs.fedoraproject.org/en-US/Fedora/17/html/Security_Guide/chap-Security_Guide-Basic_Hardening.html



