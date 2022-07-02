
def trans_MONATSZAHL(x):
    if x=='alkoholunfälle':
        x=0
    elif x=='fluchtunfälle':
        x=1
    elif x=='verkehrsunfälle':
        x=2
    return x

def trans_AUSPRAEGUNG(x):
    if x=='insgesamt':
        x=0
    elif x=='verletzte und getötete':
        x=1
    elif x=='mit personenschäden':
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