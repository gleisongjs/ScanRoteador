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
'90:8D:6C:72:96:FC':'Ipad', '00:01:02:03:04:05':'Sistema Layla', '5c:c9:d3:3a:d0:07':'Asus', '64:31:50:FF:0B:39':'Servidor',
'4C:D0:8A:AB:18:7C':'Roteador', 'E4:9A:79:1A:9C:14':'Reginaldo', 'E4:9A:79:23:CD:58':'Andressa', '28:83:35:11:35:5F':'Gleicielle',
'14:A3:64:27:FF:41':'Mãe', '30:C7:AE:B7:A2:A0':'Jonas', 'AC:5F:3E:A9:16:25':'Bruna Rubinger', '28:83:35:B1:F0:9D':'Gleiciane'}

dispositivosConhecidos = []
dispositivosDesconhecidos = []

#Autenticação do twitter
api = twitter.Api(consumer_key='ftH2lqxvH6eTdYlQi78wbusnp', 
consumer_secret='oLgaI8Ia9HwZ2gPjQItTNIRiQiHkgRsvs4IxNl3gUX00EJ2Kzp',
access_token_key='832896102366068736-YtZwU7fMsHLuWYPhZLktZug8oTx7ua6',
access_token_secret='wSNwxnqIeJYoyQZAATOPruT6NcoGizJY8ENrk7JUZ9qId')

#Buscando os dispositivos conectados da minha rede
nm = nmap.PortScanner()
cidr2='192.168.0.1-254'

a=nm.scan(hosts=cidr2, arguments='-sP')

for k,v in a['scan'].iteritems():
    try:
        endMac = str(v['addresses']['mac'])
        if macs.has_key(endMac):            
            dispositivo = macs[endMac]
            dispositivosConhecidos.append(dispositivo)
            #print dispositivo 
            aux = 1
        elif endMac != macs:
            dispositivo = endMac
            dispositivosDesconhecidos.append(dispositivo)
            #print desconhecido
            aux = 2
           
    except: print 'Este dispositivo' 

#jeito eficiente de concatenar string
dispositivosConhecidos = ', '.join(dispositivosConhecidos)
dispositivosDesconhecidos = ', '.join(dispositivosDesconhecidos)
#print dispositivosConhecidos
#print dispositivosDesconhecidos

#Twitando 
if aux == 1:
    status = api.PostUpdate('''@GleisonJSilva os seguintes dispositivos estão utilizando a rede: '''+dispositivosConhecidos)
    print status.text
elif aux==2:
    status = api.PostUpdate('@GleisonJSilva não conhecemos o dispositivo: '+ dispositivosDesconhecidos +' - Ele está utilizando a rede agora.')
    print status.text
   
