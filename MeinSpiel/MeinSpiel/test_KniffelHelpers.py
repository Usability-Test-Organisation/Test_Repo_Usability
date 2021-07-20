from checkRules import CheckDreierpasch, CheckViererpasch, CheckElement, CheckKniffel, CheckFullHouse, CheckSmallStreet, CheckBigStreet
from kniffelHelpers import addAll, addElement, evaluateTotalPoints, evaluateWinner, checkSortOut, evaluateHighestPoints

def test_addAll():
    """Test, der die Funktion "Add All" prüft"""
    l = [1,2,3,4,5]
    assert(addAll(l) == 15)

def test_AddElement():
    l = [2,5,3,5,6]
    assert(addElement(l,5) == 10)
    assert(addElement(l,2) == 2 )

""" KONDITIONEN / REGELN PRUEFEN - Test"""

def test_CheckDreierpasch():
    l = [3,2,6,2,1]
    assert(CheckDreierpasch(l) == False)
    l = [2,4,2,2,4]
    assert(CheckDreierpasch(l) == True)
    l = [1,1,1,1,1]
    assert(CheckDreierpasch(l) == True)

def test_CheckViererpasch():
    l = [2,2,2,2,1]
    assert(CheckViererpasch(l) == True)
    l = [2,4,2,5,1]
    assert(CheckViererpasch(l) == False)

def test_CheckElement():
    l = [2,1,4,1,6]
    assert(CheckElement(l, 2) == True)
    assert(CheckElement(l, 3) == False)

def test_CheckFullHouse():
    l = [6,6,6,6,6]
    assert(CheckFullHouse(l) == True)
    l = [5,5,5,2,2]
    assert(CheckFullHouse(l) == True)
    l = [6,2,6,2,6]
    assert(CheckFullHouse(l) == True)
    l = [1,1,6,6,6]
    assert(CheckFullHouse(l) == True)
    l = [1,6,2,6,6]
    assert(CheckFullHouse(l) == False)

def test_CheckKniffel():
    l = [2,2,2,2,2]
    assert(CheckKniffel(l) == True)
    l = [2,5,2,6,3]
    assert(CheckKniffel(l) == False)

def test_CheckFullHouse():
    l = [2,3,2,3,3]
    assert(CheckFullHouse(l) == True)
    l = [2,3,5,1,5]
    assert(CheckFullHouse(l) == False)
    l = [2,2,2,2,2]
    assert(CheckFullHouse(l) == True)

def test_CheckSmallStreet():
    l = [2,3,4,5,6]
    assert(CheckSmallStreet(l) == True)
    l = [1,2,4,3,1]
    assert(CheckSmallStreet(l) == True)
    l = [2,5,3,3,4]
    assert(CheckSmallStreet(l) == True)
    l = [1,4,5,3,6]
    assert(CheckSmallStreet(l) == True)
    l = [2,4,1,2,4]
    assert(CheckSmallStreet(l) == False)

def test_CheckBigStreet():
    l = [1,3,2,5,4]
    assert(CheckBigStreet(l) == True)
    l = [1,2,5,3,1]
    assert(CheckBigStreet(l) == False)
    l = [1,3,4,3,1]
    assert(CheckBigStreet(l) == False)
    l = [2,6,4,3,5]
    assert(CheckBigStreet(l) == True)


""" weitere Hilfsfunktionen """

def test_evaluateTotalPoints():
    kniffelblock = [[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7]]
    assert(evaluateTotalPoints(kniffelblock) == [47,47,47,47])

    kniffelblock = [[1,4,6,1,1,6,3,5,3,5,4,7],[1,4,6,1,1,6,3,7,3,5,4,7],[1,4,6,2,1,1,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,1]]
    assert(evaluateTotalPoints(kniffelblock) == [46, 48, 42, 41])

def test_evaluateHighestPoints():
    kniffelblock = [[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7],[1,4,6,2,1,6,3,5,3,5,4,7]]
    assert(evaluateHighestPoints(kniffelblock) == 47)

def test_checkSortOut():
    dices = [2,4,5,6]
    sortOut = [2,4,5,4]
    assert(checkSortOut(dices, sortOut) == False)
    
def run_KniffelHelpers_tests():
    test_addAll()
    test_AddElement()
    test_evaluateHighestPoints()
    test_CheckDreierpasch()
    test_CheckElement()
    test_CheckFullHouse()
    test_CheckKniffel()
    test_CheckSmallStreet()
    test_CheckBigStreet()
    test_checkSortOut()
    test_CheckViererpasch()
    test_evaluateTotalPoints()
    test_CheckFullHouse()
