# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:14:34 2021

@author: ahmet
"""

#########################
##                     ##
##  TCP CLIENT SOCKET  ##
##                     ##
#########################


import socket

kimlik = input("bir kullanıcı adı belirleyiniz: ")

# socket oluşturma

client_socket = socket.socket()


# server sockete bağlanıyoruz.


client_socket.connect(("localhost", 50001))

print(kimlik, "ile server arasında bağlantı kuruldu")
mesaj = input("Client-01: ")

client_socket.send(bytes(kimlik+": "+mesaj, 'utf-8'))


    
