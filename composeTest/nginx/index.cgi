#!/usr/bin/python3

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<meta charset="utf-8">
 <body>
   <form action="afficher.cgi" method="POST">
    <fieldset>
     <legend> Voulez-vous afficher les machines avant de vous décider ? </legend>
    </fieldset>
    <button>Afficher les machines</button>
   </form>
   <form action="ajouter.cgi" method="POST">
    <fieldset>
     <legend> Quelle machine souhaitez-vous ajouter ? </legend>
     <label>Ip de la machine: <input type="text" name="ipAddress"></label><br/>
     <label>Nom de la machine: <input type="text" name="name"></label><br/>
     <label>Groupe de la machine: <input type="text" name="group"></label><br/>
    </fieldset>
    <button>Ajouter la machine</button>
   </form>

   <form action="supprimer.cgi" method="POST">
    <fieldset>
     <legend> Quelle machine souhaitez-vous supprimer ? </legend>
     <label>Ip de la machine: <input type="text" name="ipAddressSup"></label><br/>
    </fieldset>
    <button>Supprimer la machine</button>
   </form>

   <form action="modifier.cgi" method="POST">
    <fieldset>
     <legend> Quelle machine souhaitez-vous modifier ? </legend>
     <label>Ip de la machine: <input type="text" name="ipAddressM"></label><br/>
    </fieldset>
    <button>Modifier la machine</button>
   </form>







 </body>
</html>""")
