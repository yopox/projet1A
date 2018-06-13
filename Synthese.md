---
title: Réalisation d'une table d'arcade - Synthèse
author: Castello Cyprien, Vignier Louis
lang: FR
institute: CentraleSupélec
documentclass: report
toc: false
header-includes:
    - \input{common.tex}
---

# Introduction

## Présentation

### Concept

Notre projet consiste en la réalisation d’une table de jeu de type arcade. Cette table permet à deux joueurs de s’affronter sur un jeu dans lequel chacun des joueurs contrôle un serpent (constitué d’une trainée de points) et doit obliger son adversaire à entrer en collision avec un serpent.

Ce jeu est connu sous le nom de « Achtung die Kurve ! » sorti initialement en 1995. Il a fait l’objet de nombreuses reprises depuis sa sortie et nous proposons de créer une nouvelle façon originale de jouer à ce jeu. L’utilisation d’une table à part entière offre plus de confort aux joueurs car les contrôles sont de vrais boutons au lieu de touches de clavier et les joueurs auront plus d’espace que s’ils devaient s’entasser à plusieurs autour d’un clavier d’ordinateur. De plus, la matrice de leds utilisée pour l’affichage permet d’obtenir un rendu graphique plus attrayant que celui d’un écran d’ordinateur.

### Règles du jeu

Au début d’une partie chaque joueur apparaît de manière aléatoire en un point de l’écran. A l’aide de deux boutons qui permettent des déplacements vers la gauche ou vers la droite chaque joueur va pouvoir déplacer ce point.  Un joueur perd s’il entre en collision avec une traînée ou l’un des murs. La partie s’arrête lorsqu’il ne reste plus qu’un joueur en jeu qui est déclaré vainqueur.

#### Serpents

Chaque joueur va laisser une traînée sur son passage qu’il faudra éviter.
Ainsi, à mesure que la partie avance, la difficulté s’accroit du fait que le nombre de traînées crées par les joueurs augmente.

Cependant, la traînée n’est pas entièrement continue, des trous sont générés pour pouvoir éviter de se retrouver bloqué trop rapidement. Un joueur peut être dans l'un des 3 états suivants :

- `BLOC` $\rightarrow$ Le joueur a laissé un bloc derrière lui à la frame précédente. Il en laisse un nouveau avec une probabilité $p_{BLOC}$.
- `NONE` $\rightarrow$ Le joueur n'a pas laissé de bloc derrière lui à la frame précédente. Il n'en laisse toujours pas à cette frame avec une probabilité $p_{NONE}$.
- `TURN` $\rightarrow$ Le joueur vient de tourner et laisse systématiquement un bloc derrière lui pour que le joueur sache où il se trouve. Il repasse ensuite dans l'état `BLOC`.

On a le graphe d'états suivants :

\begin{center}
\begin{tikzpicture}[->, shorten >=1pt, node distance=3.5cm, on grid, >=stealth, initial text=, every state/.style={draw=blue!50, very thick, fill=blue!20}]

  \node[state]   (e0)               {$BLOC$};
  \node[state]   (e1) [right=of e0] {$NONE$};
  \node[state]   (e2) [below=of e0] {$TURN$};

  \path (e0) edge [loop above] node {$p_{BLOC}$} (e0)
             edge [bend left] node [above] {$1 - p_{BLOC}$} (e1)
        (e1) edge [bend left] node [below] {$1 - p_{NONE}$} (e0)
        (e1) edge [loop right] node {$p_{NONE}$} (e1)
        (e2) edge [bend left] node [left] {1} (e0);

\end{tikzpicture}
\end{center}

Cette méthode permet de générer des trous de manière plus efficace qu'en donnant simplement une probabilité à chaque bloc de ne pas apparaître. En effet, on ajuste $p_{BLOC}$ pour qu'un trou n'apparaisse pas trop souvent, puis on ajuste $p_{NONE}$ pour que lorsqu'un trou commence, il fasse souvent deux cases. Le résultat est alors plus naturel.

On a choisi $p_{BLOC} = 0.8$ et $p_{NONE} = 0.35$

## Méthodologie

### Outils de travail

#### Matériel

#### Logiciels

# Respect du cahier des charges

<!-- Ce qui a été fait par rapport au document cahier des charges initial -->

<!-- Changement de Raspberry -->

# Conception

## Branchements

### Pour la matrice de LED

#### Alimentation de la matrice

Les branchements à effectuer sur la matrice de LED concernent soit son alimentation, soit l'affichage. Adafruit, le constructeur de la matrice fournit une documentation à ce sujet sur son site disponible à l'adresse suivante : 
[https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/overview](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/overview)

L'ensemble des pixels allumés en blanc de la matrice peut consommer
jusqu'à 4A. Pour une utilisation plus classique, la matrice consomme en
moyenne 2A. On peut alimenter la matrice avec des courants plus grand (par
exemple 10A), par contre il est très important de bien l'alimenter sous 5V. Nous avons donc opté pour alimentation 5V/4000mA.

Au dos de la table, l'alimentation se fera au travers d'un connecteur de type
Molex.

![Alimentation au dos de la matrice\label{alim}](assets/Alim.jpg)

On dispose du cable d'alimentation suivant :

![Cable fournit pour alimenter la matrice\label{cable}](assets/Cable.jpg)

Ce câble dispose de deux connecteurs de type Molex mais nous n'utiliserons qu'un seul des deux pour alimenter la matrice.

Pour connecter l'autre extrémité du câble avec notre alimentation, nous utiliserons un adaptateur comme sur la photo suivante :

![Adapteur cable/alimenation 5V\label{adapt}](assets/Solution_adafruit.jpg)

#### Gestion de l'affichage

Pour l'affichage, il faut connecter les pins de la raspberry Pi au connecteur de pins de la matrice de LED.

Au dos de la matrice, il y a deux connecteurs de pin (INPUT à gauche,
OUTPUT à droite). Nous n'utiliserons pas le connecteur OUTPUT qui sert
dans les cas où l'on veut brancher plusieurs matrices de leds en parallèle.

Un connecteur possède 16 pins qui devront être relié à la raspberry Pi. Sa disposition est la suivante :

![Disposition des pins\label{pins}](assets/Disposition_pins.png)

Librairie qui indique les connexions entre les pins de la matrice et ceux de la raspberry


### Pour la Raspberry Pi

## Conception de la table

Pour réaliser notre table, nous sommes partis d'une cagette dont les dimensions permettaient de pouvoir y ajouter la matrice de LED et des boutons pour les deux joueurs. Nous avons ensuite percé cette table afin de pouvoir y intégrer les boutons poussoirs et faire passer les câbles nécessaires à l'alimentation et à l'affichage de la matrice de LED. Nous avons du souder les deux broches des boutons poussoirs à des fils pour pouvoir ensuite les connecter à la raspberry Pi. Une des broches du bouton poussoir est relié à un pin GND de la raspberry et l'autre à un pin normal.

Pour rendre la table portative, nous y avons intégré un compartiment pour pouvoir y poser la raspberry Pi. Enfin, nous avons travaillé son esthétique en bouchant certains trous et en la peignant.

## Conception du jeu

### Librairies utilisées

### "Code"

## Évolutions futures

Le principal problème de notre système actuel concerne son alimentation. En effet, la table nécessite deux brancher deux blocs d’alimentation pour fonctionner. Cela est dû au fait que nous alimentons directement les deux composants qui ont besoin d’électricité. Pour pallier à ce problème, il faudrait concevoir un bloc d’alimentation unique capable d’alimenter chacun des composants selon les contraintes qui lui sont propres.
Cependant, une telle solution ne serait pas forcément optimale car l’un des objectifs de notre projet était de pouvoir obtenir une table portative. Pour ce faire il faudrait envisager l’utilisation d’une batterie.

<!-- Améliorations sur le jeu -->

<!-- Améliorations sur la table -->

<!-- Augmentation du nombre de jeux -->

# Annexes

## Inspirations

## Autres implémentations du jeu