

def slownik():
    n = int(input("podaj ilość numerów: "))
    baza = {}
    for i in range(0, n):
        a = input("Podaj imię i numer: ")
        baza[a[:-10]] = str(a[-8:])
    print(baza)
    while 1:
        try:
            question = input("Podaj imie: ")
            if question in baza:
                print(question+"="+baza.get(question))
            else:
                print("Not found")
        except:
            break


slownik()
