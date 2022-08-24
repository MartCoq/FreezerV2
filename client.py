#!/usr/bin/python 
# Module Imports
import mysql.connector as database
from ftplib import FTP
import subprocess, time
import sys
import os
import re
import random
import socket, threading
from random import sample



def handle_messages(connection: socket.socket):
    '''
        Receive messages sent by the server and display them to user
    '''

    #while True:
        #try:
            #msg = connection.recv(1024)

            # If there is no message, there is a chance that connection has closed
            # so the connection will be closed and an error will be displayed.
            # If not, it will try to decode message in order to show to user.
            #if msg:
            #    print(msg.decode())
            #else:
                #from server: {e}')
                #connection.close()
            #break

def client(lu):
    '''
        Main process that start client connection to the server 
        and handle it's input messages
    '''

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 13003

    try:
        # Instantiate socket and start connection with server
        #socket_instance = socket.socket()
        #socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        # Create a thread in order to handle messages sent by server
        #threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Connected to chat!')

        # Read user's input until it quit from chat and close connection
        #while True:
        
        msg =" ".join(lu[1:])

            #if msg == 'quit':
            #    break
        verdad=0
        musique=""
        musiqueok=""
        #    login=sys.argv[1]
        #    passwd=sys.argv[2]
        
        #Etapes avant boucle
        
        login=input("Quel est votre login ?")
        passwd=input("Quel est votre password ?")
        server=input("Quel est le serveur sur lequel il faut se connecter ?")
        boucle=True


        isIn=0
        cmd="ls ~/Musics"#"lftp {0}:{1}@{2} -e 'cls;quit'".format(login,passwd,server)
        list_music=os.popen(cmd).read().split("\n")
        print(list_music)
        test_zic=msg
        titre=test_zic.split(" ")[0]
        test_zic=test_zic.replace(" ","_")
        print(test_zic,titre)
        flag=0
        for i in list_music:
            if titre.upper() in i.upper():                
                flag=1                     
                musique=i
                print(musique)
                break  
        

        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
            # Parse message to utf-8
        socket_instance.send(msg.encode())
        print (socket_instance.recv(1024).decode())
        # Close connection with the server
        #socket_instance.close()
        #msg=socket.socket()
        mass=socket_instance.recv(1024).decode()
        #print(mass)
        #mass1=socket_instance.recv(1024).decode()
        #print(mass1)
        #with open("index1.html","w") as filout:
        #    for tot in mass1:
        #        tot=str(tot)+"\n"
        #        filout.write(tot)
        #print (socket_instance.recv(1024).decode())
        #print (socket_instance.recv(1024).decode())
        #print (socket_instance.recv(1024).decode())
        socket_instance.close()
    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    #if (sys.argv[1]=='remove'):
    #        nom_machine = sys.argv[2]
    #        vdm = sys.argv[3]
    #        print("chocolat")
    #elif (sys.argv[1]=='add'):
    #        nom_machine = sys.argv[2]
    #        IP_add = sys.argv[3]
    #        vdm = sys.argv[4]
    #        print(sys.argv[3])
    #elif (sys.argv[1]=='modify'):
    #        nom_machine = sys.argv[2]
    #        vdm = sys.argv[3]
    #        if re.match("--name",sys.argv[4]):
    #            new_name = sys.argv[4].split("=")[1]
    #elif (sys.argv[1]=='lister'):
    #        vdm = sys.argv[2]

    client(sys.argv)
