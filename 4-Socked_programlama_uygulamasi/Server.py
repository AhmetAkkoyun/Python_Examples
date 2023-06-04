# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:03:22 2021

@author: ahmet
"""

#########################
##                     ##
##  TCP SERVER SOCKET  ##
##                     ##
#########################


import socket

# socket oluşturma

server_socket = socket.socket()


server_socket.bind(("localhost", 50001))

# socketler dinlenmeye başlıyor
server_socket.listen(5)
print("socket oluşturuldu bağlantı bekleniyor.")

while True:
    client_socket, adres = server_socket.accept()
    print(adres, "adresli bilgisayarla bağlantı kuruldu")
    
    #client sistemden gelen mesajı ekrana yazdırıyoruz.
    gelen_mesaj = client_socket.recv(1021).decode()
    print(gelen_mesaj)
    
    client_socket.close()
    
    if gelen_mesaj == "exit":
        break

print("Tüm bağlantılar sonlandırıldı")
server_socket.close()