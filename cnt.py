# -*- coding: utf-8 -*-
import os
import webbrowser
import time
print('\033[31m'+'''
░▒▓██████████►╬◄██████████▓▒░
░▒▓██►    1 TWITTER    ◄██▓▒░
░▒▓██►    2 YOUTUBE    ◄██▓▒░
░▒▓██►    3 INSTAGRAM  ◄██▓▒░
░▒▓██████████►╬◄██████████▓▒░
\033[0;0m''')
while True:
    option = int(input('escolha por onde quer o contato: '))
    if option == 1:
       print '\033[1;92m'+'me chama na DM do Twitter po, eu respondo quando puder :)'+'\033[0;0m'       
       time.sleep(3) # delay de 3 sec
       webbrowser.open("https://twitter.com/net3dits")
       from sys import exit
       os.system('clear')
       import teste1
       break
    if option == 2:
       print '\033[1;92m'+'da uma passada la no meu canal po! :)'+'\033[0;0m'       
       time.sleep(3) # delay de 3 sec
       webbrowser.open("https://www.youtube.com/channel/UCYFC0nvMkMT9TnJ_Tadeq-g")
       from sys import exit
       os.system('clear')
       import teste1
       break
    if option == 3:
       print '\033[1;92m'+'meu insta :)'+'\033[0;0m'       
       time.sleep(3) # delay de 3 sec
       webbrowser.open("https://www.instagram.com/net3ditsbrabo/")
       os.system('clear')
       import teste1
       break
