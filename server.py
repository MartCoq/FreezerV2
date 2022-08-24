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

    # afficher la playlist de l'utilisateur
    def liste(self,usr):
        self.cur.execute("SELECT artist,titre FROM playlists INNER JOIN users ON user_id = playlist_user_id INNER JOIN musics ON music_id = playlist_music_id WHERE user = ?;", (usr,))
        return self.cur

    # ajouter une musique a la table musics (APRES YOUTUBE-DL)
    def ajouterMusic(self,artist,title):
        self.cur.execute("INSERT INTO music (artist,title) VALUES (?,?)",(artist,title))
        self.conn.commit()

    # ajouter une chanson a la table playlists (APRES REQUETE UTILISATEUR D'UNE MUSIQUE DEJA DANS LE SERVEUR OU YOUTUBE-DL)
    def ajouterMusic(self,usr,artist,title):
        self.cur.execute("SELECT user_id FROM users WHERE user = ?;", (usr,))
        for i in self.cur:
            usr_id=i
        self.cur.execute("SELECT music_id FROM musics WHERE artist = ? AND title = ?;", (artist,title))
        for j in self.cur:
            music_id=j
        self.cur.execute("INSERT INTO playlists (playlist_user_id,playlist_music_id) VALUES (?,?)",(usr_id,music_id))
        self.conn.commit()
        return self.cur

    # ajouter un user dans users et passwd dans security (CREATION DE COMPTE OU LOGIN)
    def ajouterUser(self,usr,passwd):
        self.cur.execute("INSERT INTO users (user) VALUES (?)",(usr,))
        self.cur.execute("SELECT user_id from users WHERE user = ?",(usr,))
        for i in self.cur:
            user_id=i
        self.cur.execute("INSERT INTO security (passwd) VALUES (?) WHERE security_user_id = ? ",(passwd,user_id))
        self.conn.commit()

    # supprimer une musique de la playliste de l'utilisateur (MISE A JOUR PLAYLIST UTILISATEUR)
    def supprimer(self,usr,artist,title):
        self.cur.execute("DELETE FROM playlists INNER JOIN musics ON playlist_music_id = music_id INNER JOIN users ON playlist_user_id = user_id WHERE user = ? artiste = ? AND title = ?",(usr,artist,title))
        self.conn.commit()

    # modifier le nom de l'utilisateur (MODIFICATION NOM D'UTILISATEUR)
    def modifierUser(self,usr):
        self.cur.execute("UPDATE users SET user = ? ",(usr))
        self.conn.commit()

    # modifier le mot de passe de l'utilisateur dans security (MODIFICATION MOT DE PASSE)
    def modifierPasswd(self,usr,passwd):
        self.cur.execute("SELECT user_id from users WHERE user = ?",(usr,))
        for i in self.cur:
            user_id=i
        self.cur.execute("UPDATE security SET passwd = ? WHERE security_user_id = ? ",(passwd,user_id))
        self.conn.commit()

############################################################################
# ON EN EST LA !                                                           #
# FAUT-IL PREVOIR UNE DEFINITION POUR AFFICHER LE COUPLE USER + PASSWORD ? #
# RELIRE LA CLASSE SERVEUR                                                 #
############################################################################

class Server():
    def __init__ (self, host , port):
        self.HOST=host
        self.PORT=port
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)
        self.db = Maria("music","music","10.125.24.52",3306,"music")

    # attendre une connexion client (deja pret pour multhreading)
    def wait(self):
        con, addr = self.s.accept()
        print('Connected by', addr)
    
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
            result =re.search("^([a-z0-9\-@]+) ?([0-9]+)? ?([0-9\.A-z]+)? ?([A-z\-]+)?$",data)
            if result.group(1) == "list":
                get=self.db.liste()
                ret="\n"       
            elif result.group(1) == "afficher" and result.group(2):
                get = self.db.afficher(result.group(2))      
                ret="\n"   

            elif result.group(1) == "ajouter" and result.group(2) and result.group(3) and result.group(4):
                
                if re.search("^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",result.group(3)):
                    self.db.ajouter(result.groups())
                    get="OK"
                else:
                    get="format ip invalide"
            elif result.group(1) == "supprime" and result.group(2) and result.group(3):
                self.db.supprimer(result.group(2),result.group(3))
                get="OK"  

            else:
                get="commande inconnue "
                
            msg=""
            for i in get:
                msg+=str(i)+ret

            # on envoie une reponse au client
            con.sendall(msg.encode())

        # quand le client ferme la connexion
        con.sendall("exit".encode())

serv = Server("127.0.0.1",int(sys.argv[1]))
serv.wait()
print("server closed ")   
