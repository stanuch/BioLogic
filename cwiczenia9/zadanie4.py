import matplotlib.pyplot as plt

file = open('data_zadanie4.txt', 'r')

numery_reszt = []
wyniki = []
kolory = []

ile_dobrych = 0      # wynik >= 0.2
ile_srednich = 0     # wynik 0.0 - 0.2
ile_zlych = 0        # wynik < 0.0

for linia in file:
    linia = linia.strip()
    
    if len(linia) > 0:
        czesci = linia.split() 
        tekst_numer = czesci[0]
        tekst_wynik = czesci[3]

        numer = int(tekst_numer)
        wynik = float(tekst_wynik)

        numery_reszt.append(numer)
        wyniki.append(wynik)

        if wynik >= 0.2:
            kolory.append('green')
            ile_dobrych = ile_dobrych + 1
            
        elif wynik >= 0.0:
            kolory.append('yellow') 
            ile_srednich = ile_srednich + 1
            
        else:
            kolory.append('red')
            ile_zlych = ile_zlych + 1

file.close()

plt.figure(figsize=(10, 5))
plt.bar(numery_reszt, wyniki, color=kolory)

plt.xlabel("Numer reszty")
plt.ylabel("Uśredniony wynik 3D-1D")
plt.title("Jakość modelu")
plt.show()

plt.figure()
liczby = [ile_dobrych, ile_srednich, ile_zlych]
podpisy = ['Dobra (>=0.2)', 'Akceptowalna (0-0.2)', 'Zła (<0.0)']
kolory_kola = ['green', 'yellow', 'red']

plt.pie(liczby, labels=podpisy, colors=kolory_kola, autopct='%1.1f%%')
plt.title("Udział klas jakości")
plt.show()