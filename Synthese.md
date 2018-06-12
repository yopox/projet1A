---
title: Réalisation d'une table d'arcade - Synthèse
author: Castello Cyprien, Vignier Louis
lang: FR
institute: CentraleSupélec
documentclass: report
toc: false
header-includes:
    - \usepackage{fancyhdr}
    - \pagestyle{fancy}
    - \usepackage{booktabs}
    - \usepackage{graphicx}
    - \usepackage{sistyle}
    - \usepackage[utf8]{inputenc} 
    - \fancyhead[L]{\leftmark}
    - \fancyhead[R]{Projet de synthèse}
---

# Introduction

## Présentation

### Concept

Notre projet consiste en la réalisation d’une table de jeu de type arcade. Cette table permet à plusieurs joueurs (2à4) de s’affronter sur un jeu dans lequel chacun des joueurs contrôle un serpent (constitué d’une trainée de points) et doit obliger ses adversaires à entrer en collision avec un mur ou un serpent.

Ce jeu est connu sous le nom de « Achtung die Kurve ! » sorti initialement en 1995. Il a fait l’objet de nombreuses reprises depuis sa sortie et nous proposons de créer une nouvelle façon originale de jouer à ce jeu. L’utilisation d’une table à part entière offre plus de confort aux joueurs car les contrôles sont de vrais boutons au lieu de touches de clavier et les joueurs auront plus d’espace que s’ils devaient s’entasser à plusieurs autour d’un clavier d’ordinateur. De plus, la matrice de leds utilisée pour l’affichage permet d’obtenir un rendu graphique plus attrayant que celui d’un écran d’ordinateur.

### Règles du jeu

Au début d’une partie chaque joueur apparaît de manière aléatoire en un point de l’écran. A l’aide de deux boutons qui permettent des déplacements vers la gauche ou vers la droite chaque joueur va pouvoir déplacer ce point. Celui-ci va alors laisser une traînée sur son passage qu’il faudra éviter. Ainsi, à mesure que la partie avance, la difficulté s’accroit du fait que le nombre de traînées crées par les joueurs augmente. Cependant, la traînée n’est pas entièrement continue, des trous sont générés pour pouvoir éviter de se retrouver bloqué trop rapidement. Un joueur perd s’il entre en collision avec une traînée ou l’un des murs. La partie s’arrête lorsqu’il ne reste plus qu’un joueur en jeu qui est déclaré vainqueur.

## Méthodologie

### Outils de travail

#### Matériel

#### Logiciels

## Respect du cahier des charges

## Évolutions futures

Le principal problème de notre système actuel concerne son alimentation. En effet, la table nécessite deux brancher deux blocs d’alimentation pour fonctionner. Cela est dû au fait que nous alimentons directement les deux composants qui ont besoin d’électricité. Pour pallier à ce problème, il faudrait concevoir un bloc d’alimentation unique capable d’alimenter chacun des composants selon les contraintes qui lui sont propres.
Cependant, une telle solution ne serait pas forcément optimale car l’un des objectifs de notre projet était de pouvoir obtenir une table portative. Pour ce faire il faudrait envisager l’utilisation d’une batterie.

<!-- Améliorations sur le jeu -->

<!-- Améliorations sur la table -->

<!-- Augmentation du nombre de jeux -->