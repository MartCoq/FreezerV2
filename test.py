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

    # afficher la playlist de l'utilisateur
    def liste(self,usr):
        print("coucou")
        self.cur.execute("SELECT artiste,titre FROM playlists INNER JOIN users ON users.user_id = playlists.user_id INNER JOIN music ON music.music_id = playlists.music_id WHERE users.user_name = ?;", (usr,))
        for i in self.cur:
            print(i)
        return self.cur

DBFreezer=Maria("freezer","freezer","10.125.24.50",3306,"freezer")
DBFreezer.liste("ROMAIN")
