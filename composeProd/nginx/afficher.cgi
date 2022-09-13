#!/usr/bin/python3
import cgi, cgitb
import mariadb

#########################################################

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
       
DBFreezer=Maria("root","root","10.125.23.73",3306,"freezer")
DBFreezer.ajouterUser("ROMAIN","ROMAIN")
DBFreezer.ajouterUser("JIMMY","JIMMY")
DBFreezer.ajouterUser("DRSOSO","DRSOSO")
DBFreezer.ajouterUser("MARTIN","MARTIN")

#############################################################

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>""")

cgitb.enable()

input_data = cgi.FieldStorage()


print('<h1>Voici les machines présentes dans la base de donnée :</h1>')



# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="172.18.0.6",
        database="freezer"
    )
#    print("connexion reussite")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# Get Cursor
try:
    cur = conn.cursor()
 #   print("good")
except:
    print("not ok")

cur.execute("SELECT * FROM users;")
for line in cur:
    print(line)
    print("""<br>""")


print(""" <form action="index.cgi" method="POST">
   <button>Retour</button>
  </form>""")

print("""</body></html>""")



