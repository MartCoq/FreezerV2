#! /usr/bin/mariadb

# Initialisation de la base de donnée freezer

# Creation BDD si non existante
create database if not exists freezer;

# Creation table users si non existante
create table if not exists freezer.users (user_id int not null auto_increment, user_name text, primary key(user_id));

# Creation table security si non existante
create table if not exists freezer.security (user_id int not null, password text);

# Creation table music si non existante
create table if not exists freezer.music (music_id int not null auto_increment, artiste text, titre text, primary key(music_id));

# Creation table playslists si non existante
create table if not exists freezer.playlists (user_id int not null, music_id int not null);
