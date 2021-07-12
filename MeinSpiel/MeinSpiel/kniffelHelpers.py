from checkRules import checkRuleConform
from random import randrange

"""Listenfunktionen"""

def addAll(l):
    """addiert alle Elemente aus der Liste"""
    if l == []:
        return 0
    head, *tail = l
    return head + addAll(tail)

def addElement(l, e):
    """Addiert alle e in l"""
    counting = l.count(e)    
    return e * counting

"""HILFSFUNKTIONEN"""

def increaseRounds(round): return round + 1

def move_allowed(kniffelblock, player, fields, dices):
    """Prüft, ob die Würfel in der angegebenen Reihe eingetragen werden dürfen"""
    if fields in range(len(kniffelblock[player])):
      return kniffelblock[player][fields] == '-' and checkRuleConform(dices, fields) 
    else:
      return False

def FieldInRange(kniffelblock, player, fields):
    if fields in range(len(kniffelblock[player])):
        return kniffelblock[player][fields] == '-'
    else:
        return False



def isGameEnd(rounds, player, kniffelblock):
    """gibt True zurück wenn 13 Runden gespielt wurden"""
    if rounds > 13 and player+1 == len(kniffelblock):
        return True
    return False

def setField(kniffelblock, player, field, points):
    """erwartet ein 2-dimensionales Array, erstellt eine Kopie, verändert dort ein Feld und gibt die Kopie zurück"""
    new_a = [kniffelblock[i] for i in range(len(kniffelblock))]
    new_a[player][field] = points
    return new_a

def evaluatePoints(field, dices):
    """prueft um welches Feld(bzw. Kategorie) es sich handelt und ermittelt dann die passende Punktzahl"""
    if field <= 5:
        return str(addElement(dices, field+1))
    if field == 6 or field == 7 or field == 12:
        return str(addAll(dices))
    if field == 8:
        return  "25"
    if field == 9:
        return "30"
    if field == 10:
        return "40"
    if field == 11:
        return "50"

"""WÜRFELN"""

def throwDices(dices):
    """füllt die Liste mit random zahlen, sodass sie die länge 5 hat"""
    """liefert als Rückgabewert eine Liste der Zahlen"""
    numberDices = getNumberDices(dices)
    if numberDices == 0:
      return dices
    return dices + [randrange(1,7) for i in range(numberDices)]

def getNumberDices(dices):
    """gibt zurück, wie viele würfeln gefürfelt werden müssen"""
    if dices == []: 
      return 5
    else: 
      return 5 - len(dices)

def checkSortOut(dices, sortOut):
    """checkt ob alle Elemente aus sortOut auch in dices vorhanden sind und liefer True oder False"""
    if sortOut == []:
      return True
    head, *tail = sortOut
    if head in dices: 
      contains = True
      testDices = dices.copy()
      testDices.remove(head)
    else: 
      contains = False 
    return (contains) and checkSortOut(testDices, tail)
 
"""GEWINNERMITTLUNG"""

def evaluateTotalPoints(kniffelblock):
    """gibt eine Liste der Punkte aller Spieler zurück"""
    return [addAll(map(int, kniffelblock[i])) for i in range(len(kniffelblock))]

def evaluateHighestPoints(kniffelblock):
    """berechnet die Punkte aller Spieler und gibt die max. erreichte Punktzahl aus"""
    PointList = evaluateTotalPoints(kniffelblock)
    highestP = max(PointList)
    return highestP

def evaluateWinner(kniffelblock):
    """gibt alle Spieler aus die die max. erreichte Punktzahl erreicht haben"""
    highP = evaluateHighestPoints(kniffelblock)
    totalP = evaluateTotalPoints(kniffelblock)
    return [i+1 for i in range(len(totalP)) if totalP[i] == highP]
