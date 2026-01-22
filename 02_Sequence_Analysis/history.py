# wykorzystaj funkcję print(),
# aby wyświetlić zawartość dokumentacyjnego
# ciągu tekstowego (docstring)
# funkcji print(), czyli ciąg zapisany
# w zmiennej print.__doc__
print(print.__doc__)
# a teraz wyświetl tę zawartość,
# stosując magiczną komendę %pdoc
%pdoc print
# spróbuj ponownie zrobić to samo,
# stosując skrót klawiaturowy Shift + Tab
# tuż po wpisaniu nazwy funkcji
print
# zaimportuj moduł numpy a następnie
# wyświetl pomoc do funkcji np.stack,
# stosując pojedynczy znak zapytania
# postawiony za nazwą funkcji
import numpy

%pdoc numpy.stack
# wyświetl pomoc do funkcji np.stack,
# tym razem korzystając z podwójnego
# znaku zapytania
%pdoc numpy.stack??
# zapisz cały dotychczasowo uruchamiany kod
# do pliku output/history.py

%history -f history.py
# zapisz cały dotychczasowo uruchamiany kod
# do pliku output/history.py

%history -f history.py
