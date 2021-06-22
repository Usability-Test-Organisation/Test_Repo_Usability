from checkRules import checkRuleConform
from KniffelblockAnzeige import OutPutKniffelbock, OutputPlayerPoints
from kniffelHelpers import throwDices, checkSortOut, isGameEnd, evaluateWinner, increaseRounds, move_allowed, setField, evaluatePoints, FieldInRange, evaluateHighestPoints
from test_KniffelHelpers import run_KniffelHelpers_tests



def game_round(kniffelblock, player):
    ''' Führt eine einzelne Spielrunde durch.
        Erwartet ein Spielfeld und den Spieler, der am Zug ist.
        Liefert das neue Spielfeld zurück und den Spieler, der als nächstes am Zug ist.'''
   
    # - Spielfeld anzeigen
    print("---------- Punkte des Spielers " + str(player+1) + "----------")
    OutputPlayerPoints(kniffelblock, player)
    
    dices = makeMove([], 1)  
    OutputPlayerPoints(kniffelblock, player)

    field = int(input("Wähle bitte die Zeile, welche du füllen möchtest, indem du die zugehörige Zahl angibst:  "))
    kniffelblock = tryFillField(kniffelblock, dices, field, player)
    OutputPlayerPoints(kniffelblock, player)
    return kniffelblock


def tryFillField(kniffelblock, dices, field, player):
    if move_allowed(kniffelblock, player, field, dices) == True:
        points = evaluatePoints(field, dices)
        return setField(kniffelblock, player, field, points)
    else:
        if FieldInRange(kniffelblock, player, field) == True:
            if tryBlockField() == True:
              return setField(kniffelblock, player, field, "0")

        else: 
            OutputPlayerPoints(kniffelblock, player)
            print("Dies ware keine korrekte Eingabe, entweder hast du das Feld bereits befüllt, oder du hast eine Zahl außerhalb des Bereichs 0-12 angegben!")
            print("Du hast folgendes gewürfelt: " + str(dices))
            field = int(input("Wähle bitte die Zeile, welche du füllen möchtest, indem du die zugehörige Zahl angibst: "))
            return tryFillField(kniffelblock, dices, field, player)

def tryBlockField():
    blockField = int(input("Du kannst dieses Feld nicht füllen, möchest du es stattdessen streichen? Wenn JA, gib eine Zahl größer >>1<< ein:  "))
    if blockField >= 1:
        return True
    else: return False

def makeMove(dices, move):
    """achtet darauf, dass höchstens 3 mal gewürfelt werden kann, gibt die gewürfelten Zahlen zurück"""
    if move < 3:
        newDices = throwDices(dices)
        print("Du hast folgendes gewürfelt: " + str(newDices))
        ready = input("Möchtest du erneut würfeln? Wenn ja, gib >>1<< ein, wenn nein >>0<<:  ")
        if ready != "0" and ready != "1": ready = "1"
        if ready == "1":
            srtList = list(input("Bitte gib alle Würfel an, die du NICHT noch einmal wuerfeln möchtest!:  "))
            sortOut = list(map(int, srtList))
            return trySortout(newDices, sortOut, move)
        elif ready == "0":
            return newDices
    if move == 3:
        newDices = throwDices(dices)
        print("Du hast folgendes gewürfelt: " + str(newDices))
        print("Das war dein letzter Wurf!")
    return newDices

def trySortout(dices, sortOut, move):
    """prüft die Validität der angegebenen Würfel und gibt True oder False zurück"""
    if checkSortOut(dices, sortOut) == True:
        return makeMove(sortOut, move + 1)
    else:
        print("Die angegebenen Würfel befinden sich nicht in deinem Becher, bitte wähle erneut aus folgender Würfeln: ")
        print(dices)
        srtList = list(input("Bitte gib alle Würfel an, die du NICHT noch einmal wuerfeln möchtedt!"))
        sortOut = list(map(int, srtList))
        return trySortout(dices, sortOut, move)


def game_loop(kniffelblock, player, round):
    """ Führt so lange Spielrunden aus, bis das Spiel beendet ist. """

    if isGameEnd(round, player, kniffelblock):
        OutPutKniffelbock(kniffelblock)
        highestPoints = str(evaluateHighestPoints(kniffelblock))
        winner = str(evaluateWinner(kniffelblock))
        print("Der/Die Gewinner ist/sind die Spieler: " + winner +  " mit " + highestPoints + " Punkten!")
        return kniffelblock
    
    # - Spielereingabe einlesen
    kniffelblock = game_round(kniffelblock, player)
    OutPutKniffelbock(kniffelblock)
    
    """ wenn der letzte Spieler seinen Zug gemacht hat, beginnt die nächste Runde"""
    if player < len(kniffelblock) -1:
        return game_loop(kniffelblock, player + 1, round)
    else: 
        return game_loop(kniffelblock, 0, increaseRounds(round))

def run_Kniffel():
  """startet das Spiel und erstellt ein Spielfeld gemessen an der abgegebenen Spielerzahl"""
  print("Bitte geben sie die Anzahl an Spielern an!")
  numbPlayer = int(input())

  if numbPlayer > 0:
      round = 1
      kniffelblock = [["-" for x in range(13)] for y in range(numbPlayer)]
      OutPutKniffelbock(kniffelblock)
      kniffelblock = game_loop(kniffelblock, 0, round)
  else:
      print("Ungültige Eingabe! Die EIngabe der Spieler sollte größer als 0 sein!")
      runKniffel()

  OutPutKniffelbock(kniffelblock)

run_KniffelHelpers_tests()

if __name__ == '__main__':
    run_Kniffel()




