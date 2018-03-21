---
title: Cahier des charges - Projet de synthèse
author: Castello Cyprien, Vignier Louis
lang: FR
institute: CentraleSupélec
documentclass: article
toc: false
header-includes:
    - \usepackage{fancyhdr}
    - \pagestyle{fancy}
    - \usepackage{booktabs}
    - \usepackage{graphicx}
    - \usepackage{sistyle}
    - \usepackage[utf8]{inputenc} 
    - \fancyhead[L]{}
    - \fancyhead[R]{Projet de synthèse}
---

## Objectifs

Nous souhaitons dans ce projet réaliser un jeu vidéo pour deux joueurs sous une forme inhabituelle et esthétique : en utilisant une matrice de LED.

Il s'agit donc de réaliser une table de jeu comprenant les éléments suivants :

- Des contrôles (boutons poussoirs par exemple) pour chacun des deux joueurs
- Une matrice de LED 32x32 au centre
- Une Raspberry Pi qui fait tourner le jeu et permet de gérer la matrice et les boutons

## Méthodologie

Notre projet se découpe en trois parties :

1. Coder le jeu
2. Connexion et alimentation de la matrice de LED à la Raspberry
3. Intégrer des contrôles à la table de jeu

On dispose d'une Raspberry Pi modèle B comportant 26 pins I/O. Nous avons choisi d'acheter une matrice de LED compatible, il s'agit du composant `COM-12584`.

Le jeu sera codé en Python en tenant compte de la résolution imposée par la matrice de LED. On pourra ensuite lancer le programme Python automatiquement au démarrage de la Raspberry.

Du point de vue de l'organisation, nous pourrons travailler en parallèle sur différentes parties car le développement du jeu peut se faire sur l'ordinateur dans un premier temps.

Idéalement nous aimerions travailler sur la forme de la table de jeu pour qu'elle soit esthétique et portative. Cependant nous travaillerons ce point à la fin quand le projet sera fonctionnel.