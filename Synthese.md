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

### Pour la Raspberry Pi

## Conception de la table

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