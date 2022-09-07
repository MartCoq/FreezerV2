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

    # ajouter un user dans users et passwd dans security (CREATION DE COMPTE OU LOGIN)
    def ajouterUser(self,usr,passwd):
        self.cur.execute("INSERT INTO users (user_name) VALUES (?) ;",(usr,))
        self.cur.execute("SELECT user_id FROM users WHERE user_name = ? ;", (usr,))
        for i in self.cur:
            userId = i[0]
        self.cur.execute("INSERT INTO security (user_id, password) VALUES (?,?) ;",(userId, passwd))
        self.conn.commit()
        return self.cur

DBFreezer=Maria("root","root","192.170.0.50",3306,"freezer")
DBFreezer.ajouterUser("ROMAIN","ROMAIN")
