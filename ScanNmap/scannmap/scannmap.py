#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 08/07/2017, 00:42:38

# Nesse script vai listar todos os dados encontrados.
# Pode remover print str(v), nesse caso vai exibir a lista de ips e macs da rede.
import nmap

macs = {'C4:36:6C:65:A8:9E':'Televisão', '04:4B:ED:72:22:F2':'Verônica', 'E4:9A:79:1B:E1:DD':'Gleison', 
'90:8D:6C:72:96:FC':'Ipad', '00:01:02:03:04:05':'Arduino', '40:16:7e:9f:71:1c':'Asus', '64:31:50:FF:0B:39':'Servidor',
'4C:D0:8A:AB:18:7C':'Roteador'}

nm = nmap.PortScanner()
cidr2='192.168.0.1-254'

a=nm.scan(hosts=cidr2, arguments='-sP')

for k,v in a['scan'].iteritems():
    #if str(v['status']['state']) == 'up':
        #print str(v)
    try:
        endMac = str(v['addresses']['mac'])
        if macs.has_key(endMac):
                print macs[endMac]
        elif endMac != macs:
            print endMac
    except: print 'Este dispositivo' 
