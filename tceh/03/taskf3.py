def odds_or_evens(l, switch=True):
    odds = []
    evens = []
    for i in l:
        if i % 2 == 1:
            odds.append(i)
        else:
            evens.append(i)
    if switch:
        return odds
    else:
        return evens

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(odds_or_evens(l, switch=False))
