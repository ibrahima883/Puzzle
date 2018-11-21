# Puzzle


Pour tester la solution, tapez la ligne suivante:
    python Test_Projet.py

 
Sous Python 3, il faut d'abord rajouter au debut dans les 2 fichiers ".py" le code suivant:
    try:
        # Python 2
        xrange
    except NameError:
        # Python 3, xrange is now named range
        xrange = range

