def wypisz_dane(imie, nazwisko, data):
    print('Imię: {imie}'.format(imie=imie))
    print('Nazwisko: {nazwisko}'.format(nazwisko=nazwisko))
    print('Rok urodzenia: {data}'.format(data=data))



if __name__ == "__main__":
    dane = input('Podaj imię, nazwisko oraz rok urodzenia:').split(' ')
    wypisz_dane(*dane)

