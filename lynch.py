from time import sleep
import os, sys
import subprocess

# cores
n = '\033[m' #normal
r = '\033[1;31m' #vermelho
rf = '\033[31m' #vermelho fraco
g = '\033[1;32m' #verde
y = '\033[33m' #amarelo
b = '\033[34m' #azul
p = '\033[35m' #roxo

def animacao(cor=g):
      frase = f'{cor}###########################{n}\n'
      for i in list(frase):
            print(i, end='')
            sys.stdout.flush()
            sleep(0.1)

def banner():
    print(f"""{g}
    LL     YY   YY   NNNN    NN   CCCCCCC   HH   HH
    LL      YY  YY   NN NN   NN   CC        HH   HH
    LL        YYYY   NN  NN  NN   CC        HHHHHHH
    LL          YY   NN   NN NN   CC        HH   HH
    LLLLLLLL    YY   NN    NNNN   CCCCCCC   HH   HH {n}
    """)

banner()