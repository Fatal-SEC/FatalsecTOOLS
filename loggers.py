# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import webbrowser
import banner
import time
print '\033[1;92m'+'''

           .-=d88888888888b=-.
        .:d8888pr"|\|/-\|'rq8888b.
      ,:d8888P^//\-\/_\ /_\/^q888/b.
    ,;d88888/~-/ .-~  _~-. |/-q88888b,
   \8888888|// T      `    Y _/|888888 o
    \q88888|- \l           !\_/|88888p/
     'q8888l\-//\         / /\|!8888P'
       'q888\/-| "-,___.-^\/-\/888P'
         `=88\./-/|/ |-/!\/-!/88='
            ^^"-------------"^ 
'''+'\033[0;0m'
print('\033[31m'+'''
[1] IP LOGGER (recomendado)

[2] GRABIFY

[3] BLASZE
\033[0;0m''')
while True:
    option = int(input('digite um número, você será redirecionado para o site: '))
    if option == 1:
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'IP logger mostra informações da máquina, IP, provedora de internet e localização.'+'\033[0;0m'       
       time.sleep(3) # delay de 2 sec
       print '\033[1;92m'+'Pegue um link que seu alvo cairia, ele encurtará a URL com o logger e assim todos que clicarem terão seus Ips pegados(caso eles usem VPN não funcionará direito)'+'\033[0;0m'
       webbrowser.open('https://iplogger.org/')
       break
    if option == 2:
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'Grabify assim como IP logger mostra informações da máquina, IP, provedora de internet e localização.'+'\033[0;0m'       
       webbrowser.open('https://iplogger.org/')
       break
    if option == 3:
       time.sleep(3) # delay de 3 sec
       print '\033[1;92m'+'não é muito conhecido e está um pouco em desvantagem, porém tá ai'+'\033[0;0m'       
       webbrowser.open('https://blasze.com/')
       break
