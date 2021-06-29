""" Kniffelblock anzeigen """

def get_column(a, i):
    '''Erwartet ein zweidimensionales Array a und eine Zahl i.
    Liefert die i-te Spalte aus a.'''
    return [a[j][i] for j in range(len(a))]

def getColumnDescription(i):
    """liefert die passende Beschreibung der Zeile zurück"""
    if i == 0: return "Einser (0)       "
    if i == 1: return "Zweier (1)       "
    if i == 2: return "Dreier (2)       "
    if i == 3: return "Vierer (3)       "
    if i == 4: return "Fünfer (4)       "
    if i == 5: return "Sechser (5)      "
    if i == 6: return "Dreierpasch (6)  "
    if i == 7: return "Viererpasch (7)  "
    if i == 8: return "Full House (8)   "
    if i == 9: return "Kleine Straße (9)"
    if i == 10: return "Große Straße (10)"
    if i == 11: return "Kniffel (11)     "
    if i == 12: return "Chance (12)      "

def kniffelblock_to_String(kniffelblock):
    """Wandelt den Kniffelblock in einen ausgebbaren String um"""
    columns = [get_column(kniffelblock, j) for j in range(13)]
    return [" | ".join(line) for line in columns]

def OutPutKniffelbock(kniffelblock):
    """Gibt die Punkte aller Spieler aus"""
    lines = kniffelblock_to_String(kniffelblock)
    for i in range(13):
        print("------------------")
        print(getColumnDescription(i) + " | " + lines[i] + " | ")
    print("------------------")
  
def OutputPlayerPoints(kniffelblock, player):
    """Gibt die Punkte eines Spielers aus"""
    row = kniffelblock[player]
    for i in range(13):
      print("------------------")
      print(getColumnDescription(i) + " | " + row[i] + " | ")
    print("------------------")
