#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 08/07/2017, 00:42:38

# Nesse script vai listar todos os dados encontrados.
# Pode remover print str(v), nesse caso vai exibir a lista de ips e macs da rede.
import nmap
import twitter

#Dicionário de macs
macs = {'C4:36:6C:65:A8:9E':'Televisão', '04:4B:ED:72:22:F2':'Verônica', 'E4:9A:79:1B:E1:DD':'Gleison', 
'90:8D:6C:72:96:FC':'Ipad', '00:01:02:03:04:05':'Arduino', '40:16:7e:9f:71:1c':'Asus', '64:31:50:FF:0B:39':'Servidor',
'4C:D0:8A:AB:18:7C':'Roteador'}

#Autenticação do twitter
api = twitter.Api(consumer_key='ftH2lqxvH6eTdYlQi78wbusnp', 
consumer_secret='oLgaI8Ia9HwZ2gPjQItTNIRiQiHkgRsvs4IxNl3gUX00EJ2Kzp',
access_token_key='832896102366068736-YtZwU7fMsHLuWYPhZLktZug8oTx7ua6',
access_token_secret='wSNwxnqIeJYoyQZAATOPruT6NcoGizJY8ENrk7JUZ9qId')


nm = nmap.PortScanner()
cidr2='192.168.0.1-254'

a=nm.scan(hosts=cidr2, arguments='-sP')

for k,v in a['scan'].iteritems():
    #if str(v['status']['state']) == 'up':
        #print str(v)
    try:
        endMac = str(v['addresses']['mac'])
        if macs.has_key(endMac):            
            dispositivos = (macs[endMac])
            print dispositivos
            aux = 1
        elif endMac != macs:
            desconhecido = endMac
            aux = 2
    except: print 'Este dispositivo' 

if aux == 1:
    status = api.PostUpdate('''@GleisonJSilva os dispositivos estão utilizando a rede: '''+dispositivos)
    print status.text
elif aux==2:
    status = api.PostUpdate('@GleisonJSilva não conhecemos o dispositivo: '+ desconhecido +'- Ele está utilizando a rede agora.')
    print status.text
   
