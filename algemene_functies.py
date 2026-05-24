#MIJN_FUNCTIE_1
def mijn_functie(argumenten):
    for getal in argumenten:
        return getal **2
print(mijn_functie([10]))
# Of:
def mijn_functie(argumenten):
    return argumenten**2
print(mijn_functie(2))
#MIJN_FUNCTIE_2
def mijn_functie_2(arg_1, arg_2):
    return[arg_1+arg_2, arg_1-arg_2, arg_1*arg_2, arg_1/arg_2]
print(mijn_functie_2(12, 3))