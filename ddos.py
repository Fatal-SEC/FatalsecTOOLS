# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import webbrowser
import time

print '\033[1;96m'+'''
                                                
 ____  ____  _____ _____   _ ____  _____ _____ 
|    \|    \|     |   __| / |    \|     |   __|
|  |  |  |  |  |  |__   |/ /|  |  |  |  |__   |
|____/|____/|_____|_____|_/ |____/|_____|_____|
  Pacote de ferramentas DDOS/DOS                                             


                                         ''''\033[0;0m'
print "escolha uma ferramenta, lembrando que ela vai estar baixada na pasta da principal (fatalmultitools)"



print('\033[31m'+'''
[1] TORSHAMMER

[2] XERXES

[3] GOLDENEYE

[4] SLOWLORIS
\033[0;0m''')
while True:
    option = int(input('digite o número da ferramenta: '))
    if option == 1:
       print '\033[1;92m'+'Baixando TORSHAMMER, é uma ótima ferramenta de DOS!'+'\033[0;0m'       
       os.system("git clone https://github.com/dotfighter/torshammer")
       break
    if option == 2:
       print '\033[1;92m'+'Clonando XERXES!'+'\033[0;0m'       
       os.system("git clone https://github.com/CyberXCodder/XerXes")
       break
    if option == 3:
       print '\033[1;92m'+'Fazendo download do GOLDENEYE!'+'\033[0;0m'       
       os.system("git clone https://github.com/jseidl/GoldenEye")
       break
    if option == 4:
       print '\033[1;92m'+'Eu sempre usei slowloris, recomendo muito :)'+'\033[0;0m'       
       os.system("git clone https://github.com/gkbrk/slowloris")
       break
   
