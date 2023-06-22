from PIL import Image
import wagi
import os
width = 28 #szerokość oka
height = 28 #wysokość oka
piksele = width*height-1
nauka_lok = "Nauka\\"#ścieżka zapisu danych nauczonych
def analiza(path):
    try:
        im = Image.open(path)  # otworzenie zdjęcia
        w = 0  # ustawienie parametru szerokości
        h = 0  # ustawienie parametru wysokośći
        lista = []  # lista pikseli ze zdjęcia
        for i in range(width * height - 1):  # pętla wprowadzająca dane do listy
            coordinate = w, h  # ustawienie współrzędnych do pobierania wartości pikseli
            wartosc = im.getpixel(coordinate)  # pobranie wartości piksela o współrzędnych coordinate
            if wartosc[0] >= 128:
                lista.append(1)  # jeśli piksel ma wartość 255(biały) dodaje do listy 1
            else:
                lista.append(0)  # jeśli piksel jest czarny dodaje do listy wartoość 0

            if w < width - 1:
                w = w + 1  # zmiana szerokości
            else:
                w = 0
                h = h + 1  # zmaian wartości wysokości
        return lista

    except:
        print("Nieoczekiwany błąd analizy zdjęcia!")
        change()

def sigmoid(x):
    return 1 / (1 + 2.71828182846 ** (-x))

def warstwa1(lista, wagi0, wagi1, wagi2, wagi3, wagi4, wagi5, wagi6, wagi7, wagi8, wagi9):
    try:
        wynik_k = []

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i]*wagi0[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi1[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi2[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi3[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi4[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi5[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi6[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi7[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi8[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        warstwa_1 = []
        wynik = 0
        for i in range(piksele):
            warstwa_1.append(lista[i] * wagi9[i])
        for i in range(piksele):
            wynik = wynik + warstwa_1[i]
        wynik_k.append(wynik)

        return(wynik_k)
    except:
        print("Nieoczekiwany błąd w warstwie 2!")

def warstwa3(lista, full):
    try:
        wynik_k = []
        for i in range(len(lista)):
            try:
                wynik = (lista[i]/full[i])*100
                wynik_k.append(wynik)
            except:
                wynik_k.append(0)
        return(wynik_k)
    except:
        print("Nieoczekiwany błąd w warstwie 3!")

def warstwa2(lista, warstwa1, wagi0, wagi1, wagi2, wagi3, wagi4, wagi5, wagi6, wagi7, wagi8, wagi9):
    try:
        wynik_k = []

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi0[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi1[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi2[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi3[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi4[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi5[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi6[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi7[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi8[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        warstwa_2 = []
        wynik = 0
        for i in range(piksele):
            warstwa_2.append(lista[i] * wagi9[i])
        for i in range(piksele):
            wynik = wynik + warstwa_2[i]
        wynik_k.append(wynik)

        for i in range(len(wynik_k)):
            wynik_k[i] = wynik_k[i]+warstwa1[i]

        return (wynik_k)
    except:
        print("Nieoczekiwany błąd w warstwie 2!")

def test():
    path = input("Wpisz ścieżkę do obrazu, który ma zostać sprawdzony: ")
    exist = os.path.isfile(path)
    if exist == True:
        print("Analizowanie zdjęcia...")
        lista = analiza(path)
        print("Przetwarzanie przez warstwe 1... ")
        warstwa_1 = warstwa1(lista, wagi0, wagi1, wagi2, wagi3, wagi4, wagi5, wagi6, wagi7, wagi8, wagi9)
        full_p = warstwa1(wagi.full, wagi0, wagi1, wagi2, wagi3, wagi4, wagi5, wagi6, wagi7, wagi8, wagi9)
        print("Przetwarzanie przez warstwe 2... ")
        warstwa_2 = warstwa2(lista, warstwa_1, wagi0_v2, wagi1_v2, wagi2_v2, wagi3_v2, wagi4_v2, wagi5_v2, wagi6_v2, wagi7_v2, wagi8_v2, wagi9_v2)
        full = warstwa2(wagi.full, full_p, wagi0_v2, wagi1_v2, wagi2_v2, wagi3_v2, wagi4_v2, wagi5_v2, wagi6_v2, wagi7_v2, wagi8_v2, wagi9_v2)
        print("Przetwarzanie przez warstwe 3... ")
        warstwa_3 = warstwa3(warstwa_2, full)
        print("Podana liczba to ")
        for i in range(len(warstwa_3)):
            print(i, " w ", warstwa_3[i])
    else:
        print("Podana ścieżka nie istnieje!")


def ucz():#fukcja uczenia
    path = input("Pokaż przykład podając do niego ścieżke: ")  # podanie ścieżki przykładu
    exist = os.path.isfile(path)
    if exist == True:
        nazwa = int(input("Wpisz co to: "))  # wpisanie etykiety
        print("Analizowanie obrazu...")
        lista = analiza(path)
        print("Modyfikowanie wag warstwy 1...")
        mod_wag(lista, nazwa)
        print("Modyfikowanie wag warstwy 2...")
        mod_wag_v2(lista, nazwa)
    else:
        print("Podana ścieżka nie istnieje!")

def ucz_bot(path, nazwa):#fukcja uczenia
    print("Analizowanie obrazu...")
    lista = analiza(path)
    print("Modyfikowanie wag warstwy 1...")
    mod_wag(lista, nazwa)
    print("Modyfikowanie wag warstwy 2...")
    mod_wag_v2(lista, nazwa)

def mod_wag(nowe, ktore):
    if ktore == 1:
        for i in range(piksele):
            wagi1[i]=(wagi1[i]+nowe[i])/2
    elif ktore == 2:
        for i in range(piksele):
            wagi2[i]=(wagi2[i]+nowe[i])/2
    elif ktore == 3:
        for i in range(piksele):
            wagi3[i] = (wagi3[i] + nowe[i])/2
    elif ktore == 4:
        for i in range(piksele):
            wagi4[i] = (wagi4[i] + nowe[i])/2
    elif ktore == 5:
        for i in range(piksele):
            wagi5[i] = (wagi5[i] + nowe[i])/2
    elif ktore == 6:
        for i in range(piksele):
            wagi6[i] = (wagi6[i] + nowe[i])/2
    elif ktore == 7:
        for i in range(piksele):
            wagi7[i] = (wagi7[i] + nowe[i])/2
    elif ktore == 8:
        for i in range(piksele):
            wagi8[i] = (wagi8[i] + nowe[i])/2
    elif ktore == 9:
        for i in range(piksele):
            wagi9[i] = (wagi9[i] + nowe[i])/2
    elif ktore == 0:
        for i in range(piksele):
            wagi0[i] = (wagi0[i] + nowe[i])/2

def mod_wag_v2(nowe, ktore):
    if ktore == 1:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi1_v2[i] = 0
    elif ktore == 2:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi2_v2[i] = 0
    elif ktore == 3:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi3_v2[i] = 0
    elif ktore == 4:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi4_v2[i] = 0
    elif ktore == 5:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi5_v2[i] = 0
    elif ktore == 6:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi6_v2[i] = 0
    elif ktore == 7:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi7_v2[i] = 0
    elif ktore == 8:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi8_v2[i] = 0
    elif ktore == 9:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi9_v2[i] = 0
    elif ktore == 0:
        for i in range(piksele):
            if nowe[i] > 0:
                wagi0_v2[i] = 0


def change():#pozwala użytkownikowi wybrać interakcję z programem: 1 - nauka programu, 2 - korzystanie z programu, 3 - wypisanie wag
    try:
        co = input("Co chcesz zrobić: 1: Ucz, 2: Korzystaj, 3: Wypisz wagi: ")
        if co =="1":
            ucz()
        elif co =="2":
            test()
        elif co =="3":
            print("Wagi dla 0: ")
            print(wagi0)
            print("Wagi dla 1: ")
            print(wagi1)
            print("Wagi dla 2: ")
            print(wagi2)
            print("Wagi dla 3: ")
            print(wagi3)
            print("Wagi dla 4: ")
            print(wagi4)
            print("Wagi dla 5: ")
            print(wagi5)
            print("Wagi dla 6: ")
            print(wagi6)
            print("Wagi dla 7: ")
            print(wagi7)
            print("Wagi dla 8: ")
            print(wagi8)
            print("Wagi dla 9: ")
            print(wagi9)
            print(wagi0_v2)
    except:
        print("Wpisz prawdłową cyfrę")



wagi0 = wagi.wagi0
wagi1 = wagi.wagi1
wagi2 = wagi.wagi2
wagi3 = wagi.wagi3
wagi4 = wagi.wagi4
wagi5 = wagi.wagi5
wagi6 = wagi.wagi6
wagi7 = wagi.wagi7
wagi8 = wagi.wagi8
wagi9 = wagi.wagi9

wagi0_v2 = wagi.wagi_v2_0
wagi1_v2 = wagi.wagi_v2_1
wagi2_v2 = wagi.wagi_v2_2
wagi3_v2 = wagi.wagi_v2_3
wagi4_v2 = wagi.wagi_v2_4
wagi5_v2 = wagi.wagi_v2_5
wagi6_v2 = wagi.wagi_v2_6
wagi7_v2 = wagi.wagi_v2_7
wagi8_v2 = wagi.wagi_v2_8
wagi9_v2 = wagi.wagi_v2_9


def bot():
    l = list(os.listdir("0"))
    for i in range(len(l)):
        path = "0\\0v" + str(i + 1) + ".jpg"
        nazwa = 0
        ucz_bot(path, nazwa)

    l = list(os.listdir("1"))
    for i in range(len(l)):
        path = "1\\1v"+str(i+1)+".jpg"
        nazwa = 1
        ucz_bot(path, nazwa)

    l = list(os.listdir("2"))
    for i in range(len(l)):
        path = "2\\2v" + str(i + 1) + ".jpg"
        nazwa = 2
        ucz_bot(path, nazwa)

    l = list(os.listdir("3"))
    for i in range(len(l)):
        path = "3\\3v" + str(i + 1) + ".jpg"
        nazwa = 3
        ucz_bot(path, nazwa)

    l = list(os.listdir("4"))
    for i in range(len(l)):
        path = "4\\4v" + str(i + 1) + ".jpg"
        nazwa = 4
        ucz_bot(path, nazwa)

    """l = list(os.listdir("5"))
    for i in range(len(l)):
        path = "5\\5v" + str(i + 1) + ".jpg"
        nazwa = 5
        ucz_bot(path, nazwa)"""


bot()

while True:
    change()