# -*- coding: cp1254 -*-
#Modül İşlemleri
import time
from socket import *

#Giriş
print """PorScan
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Port Tarama Yazılımı                 | karaayaz_"""
print ""
print "Operasyon Başlangıç Saati:"+" "+time.strftime("%H:%M:%S")
print "/"*60

#Bilgi İste & Bilgi Ver
vict = raw_input("Hedef Site: ")
if "http://" in vict:
    victim=vict.replace("http://", "")   
else:
    victim = vict
    
victimIP = gethostbyname(victim)
print 'Hedef Site Ip Adres: ', victimIP
print "~"*60

# Operasyon Sahası
for port in range(20, 1025):
    giris = socket(AF_INET, SOCK_STREAM)
    result = giris.connect_ex((victimIP, port))
    if(result == 0):
        print "Port %d: AÇIK!" %(port,)
        print "\t Bulma Zamanı:"+" "+time.strftime("%H:%M:%S")
        print "~"*60
    giris.close()

print "Operasyon Tamamlanmıştır."
print "~~~~~~~ Kara Ayaz ~~~~~~~"
