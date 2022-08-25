#!/bin/bash

###########
# FREEZER #
###########

python ~/server1.py 
manu=$(cat ~/test505.txt)

echo "la voiture est lancée :" $manu " " $manuel 
# récupération des arguments
#for i in $(seq 0 $#)
#do
#	if [[ $1 = -u ]]
#	then
#		user=$2
#		shift 2
#	elif [[ $1 = -p ]]
#	then
#		password=$2
#		shift 2
#	elif [[ $1 = -play ]]
#	then
#		action="play"
#		shift 1
#	elif [[ $1 = -show ]]
#	then
#		action="show"
#		shift 1
#	elif [[ $1 = -artist ]]
#	then
#		artiste=$2
#		shift 2
#	elif [[ $1 = -song ]]
#	then
#		musique=$2
#		shift 2
#	fi
#done

host=10.125.24.52

# fonction pour afficher la liste des musiques
function show(){
usr=$1
pw=$2
ftp -i -nv $host  << EOF 
user $usr $pw
ls -R
EOF
}

# fonction pour jouer une musique
function play(){
checking=$1
vlc -I ncurses ~/Music/$checking
}

# fonction pour télécharger depuis youtube (si pas présent sur remote)
function download(){
art=$1
song=$2
artsong="$1_$2"
youtube-dl -x -o "~/Music/$artsong.%(ext)s" ytsearch1:"$art $song"
}

# fonction pour transférer la musique du local au remote
function upload(){
usr=$1
pw=$2
song=$3
song2=$4
ftp -i -n $host << EOF
user $usr $pw
put $song $song2  
EOF
}

# fonction pour télécharger la musique depuis le remote
function load(){
usr=$1
pw=$2
song=$3
song2=$4
ftp -i -nV $host << EOF
user $usr $pw
get $song2 $song  
EOF
}

if [[ $action = "show" ]]
then
	songs=$(show $user $password | grep _ | rev | cut -d " " -f1 | rev )
	echo $songs
elif [[ $action = "play" ]]
then
	checking=$(show $user $password | grep $artiste_$musique | rev | cut -d " " -f1 | rev)
	if [[ -z "$checking" ]] 
	then	
		echo "Chanson non disponible. Téléchargement en cours. Merci de patienter."
		download $artiste $musique
		chanson=$(ls ~/Music | grep $artiste_$musique | rev | cut -d " " -f1 | rev )
		upload $user $password ~/Music/$chanson $chanson
		play $chanson
	else
		locale=$(ls ~/Music | grep $artiste_$musique | rev | cut -d " " -f1 | rev )
		if [[ -z "$locale" ]]
		then
			chanson=$(show $user $password | grep $artiste_$musique | rev | cut -d " " -f1 | rev)
			load $user $password ~/Music/$chanson $chanson
			play $chanson
		else
			play $locale
		fi
	fi
else
	echo "Commande inconnue"
fi
