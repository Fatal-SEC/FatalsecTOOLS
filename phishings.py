# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import webbrowser
import banner
import time
mensagem = 'escolha alguma ferramenta'
print(mensagem)

print '\033[1;92m'+'''


 _________         .    .
(..       \_    ,  |\  /|
 \       O  \  /|  \ \/ /
  \______    \/ |   \  / 
     vvvv\    \ |   /  |
     \^^^^  ==   \_/   |
      `\_   ===    \.  |
      / /\_   \ /      |
      |/   \_  \|      /
             \________/
'\033[31m'+'''

time.sleep(2) # delay de 2 segundo
print('\033[31m'+'''
[1] Weeman

[2] Hideen Eye (possui erros)

[3] Zphisher

em breve outra versão dessa ferramenta ;)
\033[0;0m''')

while True:
    option = int(input('digite o número da ferramenta: '))
    if option == 1:
       time.sleep(3) # delay de 3 sec
       print '\033[1;94m'+'Weeman, você terá que escolher qual alvo será o phishing.'+'\033[0;0m'       
       os.system("git clone https://github.com/evait-security/weeman" )
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'use Python2 weeman.py ;)'+'\033[0;0m'
       break
    if option == 2:
       time.sleep(3) # delay de 3 sec
       print '\033[1;94m'+'HiddenEye é automatizada com Localhost e Ngrok e com bastante templates, porem possui erros :/'+'\033[0;0m'       
       os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye")
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'use python3 HiddenEye.py ;)'+'\033[0;0m'
       break
    if option == 3:
       time.sleep(3) # delay de 3 sec
       print '\033[1;94m'+'Zphisher é automatico e não possui tantos erros, possui templates legais!'+'\033[0;0m'       
       os.system("git clone https://github.com/htr-tech/zphisher")
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'use bash zphisher.sh ;)'+'\033[0;0m'
       break
