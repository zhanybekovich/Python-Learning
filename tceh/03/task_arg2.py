def case(word, case=True):
    if case:
        return word.upper()
    else:
        return word.lower()

print(case('GloRy', case=True))