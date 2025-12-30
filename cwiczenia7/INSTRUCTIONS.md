<b>Przygotował:</b> Michał Gucwa <br>
<b>Aktualizacja:</b> Sebastian Bętkowski gru 2025
<!-- There are no Easter Eggs up here, Go away -->

<h3>Metody przewidywania i walidacji struktury przestrzennej białek. Rola metaserwerów predykcyjnych w stymulowaniu rozwoju bioinformatyki strukturalnej.</h3>

<p1>Funkcja biologiczna białka związana jest z jego strukturą przestrzenną, którą można wyznaczyć
metodami doświadczalnymi i obliczeniowymi. 

W modelowaniu porównawczym, model struktury białka konstruowany jest na podstawie informacji zawartych w strukturze białek spokrewnionych ewolucyjnie. Zasadność stosowania metod porównawczych wynika z faktu, że struktura jest bardziej konserwatywna niż sekwencja.

Istota metody modelowania porównawczego sprowadza się do wykrycia pokrewieństwa
ewolucyjnego między białkami o znanej i nieznanej strukturze przestrzennej (temat przewodni
poniższego ćwiczenia) i wykorzystaniu informacji strukturalnej z białka szablonu (ang. template
protein) do skonstruowania modelu struktury białka celu (ang. target protein).

Używane programy podczas zajęć:<br>
- PyMOL<br>
- AlphaFold2<br>
- AlphaFold3<br>
- I-TASSER<br>


<b>Proszę odpowiedzieć na pytania a następnie:<br>
Zdeponować w <i>Assignment</i> w zespole Teams
</b>
</p1>

# I-TASSER

## Czym jest I-TASSER?

I-TASSER Server to internetowa platforma wykorzystująca algorytmy rodziny I-TASSER do przewidywania struktury 3D i funkcji biologicznej białek.
Umożliwia użytkownikom akademickim automatyczne generowanie wysokiej jakości modeli na podstawie samej sekwencji aminokwasowej, bez potrzeby posiadania znanej struktury eksperymentalnej.

[🔗 I-TASSER Server](https://zhanggroup.org/I-TASSER/)


## Jak działa I-TASSER

### 1. Wyszukiwanie szablonów (threading)

Po podaniu sekwencji białka serwer uruchamia LOMETS, czyli meta-server łączący wiele algorytmów threadingu. Jego zadaniem jest znalezienie w bazie PDB struktur o podobnym ułożeniu domen lub motywów drugorzędowych.

### 2. Składanie modelu (assembly)

Z odnalezionych szablonów wycina się ciągłe fragmenty, które następnie są składane w pełną strukturę za pomocą symulacji replica-exchange Monte Carlo.
Niedopasowane rejony — głównie pętle — są dogenerowane metodami ab initio.

Jeśli LOMETS nie znajdzie odpowiednich szablonów, całe białko modelowane jest de novo.
Najniższe energetycznie konformacje identyfikuje algorytm SPICKER poprzez klasteryzację uzyskanych struktur.

### 3. Udokładnianie i druga iteracja składania

Symulacje składania są uruchamiane ponownie, tym razem startując z centroidów klastrów SPICKER.
W tej fazie model jest prowadzony przez restrykcje przestrzenne pochodzące z szablonów LOMETS oraz dopasowań strukturalnych z PDB (TM-align).
Celem drugiej iteracji jest:

- usunięcie kolizji sterycznych,

- poprawa ogólnej topologii modelu.

Nowe struktury są ponownie klastrowane i wybierane są te o najniższej energii.

### 4. Finalizacja modelu atomowego

Wybrane modele szkieletowe są konwertowane do pełnej reprezentacji atomowej przez REMO, który odbudowuje szczegóły atomowe i optymalizuje sieć wiązań wodorowych.


[![I-TASSER pipeline](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/I-TASSER-pipeline.jpg/1200px-I-TASSER-pipeline.jpg)](https://zhanggroup.org/I-TASSER/about.html)

*Źródło: Zhang Lab — I-TASSER server (https://zhanggroup.org/I-TASSER/about.html)*

## Jak interpretować wyniki generowane przez serwer I-TASSER?

Po zakończeniu modelowania serwer wysyła użytkownikowi link do strony z podsumowaniem wyników. Poniżej znajdują się wyjaśnienia najważniejszych elementów, które pojawiają się w outputach I-TASSER.

*Na potrzeby ćwiczeń wygenerowano przykładowe wyniki predykcji przy użyciu I-TASSER'a*

### Top 10 templates used by I-TASSER

Modelowanie zaczyna się od wyszukania szablonów strukturalnych przez LOMETS (zestaw różnych programów threading).
Każdy program generuje dużą liczbę potencjalnych szablonów, ale I-TASSER wybiera tylko najbardziej znaczące, oceniane na podstawie Z-score (różnicy między wynikiem raw a średnią, w jednostkach odchylenia standardowego).

Top 10 templates to dziesięć szablonów o najwyższym znaczeniu, zwykle po 1–2 najlepsze z każdego narzędzia threadingowego.

### Top 5 models predicted by I-TASSER

Podczas symulacji I-TASSER generuje dziesiątki tysięcy konformacji (decoys).
Są one klastrowane przez algorytm SPICKER, a maksymalnie pięć największych klastrów jest wybieranych jako:

- Model 1 — największy klaster (najniższa energia → najwyższe prawdopodobieństwo),

- Model 2–5 — kolejne klastry malejące wielkością.

Choć modele są sortowane po wielkości klastrów, czasami model o niższym numerze rankingu może mieć wyższy C-score.
Jeśli symulacje mocno się zbiegną, może pojawić się mniej niż 5 klastrów — zwykle oznacza to dobre modele.

### Proteins structurally close to the target in the PDB

I-TASSER dopasowuje pierwszy model do wszystkich struktur z PDB za pomocą TM-align. W tej sekcji prezentowane są najbardziej podobne strukturalnie białka (najwyższe TM-score).

### C-score 

C-score to główna metryka oceny jakości modelu I-TASSER.
Opiera się na:

- jakości dopasowań z threadingu,

- zbieżności symulacji składania struktury.

Zakres: od −5 do 2, gdzie wyższe wartości = większa pewność.

### TM-score

TM-score mierzy podobieństwo topologii dwóch struktur 3D.
Jest odporny na lokalne błędy (w przeciwieństwie do RMSD).

Interpretacja:

- TM-score > 0.5 → poprawna topologia,

- TM-score < 0.17 → przypadkowe podobieństwo.

Cutoffy są niezależne od długości białka.

## Zadanie 1.

W ćwiczeniu będziemy pracowali na białku o sekwencji:

<code>GAMGMKNAPLTLNFGSVRLPVSADGLLHAPTAQQQLGLTQSWEAALVEHGLPETYRDFG
AGPEAAVSVPDFVALAFALDTPEARRWQKRARELLARAMQGDVRVAAQIAERNPEPDARR
WLAARLESTGARRELLATVARHGGEGRVYGQLGSISNRTVLGKDSASVRQERGVKATRDGL
TSAELLRLAYIDTVTARAIQESEARGNAAILTLHEQVARSERQSWERAGQVQRVG</code>

To białko było jednym z bialek użytych w CASP15 (Tar-id: T1120). 

Na potrzeby ćwiczeń wygenerowano wyniki predykcji struktury tego białka, dla dwóch przypadków:

- <b>A</b>) z wykluczeniem struktur szablonowych o wysokim stopniu identyczności <code>data/iTASSER_exclude/</code>
- <b>B</b>) bez odrzucania struktur szablonowych o wysokim stopniu identyczności <code>data/iTASSER_100ident/</code>

Wyniki predykcji znajdują się w odpowiednich folderach w pliku <code>index.html</code>

### 1.1 Podać trzy najważniejsze struktury użyte jako szablony w modelowaniu homologicznym analizowanej sekwencji 

*A):*
- ...
- ...
- ...

*B):*

- ...
- ...
- ...

### 1.2 Podać szacowany TM, RMSD oraz C-score dla modelu 1.

*A):*
- TM = ...
- RMSD = ...
- C-score = ...

*B):*
- TM = ...
- RMSD = ...
- C-score = ...

### 1.3 Obejrzeć przewidywaną strukturę w PyMOL i podać RMSD względem struktury szablonowej *7qvb*. Czy I-TASSER poprawnie przewidział szacowane RMSD modeli?

*A):*
- RMSD = ...

*B):*
- RMSD = ...

### 1.4 Dla którego przypadku (z odrzuceniem/bez odrzucania) I-TASSER lepiej poradził sobie z predykcją struktury, dlaczego?

...

# AlphaFold 2
AlphaFold 2 to wersja algorytmu DeepMind z 2020 roku, która znacznie różni się od wcześniejszej edycji z 2018 r. W przeciwieństwie do AlphaFold 1, który składał się z kilku osobnych modułów połączonych z klasycznymi metodami fizycznymi, AlphaFold 2 jest jednolitym modelem typu end-to-end, opartym całkowicie na sieciach neuronowych i rozpoznawaniu wzorców.

Model uczy się przewidywać strukturę przestrzenną białka bez podziału na etapy, a wszystkie elementy systemu są trenowane jednocześnie. Dopiero na sam koniec stosowana jest niewielka optymalizacja energii (minimization) przy użyciu pola siłowego AMBER, która delikatnie koryguje lokalną geometrię.

[🔗AlphaFold – źródło (GitHub, DeepMind)](https://github.com/google-deepmind/alphafold)

## Jak działa AlphaFold?
### 1. Evoformer — główny blok przetwarzania informacji

Evoformer to zestaw dwóch współpracujących ze sobą modułów (opartych na architekturze transformerów):

- moduł reszta–reszta (residue–residue)
aktualizuje informacje o wzajemnych relacjach między każdą parą aminokwasów,

- moduł reszta–MSA (residue–multiple sequence alignment)
analizuje powiązania między pozycjami w białku a homologami z MSA.

Oba moduły wymieniają między sobą informacje i są wykonywane wielokrotnie. W każdej iteracji model „czyści” i uściśla dane dotyczące zależności przestrzennych i ewolucyjnych.

### 2. Structure Module — przewidywanie współrzędnych 3D

Po przetworzeniu danych przez Evoformer informacje trafiają do modułu strukturalnego, który generuje współrzędne atomów białka.

Model wykonuje kilka kolejnych iteracji przewidywania. W każdej z nich poprawia:

- topologię struktury,

- geometrię wiązań i kątów,

- liczbę błędów stereochemicznych.

Pierwsze iteracje zwykle dają poprawną ogólną strukturę, a kolejne poprawiają dokładność.

### 3. Refinement (AMBER)

Na końcu integruje się lekki etap optymalizacji energii przy użyciu pola siłowego AMBER.
Ten krok nie zmienia ogólnej struktury, a jedynie koryguje szczegóły geometryczne.

![Architecture of AlphaFold 2](https://lh3.googleusercontent.com/pL18FAkwzN55iHvMt2W4XRGjueHWe0ILqX1Qm2e4qlPsK3yjDSott3LZIgSg2uqPPn7Zvu3hfxUtYtjDs3bM27zcF8AO_jYnfk8q%3Dw1440)
  
*Źródło: „AlphaFold 2: Attention Mechanism for Predicting 3D Protein Structures” — PIIP blog (https://piip.co.kr/en/blog/AlphaFold2_Architecture_Improvements)*  

## Jak interpretować wyniki AlphaFold 2

### 1. pLDDT (local confidence score)

Skala: 0–100
To ocena pewności modelu dla każdej reszty.

Interpretacja:

- 90–100 — bardzo wysoka pewność,

- 70–90 — wiarygodny poziom pewności,

- 50–70 — niepewne regiony, możliwa elastyczność,

- <50 — prawdopodobnie nieustrukturyzowane fragmenty (IDP, pętle).

### 2. PAE (Predicted Aligned Error)

Macierz przewidywanego błędu między parami reszt.
Wskazuje, jak pewne jest względne ułożenie domen lub segmentów białka.

- niski PAE — stabilna orientacja,

- wysoki PAE — domeny mogą się swobodnie poruszać względem siebie.

### 3. Ranking modeli

AlphaFold generuje kilka modeli i sortuje je według przewidywanej jakości (średniego pLDDT).
Najczęściej najlepszy jest model rank_0.

## Zadanie 2.

Na potrzeby ćwiczeń korzystając z AF2 wygenerowano predykcje struktury *7qvb* oraz *7qvb dimer*. Pliki wyjściowe po wykonaniu predykcji znajdują się w folderach odpowiednio:

- data/af2/7qvb/output/
- data/af2/7qvb_dimer/output

### 2.1 Analizując plik <code>coveraged_LDDT.png</code> z folderu <code>7qvb</code> spróbuj wytłumaczyć zmniejszony parametr LDDT w okolicach 109-116 reszty aminokwasowej przewidzianej struktury. 

...

### 2.2 Wykorzystując program PyMOL porównaj strukturę przewidywaną przez AF2 (<code>.../7qvb/output/relaxed_model_1_multimer_v2_pred_2.pdb</code>) z wynikami eksperymentalnymi (<code>7qvb</code>). Jakie jest RMSD?

- RMSD = ...


### 2.3 Zlokalizuj miejsce charakteryzowane mniejszym LDDT a następnie napisz jaka to struktura.

...

### 2.4 Wyświetl aminokwasy hydrofobowe. Czy znajdują się na powierzchni przewidzianej struktury jakieś ugrupowania aminokwasów hydrofobowych? Czy można podejrzewać, że białko to występuje w formie dimeru?

...

### 2.5 Załaduj plik <code>.../af2/7qvb_dimer/output/relaxed_model_3_multimer_v2_pred_0.pdb</code> oraz strukture eksperymentalną <code>7qvb</code> do programu PyMOL. Pokoloruj łańcuchy (na niebiesko łańcuchy A, na zielono łańcuchy B, ciemnym kolorem strukture ekseprymentalna a przeiwdywaną przez AF2 jasnym). Dopasuj globalnie te struktury, czy jest ono akceptowalne? Jakie jest RMSD?

- RMSD = ...

...

### 2.6 Czy globalne dopasowanie dla łańuchów A i B są akceptowalne? Jakie jest RMSD?

- RMSD (łańcuch A) = ...
- RMSD (łańcuch B) = ...

### 2.7 Sprawdź dwa lokalne dopasowania łańcucha B i podaj ich RMSD:

- 1: <code>n. CA and c. B and resid 1-121 </code>
- 2: <code>n. CA and c. B and resid 125-230 </code>

- RMSD_1 = ...
- RMSD_2 = ...

### 2.8 Opisz największą różnicę pomiędzy strukturą eksperymentalna a przewidzianą przez AF2. Czy ta różnica jest spowodowana odmienną konformacją krótkiego fragmentu łańcucha czy może dłuższy fragment został niepoprawnie przewidziany. Podaj zakres reszt które wprowadzają największą różnicę pomiedzy tymi dwoma strukturami.

...

# AlphaFold 3

AlphaFold 3 to najnowsza wersja systemu DeepMind do modelowania struktur biologicznych. W przeciwieństwie do AlphaFold 2, który przewidywał głównie struktury pojedynczych białek (lub prostych kompleksów w wersji Multimer), AlphaFold 3 rozszerza zakres działania o białko–DNA, białko–RNA, interakcje z ligandami, modyfikacje chemiczne oraz bardziej złożone kompleksy.
Model wykorzystuje nową architekturę bazującą na tzw. diffusion models, co pozwala przewidywać nie tylko strukturę, ale też wiązania i interakcje w znacznie bardziej ogólnym ekosystemie biomolekularnym.

[🔗AlphaFold 3 Server (DeepMind)](https://alphafoldserver.com/)

## Porównanie AlphaFold 2 i AlphaFold 3

| **Kategoria**                     | **AlphaFold 2**                                                 | **AlphaFold 3**                                                                 |
|----------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Zakres modelowanych struktur** | Struktury białek; Multimer dla prostych kompleksów              | Białka, DNA, RNA, ligandy, jony, modyfikacje chemiczne, złożone kompleksy        |
| **Architektura modelu**          | Transformery (Evoformer + Structure Module)                     | Diffusion models (generowanie przez odszumianie), nowa architektura              |
| **Dane wejściowe**               | Sekwencja białka + MSA                                          | Sekwencje wielu typów cząsteczek; informacje chemiczne i strukturalne            |
| **Interakcje**                   | Dobre dla białko–białko (Multimer)                              | Szeroki zakres: białko–DNA, białko–RNA, białko–ligand, inne biomolekuły          |
| **Dokładność interfejsów**       | Ograniczona, zależna od MSA                                     | Znacznie wyższa dokładność przewidywania interakcji                              |
| **Zastosowania**                 | Modelowanie struktury białek                                    | Modelowanie kompleksów, analiza interakcji, projektowanie leków                  |
| **Refinement**                   | Lekki refinement (AMBER), minimalne poprawki                    | Wbudowana w generację struktury (diffusion), bez osobnego etapu fizycznego       |
| **Dostępność kodu**              | Open-source (GitHub)                                             | Kod zamknięty; dostępny publiczny serwer                                         |

## Zadanie 3. Korzystając z servera AF3 (link wyżej) wykorzystaj wcześniej analizowaną sekwencję *7qvb*. Przeprowadź podobne analizy jak dla AF2 i odpowiedz na pytania:

###   Które regiony białka mają słaby plDDT?
...
### Czy AF3 lepiej radzi sobie z przeiwdywaniem struktury od AF2?
...
### Jakie jest RMSD względem struktury eksperymentalnej?

...

