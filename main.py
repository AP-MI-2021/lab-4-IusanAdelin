def citireLista():
    l = []
    givenString = input("Dati lista cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def Suma(l):
    """
    Gaseste cel mai mare si cel mai mic numar din lista si afiseaza suma lor
    :param l: lista de numere intregi
    :return: Suma celui mai mare si celui mai mic numar din lista
    """
    suma=0
    max= -99999
    min= 99999
    for x in l:
        if x > max:
            max=x
        if x < min:
                min=x
    suma=min+max
    return suma

def test_Suma():
    assert Suma([10, -3, 25, -1, 3, 25, 18]) == 22
    assert Suma([]) == 0
    assert Suma([1,2,3,4,5]) == 6

def SumaCif(l, n):
    """
    Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de
la tastatură.
    :param l: lista de nr intregi
    :return:Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de
la tastatură.
    """

    rez = []
    for x in l:
        s=0
        copie = x
        while x!=0:
            s = s + x % 10
            x = x // 10
        if s >= n:
            rez.append(copie)
    return rez

def test_SumaCif():
    assert SumaCif([25, 11, 10, 24, 39],7) == [25, 39]
    assert SumaCif([],6) == []
    assert SumaCif([12, 10, 45],9) == [45]


def Concat(l):
    """
    Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.
    :param l:lista de numere intregi
    :return:Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.
    """
    rez= []
    for x in l:
        if x>0:
            rez=str(rez) + str(x)
    return rez

def main():
    test_Suma()
    test_SumaCif()
    l = []
    while True:
        print("Optiuni meniu: ")
        print("1. Citire lista.")
        print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
        print("3. Suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
        print("4. Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit.")
        print("5. Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite ")
        print("   cu radicalul acestora.")
        print("X. Iesire.")


        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(Concat(l))
        elif optiune == "3":
            print(Suma(l))
        elif optiune == "4":
            n=int(input("Dati un numar: "))
            print(SumaCif(l, n))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()