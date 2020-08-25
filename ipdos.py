# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import webbrowser
import time

print '\033[31m'+'''
██╗██████╗     ██████╗ ██╗███╗   ██╗ ██████╗ 
██║██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ 
██║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗
██║██╔═══╝     ██╔═══╝ ██║██║╚██╗██║██║   ██║
██║██║         ██║     ██║██║ ╚████║╚██████╔╝
╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
FATALSEC TOOLS                                           

'''

ip = raw_input ('\033[1;94m'+'digite o ip ou url: ')
time.sleep(3) # Sleep for 1 seconds
print '\033[1;92m'+'você irá pingar pacotes no '+'\033[0;0m' + ip 
print "la vai ;)"
time.sleep(1) # Sleep for 1 seconds
print '\033[1;92m'+''+'\033[0;0m'
os.system('ping ' + ip)
