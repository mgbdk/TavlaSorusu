def compareDicts(tempCheckers, checkers):
    point = 0
    for key in range(1, 25):
        if checkers[key] != tempCheckers[key]:
            if checkers[key] > 1 and tempCheckers[key] == 1:
                if (key > 4 and key < 9) or (key > 16 and key < 21):
                    point -= 2
                else:
                    point -= 1
            if checkers[key] < 2 and tempCheckers[key] > 1:
                if (key > 4 and key < 9) or (key > 16 and key < 21):
                    point += 2
                else:
                    point += 1
            if checkers[key] == 1 and tempCheckers[key] == 0:
                point += 1
            if checkers[key] == 0 and tempCheckers[key] == 1:
                point -= 1
    return point

def setCheckers(checkers):
    for key in range(1, 25):
        if key not in checkers:
            checkers[key] = 0

def find_moves(checkers, dice1, dice2):
    """calculates possible moves and scores in backgammon
    >>> find_moves(checkers, 6, 1)
    [((1, 7), (6, 7), 3), ((1, 7), (12, 13), 1), ((6, 12), (1, 2), 1), ((6, 12), (12, 13), 2), ((6, 12), (13, 14), 2)]
    >>> find_moves(checkers, 3, 2)
    [((1, 4), (4, 6), 2), ((10, 13), (10, 12), 2), ((12, 15), (13, 15), 3)]
    >>> find_moves(checkers, 4, 2)
    [((6, 10), (10, 12), 2), ((6, 10), (12, 14), 1), ((6, 10), (13, 15), 1), ((10, 14), (12, 14), 1)]
    """
    setCheckers(checkers) #Bos olan ücgenleri tespit etmek icin yazılan fonksiyon
    tempCheckers1 = checkers.copy()
    list = []
    for i in range(1, 25):
        if tempCheckers1[i] > 0:
            tempCheckers1[i] -= 1
            if (i + dice1) < 25:
                tempCheckers1[i + dice1] += 1
                tempCheckers2 = tempCheckers1.copy()
                for j in range(1, 25):
                    if tempCheckers2[j] > 0:
                        tempCheckers2[j] -= 1
                        if (j + dice2) < 25:
                            tempCheckers2[j + dice2] += 1
                            point = compareDicts(tempCheckers2, checkers) #ilk durumdaki pulların poziyonları ile son durumu kıyaslar
                            if point > 0:
                                new_move = ((i, i+dice1), (j, j+dice2), point) #puan 0'dan büyükse pozisyonları ve puanı list'e ekler
                                list.append(new_move)
                            tempCheckers2 = tempCheckers1.copy()
                tempCheckers1 = checkers.copy()
    print(list)


checkers = {1:3, 6:1, 10:2, 12:1, 13:1}
dice1 = 6
dice2 = 1
find_moves(checkers, dice1, dice2)