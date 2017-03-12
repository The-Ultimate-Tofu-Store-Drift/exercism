
"""Falls man eine GESAMTE Datei import, muss man um auf eine Funktion zu greifen zu können,
folgenden Syntax anwenden:"""
import hamming
print(hamming.distance("ABC", "ABE"))


"""Falls man aus einer Datei nur EINZELNE Funktionen import, reicht der einfache Funktionsaufruf."""
from hamming import distance
print(distance("GAFER", "GABEN"))
