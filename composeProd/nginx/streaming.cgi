#!/usr/bin/python3
import cgi, cgitb
import mariadb


print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>""")

cgitb.enable()

input_data = cgi.FieldStorage()

music=str(input_data["music"].value)
user_name=str(input_data["username"].value)

print('<h1>Voici les musiques présentes dans votre dossier ftp :</h1>')

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

cur.execute(f"INSERT INTO music (artiste, titre) values ('adele','{music}');")
cur.commit()

cur.execute(f"SELECT * FROM music WHERE user_name='{username}';")
for line in cur:
    print(line)
    print("""<br>""")


print(""" <form action="index.cgi" method="POST">
   <button>Retour</button>
  </form>""")

print("""</body></html>""")



