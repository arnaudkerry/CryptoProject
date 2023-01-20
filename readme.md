# README ProjetCrypto #2  
# Kerry LAVOILE

## Lancement de génération de clé
    - python3 key_generator.py N size

## Vérification de doublons
    - python3 check_duplicate.py keys

## Affichage des chaînes de caractère communes
    - python common_substring.py keys

## Temps d'exécution sur ancienne VM (rsa256)
 - 2000 clés : 10 secondes
 - 4000 clés 25 secondes
 - 8000 clés : 46 secondes
 Extrapolation : Pour 1 millions de clés -> 6000 secondes

 ## Temps d'exécution sur ancienne VM (rsa512)
 - 2000 clés : 10 secondes
 - 4000 clés 27 secondes
 - 8000 clés : 39 secondes
 Extrapolation : Pour 1 millions de clés -> 6000 secondes

 ## Temps d'exécution sur ancienne VM (rsa1024)
 - 2000 clés : 40 secondes
 - 4000 clés 80 secondes
 - 8000 clés : 170 secondes
 Extrapolation : Pour 1 millions de
 clés -> 22 100 secondes

  ## Temps d'exécution sur ancienne VM (rsa2048)
 - 2000 clés : 238 secondes
 - 4000 clés 490 secondes
 - 8000 clés : 964 secondes
 Extrapolation : Pour 1 millions de
 clés -> 130 000 secondes

 ## Présence de doublon
 - Jamais eu de doublons durant les tests (taille max 400000)

## Plus longue sous chaîne commune
 - Environ 27 caractères
 