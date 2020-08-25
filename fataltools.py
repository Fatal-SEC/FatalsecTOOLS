# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import webbrowser
import banner
import time
mensagem = 'escolha alguma coisa'
print(mensagem)

print('\033[31m'+'''
[1] MENU DE FERRAMENTAS DDOS
[2] Consultar operadora de número 
[3] pacotes de travas (não tem nada)
[4] script para assustar pessoas
[5] Site para spam de SMS
[6] Ping no IP/URL
[7] Phishings (limitado)
[8] Sair
[9] Ip Loggers
[10] Creditos
[11] entre em contato comigo
\033[0;0m''')
while True:
    option = int(input('digite o número da ferramenta: '))
    if option == 1: 
      print 'abrindo menu de DDOS/DOS'
      time.sleep(3) # delay de 3 sec
      os.system('clear')
      import ddos 
      break
    if option == 2:
      print '\033[1;92m'+'irá abrir uma page com o site de consulta, adiciona o número sem o 55.'+'\033[0;0m' 
      time.sleep(3) # delay de 3 sec
      webbrowser.open('https://consultaoperadora.com.br/site2015/')
      break    
    if option == 3:
      print '\033[1;92m'+'Irá abrir suas travas, seu zé travinha fodido'+'\033[0;0m' 
      webbrowser.open('https://pastebin.com/WK8xDVcM')
      break
    if option == 4:
     import Darknetools
     break
    if option == 5:
      print '\033[1;92m'+'configure o número e selecione se quer RAPIDO(fast) MEDIO(medium) ou LENTO(slow) e em seguida START ;)'+'\033[0;0m'
      time.sleep(3) # delay de 3 sec
      webbrowser.open('https://mytoolstown.com/smsbomber/#bestsmsbomber')
      break
    if option == 6:
      print '\033[1;92m'+'Iniciando ferramenta de DOS'+'\033[0;0m'
      time.sleep(2) # delay de 2 sec
      os.system('clear')
      import ipdos
      break
    if option == 7:
     print ""
     print '\033[1;95m'+'abrindo phishings :)'+'\033[0;0m'
     time.sleep(2) # delay de 2 sec  
     os.system('clear')
     import phishings
     break
    if option == 8:
     time.sleep(2) # delay de 2 sec
     print "até a próxima :)"
     quit()
     break
    if option == 9:
      print '\033[1;92m'+'Abrindo os IP loggers '+'\033[0;0m'
      time.sleep(2) # delay de 2 sec
      os.system('clear')
      import loggers
   
    if option == 10:
      print '\033[1;92m'+'obrigado :)'+'\033[0;0m'
      time.sleep(2) # delay de 2 sec
      os.system('clear')
      import thanks
    if option == 11:
      print '\033[1;92m'+'fale comigo para reportar algum erro ou dúvida :)'+'\033[0;0m'
      time.sleep(2) # delay de 2 sec
      os.system('clear')
      import cnt
      break
  
