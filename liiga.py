
def tulokset():
    sanakirja = {}
    lista = []

    with open("tulokset.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n","")
            rivi = rivi.replace("-","")
            rivi = rivi.replace(":","")
            lista.append(rivi)
    
    for i in lista:
        apuri = []
        a = i.split(" ")
        apuri.append(a)
        if int(a[3]) > int(a[5]):
            if a[0] in sanakirja:
                uusiValue = sanakirja[a[0]] + 3
                sanakirja[a[0]] = uusiValue
            else:
                sanakirja[a[0]] = 3
        if int(a[3]) < int(a[5]):
            if a[2] in sanakirja:
                uusiValue = sanakirja[a[2]] + 3
                sanakirja[a[2]] = uusiValue
            else:
                sanakirja[a[2]] = 3
        if int(a[3]) == int(a[5]):
            if a[0] in sanakirja:
                uusiValue = sanakirja[a[0]] + 1
                sanakirja[a[0]] = uusiValue
            else:
                sanakirja[a[0]] = 1
            if a[2] in sanakirja:
                uusiValue = sanakirja[a[2]] + 1
                sanakirja[a[2]] = uusiValue
            else:
                sanakirja[a[2]] = 1

    return sanakirja

print(tulokset())
