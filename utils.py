
def trans_MONATSZAHL(x):
    if x=='Alkoholunfälle':
        x=0
    elif x=='Fluchtunfälle':
        x=1
    elif x=='Verkehrsunfälle':
        x=2
    return x

def trans_AUSPRAEGUNG(x):
    if x=='insgesamt':
        x=0
    elif x=='Verletzte und Getötete':
        x=1
    elif x=='mit Personenschäden':
        x=2
    return x

def trans_JAHR(x):
    return int(x)

def trans_MONAT(x):
    return int(x)


def transform(X):
    X['MONATSZAHL']=X['MONATSZAHL'].apply(lambda x: trans_MONATSZAHL(x))
    X['AUSPRAEGUNG']=X['AUSPRAEGUNG'].apply(lambda x: trans_AUSPRAEGUNG(x))
    X['JAHR']=X['JAHR'].apply(lambda x: trans_JAHR(x))
    X['MONAT']=X['MONAT'].apply(lambda x: trans_MONAT(x))
    return X