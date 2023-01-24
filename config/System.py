import os, time


def reboot():
    time.sleep(2)
    os.system('python app.py')
content = '''\033[0;34m
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄█░▄▄▀█▀▄▀█░▄▄██░▄▄░█░█████▄██░▄▄█░████░▄▄█░▄▄▀
██░▄▄██░▀▀░█░█▀█░▄▄██░▀▀░█░▄▄░██░▄█▄▄▀█░▄▄░█░▄▄█░▀▀▄
██░████▄██▄██▄██▄▄▄██░████▄██▄█▄▄▄█▄▄▄█▄██▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;m'''

def playpage():
    loop = True
    nn = ''
    while len(nn) <= 2:
        os.system('clear')
        nn = nn+'.'
        print (content,'\nIniciando Pagina',nn)
        time.sleep(4)
def getdata():
    print ('Digite o id:')
    id = input(int())
    return id  