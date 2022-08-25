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

    # modifier le nom de l'utilisateur (MODIFICATION NOM D'UTILISATEUR)
    def modifierUser(self,usr,oldUsr,passwd):
        self.cur.execute("SELECT user_name, password FROM users INNER JOIN security ON users.user_id = security.user_id WHERE user_name = ? AND password = ?",(oldUsr,passwd))
        for i in self.cur:
            print(i)
            if i == (oldUsr,passwd):
                self.cur.execute("SELECT user_id from users WHERE user_name = ?;", (oldUsr,))
                for j in self.cur:
                    userId=j[0]
                    print(userId)
                self.cur.execute("UPDATE users SET user_name = ? WHERE user_id = ?",(usr,userId))
                self.conn.commit()
                return self.cur

DBFreezer=Maria("freezer","freezer","10.125.24.50",3306,"freezer")
DBFreezer.modifierUser("ROMAIN","ROMAINE","ROMAIN")
