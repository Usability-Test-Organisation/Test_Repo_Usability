
def checkRuleConform(dices, col):
    """Aufruf der Pruefungsmethoden"""
    if dices == [] : return True
    if col <=5 : return CheckElement(dices, col+1)
    if col == 6: return CheckDreierpasch(dices)
    if col == 7: return CheckViererpasch(dices)
    if col == 8: return CheckFullHouse(dices)
    if col == 9: return CheckSmallStreet(dices)
    if col == 10: return CheckBigStreet(dices)
    if col == 11: return CheckKniffel(dices)
    if col == 12: return True
    
""" KONDITIONEN / REGELN PRUEFEN """

def CheckDreierpasch(l):
    """prueft, ob 3 gleiche Elemente in l vorhanden sind"""
    return [x for x in range(1, 7) if l.count(x) > 2] != []

def CheckViererpasch(l):
    """prueft, ob 4 gleiche Elemente in l vorhanden sind"""
    return [x for x in range(1, 7) if l.count(x) > 3] != []

def CheckElement(l, e):
    """prueft, ob das Element e ein l vorhanden ist"""
    if e in l:
        return True
    return False

def CheckKniffel(l):
    """prueft, ob alle Elemente in der Liste (Länge von 5) gleich sind"""
    return l.count(l[0]) == 5

def CheckFullHouse(l):
    """prueft, ob 1. 3 und 2. 2 mal die selbe Zahl vorhanden ist oder alle Zahlen gleich sein"""
    return ([x for x in range(1, 7) if l.count(x) == 3] != [] and [x for x in range(1, 7) if l.count(x) == 2] != []) or CheckKniffel(l)

def CheckSmallStreet(l):
    """prueft, ob eine Zahlenreihe einer laenge von mind. 4 in l enthalten ist"""
    """Zunächte Liste sortieren und doppelte Werte entfernen, indem l in ein Set umgewandelt wird""" 
    sortedList = sorted(set(l))
    """Fall 1: Liste hat die Länge 4 -> Komb prüfen"""
    if len(sortedList) == 4:
        return sortedList == [1,2,3,4] or sortedList == [2,3,4,5] or sortedList == [3,4,5,6]
    """Fall 2: Liste hat die Länge 5 -> Komb prüfen"""
    if len(sortedList) == 5:
        return sortedList[0:-1] == [1,2,3,4] or sortedList[0:-1] == [2,3,4,5] or sortedList[1:] == [3,4,5,6] or sortedList[1:] == [2,3,4,5]
    return False

def CheckBigStreet(l):
    """prueft, ob eine Zahlenreihe einer laenge von 5 in l entahlten ist"""
    sortedList = sorted(l)
    return sortedList == [1,2,3,4,5] or sortedList == [2,3,4,5,6]
