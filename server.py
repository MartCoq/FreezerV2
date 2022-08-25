#! /usr/bin/python3

import socket
import mariadb
import sys
import re

# classe qui permet de se connecter a mariadb et d'envoyer/recevoir des messages
# amelioration : classe hétité de mariadb
class Maria():
    def __init__ (self,user,password,host,port,db):
        try:  
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db
                )
            
            # Get Cursor
            self.cur = self.conn.cursor()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
       

    # afficher toute la table music
    def listeAll(self):
        self.cur.execute("SELECT * FROM music;")
        return self.cur

   # afficher toute la table music
    def checkPresence(self,artiste,titre):
        self.cur.execute("SELECT * FROM music, WHERE artiste = ? AND titre = ?;", (artiste,titre))
        return self.cur

    # afficher la playlist de l'utilisateur
    def liste(self,usr):
        self.cur.execute("SELECT artist,titre FROM playlists INNER JOIN users ON users.user_id = playlists.user_id INNER JOIN music ON music.music_id = playlists.music_id WHERE users.user_name = ?;", (usr,))
        return self.cur

    # ajouter une musique a la table musics (APRES YOUTUBE-DL)
    def ajouterMusic(self,artist,title):
        self.cur.execute("INSERT INTO music (artiste,titre) VALUES (?,?)",(artist,title))
        self.conn.commit()
        return self.cur

    # ajouter une chanson a la table playlists (APRES REQUETE UTILISATEUR D'UNE MUSIQUE DEJA DANS LE SERVEUR OU YOUTUBE-DL)
    def ajouterMusicPlaylist(self,usr,artist,title):
        self.cur.execute("SELECT users.user_id FROM users WHERE users.user_name = ?;", (usr,))
        for i in self.cur:
            usr_id=i[0]
        self.cur.execute("SELECT music_id FROM music WHERE artiste = ? AND titre = ?;", (artist,title))
        for j in self.cur:
            music_id=j[0]
        self.cur.execute("INSERT INTO playlists (playlists.user_id,playlists.music_id) VALUES (?,?)",(usr_id,music_id))
        self.conn.commit()
        return self.curACTIONS

    # ajouter un user dans users et passwd dans security (CREATION DE COMPTE OU LOGIN)
    def ajouterUser(self,usr,passwd):
        self.cur.execute("INSERT INTO users (user) VALUES (?)",(usr,))
        self.cur.execute("INSERT INTO security (password) VALUES (?) ",(passwd,))
        self.conn.commit()
        return self.cur

    # supprimer une musique de la playliste de l'utilisateur (MISE A JOUR PLAYLIST UTILISATEUR)
    def supprimer(self,usr,artist,title):
        self.cur.execute("DELETE playlists FROM playlists INNER JOIN music ON playlists.music_id = music.music_id INNER JOIN users ON playlists.user_id = users.user_id WHERE user_name = ? artiste = ? AND titre = ?",(usr,artist,title))
        self.conn.commit()
        return self.cur

    # modifier le nom de l'utilisateur (MODIFICATION NOM D'UTILISATEUR)
    def modifierUser(self,usr,oldUsr,passwd):
        self.cur.execute("SELECT user_name, password FROM users INNER JOIN security ON users.user_id = security.user_id WHERE user_name = ? AND password = ?",(oldUsr,passwd))
        for i in self.cur:
            if i == (oldUsr,passwd):
                self.cur.execute("SELECT user_id from users WHERE user_name = ?;", (oldUsr,))
                for j in self.cur:
                    userId=j[0]
                self.cur.execute("UPDATE users SET user_name = ? WHERE user_id = ?",(usr,userId))
                self.conn.commit()
                return self.cur
            else:
                print("Mauvais utilisateur")

    # modifier le mot de passe de l'utilisateur dans security (MODIFICATION MOT DE PASSE)
    def modifierPasswd(self,usr,oldPasswd,passwd):
        self.cur.execute("SELECT user_id from users WHERE user = ?",(usr,))
        for i in self.cur:
            user_id=i[0]
        self.cur.execute("SELECT user_name, password FROM users INNER JOIN security ON users.user_id = security.user_id WHERE user_name = ? AND password = ?",(usr,oldPasswd))
        for j in self.cur:
            if j == (usr,oldPasswd):
                self.cur.execute("UPDATE security SET password = ? WHERE security_user_id = ? ",(passwd,user_id))
            else:
                print("Mauvais identifiants")
        self.conn.commit()
        return self.cur

    # afficher utilisateur et mot de passe
    def afficherUser(self,usr,passwd):
        self.cur.execute("SELECT user passwd FROM users INNER JOIN security ON user_id = security_user_id WHERE user = ? AND passwd = ?",(usr,passwd))
        return self.cur

class Server():
    def __init__ (self, host , port):
        self.HOST=host
        self.PORT=port
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)
        self.db = Maria("freezer","freezer","10.125.24.50",3306,"freezer")
        self.clientAddr=""

    # attendre une connexion client (deja pret pour multhreading)
    def wait(self):
        con, addr = self.s.accept()
        print('Connection from', addr)
        self.clientAddr=addr
        self.conn(con,addr)
    
    # fonction qui gere 1 client connecté
    def conn(self,con,addr):
        client = True
        while client == True:

             # on recoit le message du client
            data = con.recv(1024).decode()
            print(addr,": ", data)
            print()
            ret=""

            # on traite le message et on cherche dans la bdd
            if  data == "quit()" :
                break
            # result =re.search("^([a-z0-9\-@]+) ?([0-9]+)? ?([0-9\.A-z]+)? ?([A-z\-]+)?$",data)
            # if result.group(1) == "list":
            #     get=self.db.liste()
            #     ret="\n"       
            # elif result.group(1) == "afficher" and result.group(2):
            #     get = self.db.afficher(result.group(2))      
            #     ret="\n"   

            # elif result.group(1) == "ajouter" and result.group(2) and result.group(3) and result.group(4):
                
            #     if re.search("^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",result.group(3)):
            #         self.db.ajouter(result.groups())
            #         get="OK"
            #     else:
            #         get="format ip invalide"
            # elif result.group(1) == "supprime" and result.group(2) and result.group(3):
            #     self.db.supprimer(result.group(2),result.group(3))
            #     get="OK"  

            # else:
            #     get="commande inconnue "
            get="OK"
            msg=""
            for i in get:
                msg+=str(i)+ret

            # on envoie une reponse au client
            con.sendall(msg.encode())

        # quand le client ferme la connexion
        con.sendall("exit".encode())

##### MESSAGE RECU PAR LE SOCKET
#####        msg1=" messeage:"+user+" "+passwd+" "+action+" "+NewUser+"? "+NewPasswd+"?  "+titre+"? "+artiste+"? " # AJOUTER "+presence+" POUR LA PRESENCE DU FICHIER EN LOCAL ET RETIRER "+server+" INUTILE

#####
# 1 # Création de compte if action = register
#####

message="MARTIN MARTIN register"

user=message.split(" ")[0]
password=message.split(" ")[1]
ACTIONS=message.split(" ")[2]

DBFreezer=Maria("freezer","freezer","10.125.24.50",3306,"freezer")

if ACTIONS == "register":
    DBFreezer.ajouterUser(user,password)
elif ACTIONS == "PWDUpdate":
    newPassword=message.split(" ")[3]
    DBFreezer.modifierPasswd(user,password,newPassword)
elif ACTIONS == "USERUpdate":
    newUser=message.split(" ")[3]
    DBFreezer.modifierUser(newUser,user,password)
elif ACTIONS == "show":
    if DBFreezer.afficherUser(user,password) == (user,password):
        DBFreezer.liste(user)
    else:
        print("Mauvais identifiants")
elif ACTIONS == "showALL":
    if DBFreezer.afficherUser(user,password) != "":
        DBFreezer.listeALL(user)
    else:
        print("Mauvais identifiants")
elif ACTIONS == "play":
    artiste=message.split(" ")[3]
    titre=message.split(" ")[4]
    presence=message.split(" ")[5]
    if DBFreezer.afficherUser(user,password) == (user,password):
        if presence == "OUI":
            if DBFreezer.checkPresence(artiste,titre):
                print("Présent dans la playlist")
else:
    print("action n existe pas")

serv=Server("10.125.24.50",69)
serv.wait()
print("server closed ")
