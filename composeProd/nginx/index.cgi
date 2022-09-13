#!/usr/bin/python3

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>
   <form action="afficher.cgi" method="POST">
    <fieldset>
     <legend> Souhaitez vous afficher la liste des users de la DB ? </legend>
    </fieldset>
    <button>Afficher les machines</button>
   </form>
   <form action="streaming.cgi" method="POST">
    <fieldset>
     <legend> Quelle musique souhaitez-vous jouer ? </legend>
     <label>Chanson à jouer : <input type="text" name="music"></label><br/>
    </fieldset>
    <fieldset>
     <legend> Quelle est votre nom d'utilisateur ? </legend>
     <label>Nom d'utilisateur : <input type="text" name="username"></label><br/>
    </fieldset>   
    <button>Lire la chanson</button>
   </form>

 </body>
</html>""")
