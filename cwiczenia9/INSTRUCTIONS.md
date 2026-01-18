# Walidacja
Przygotowanie: Sebastian Bętkowski

Grudzień 2025

## RMSD (Root Mean Square Deviation)

**RMSD (root mean square deviation)** jest powszechnie stosowaną miarą podobieństwa struktur w bioinformatyce i biologii strukturalnej. Określa średnią odległość pomiędzy odpowiadającymi sobie atomami dwóch cząsteczek po ich optymalnej superpozycji jako brył sztywnych. W analizie struktur białek RMSD najczęściej oblicza się dla atomów szkieletu głównego lub atomów Cα i wykorzystuje do porównywania trójwymiarowych konformacji.

W kontekście symulacji dynamiki molekularnej RMSD opisuje odchylenie struktury od konformacji referencyjnej lub średniej w czasie. Dla układów fluktuujących wokół dobrze zdefiniowanej pozycji równowagowej stosuje się powiązaną wielkość **RMSF (root mean square fluctuation)**, która charakteryzuje lokalną ruchliwość i elastyczność poszczególnych atomów lub reszt.

Superpozycja wykorzystywana do obliczania RMSD polega na translacji i rotacji jednej struktury względem drugiej w celu minimalizacji wartości RMSD. Problem ten jest standardowo rozwiązywany przy użyciu **algorytmu Kabsha**, który wyznacza optymalną transformację bryły sztywnej.

**Źródło:**  
[Wikipedia (EN): *Root-mean-square deviation of atomic positions*](https://en.wikipedia.org/wiki/Root-mean-square_deviation_of_atomic_positions)

**Definicja matematyczna:**

$$RMSD = \sqrt{\frac{1}{N}\sum_{i=1}^{N} \lVert r_i - r'_i \rVert^2}$$


gdzie:

- N — liczba atomów,
- $r_i$, $r'_i$ — wektory położeń i-tego atomu w obu strukturach (po superpozycji).


**Ważne:**
- superpozycja wykonywana jest przez minimalizację RMSD (np. algorytm Kabsha),
- wynik zależy od wyboru atomów (Cα, backbone, wszystkie atomy),
- metryka jest wrażliwa na lokalne fluktuacje i elastyczne regiony.

---

## TM-score (Template Modeling Score)

**TM-score (Template Modeling Score)** jest miarą podobieństwa struktur białkowych stosowaną w biologii strukturalnej do oceny zgodności globalnego zwoju dwóch struktur po ich optymalnej superpozycji. W przeciwieństwie do RMSD, TM-score jest znormalizowany względem długości białka i zaprojektowany tak, aby być mniej wrażliwym na lokalne odchylenia oraz elastyczne fragmenty struktury.

Wartość TM-score mieści się w zakresie od 0 do 1, gdzie wyższe wartości oznaczają większe podobieństwo strukturalne. Przyjmuje się, że wartości TM-score powyżej 0.5 wskazują na bardzo duże prawdopodobieństwo tego samego zwoju, natomiast wartości poniżej 0.3 odpowiadają podobieństwu losowemu. Dzięki tym właściwościom TM-score jest szczególnie przydatny w porównaniach struktur białek o różnej długości oraz w ocenie jakości modeli predykcyjnych.

**Źródło:**  
[Wikipedia (EN): *Template modeling score*](https://en.wikipedia.org/wiki/Template_modeling_score)

**Definicja matematyczna:**

TM-score definiuje się jako:


$$\mathrm{TM\text{-}score}=\max\left[\frac{1}{L_{\text{target}}}\sum_{i=1}^{L_{\text{common}}}\frac{1}{1 + \left(\frac{d_i}{d_0(L_{target})}\right)^2}\right]$$


gdzie:
- $L_{\text{target}}$ — długość struktury referencyjnej (target),
- $L_{\text{common}}$ — liczba dopasowanych (aligned) reszt aminokwasowych,
- $d_i$ — odległość pomiędzy $i$-tą parą odpowiadających sobie reszt po superpozycji,
- $d_0$ — parametr normalizacyjny zależny od długości struktury.

---

### Porównanie RMSD i TM-score

| Cecha | RMSD | TM-score |
|------|------|----------|
| Wymaga superpozycji | Tak | Tak |
| Zakres wartości | [0, ∞] | [0, 1] |
| Normalizacja względem długości | Nie | Tak |
| Ocena lokalnych różnic | Dobra | Ograniczona |
| Ocena poprawności zwoju | Ograniczona | Bardzo dobra |
| Typowe zastosowanie | MD, ocena zbieżności konformacyjnej | Porównanie struktur, rozpoznawanie zwoju, modele predykcyjne |

---

## GDT (Global Distance Test)

**GDT (Global Distance Test)** jest miarą podobieństwa struktur białkowych stosowaną w biologii strukturalnej, szczególnie w ocenie jakości modeli predykcyjnych. Określa stopień zgodności dwóch struktur po ich optymalnej superpozycji poprzez wyznaczenie odsetka reszt aminokwasowych, które po nałożeniu znajdują się w zadanych progach odległości.

Najczęściej stosowaną wariantą jest **GDT_TS (Total Score)**, który oblicza się jako średnią procentową reszt mieszczących się w czterech progach odległości: 1, 2, 4 i 8 Å. Metryka ta jest mniej wrażliwa na lokalne odchylenia niż RMSD i lepiej odzwierciedla globalne podobieństwo strukturalne.

GDT jest standardową miarą stosowaną w eksperymentach **CASP** do porównywania struktur referencyjnych z modelami predykcyjnymi, gdzie umożliwia obiektywną ocenę jakości globalnego zwoju.

**Źródło:**  
[Wikipedia (EN): *Global distance test*](https://en.wikipedia.org/wiki/Global_distance_test)

**Definicja matematyczna:**


$$\mathrm{GDT\_TS}=\frac{1}{4}\left(P_{1\ \text{Å}} + P_{2\ \text{Å}} + P_{4\ \text{Å}} + P_{8\ \text{Å}}\right)$$


gdzie:
- $P_{d}$ — odsetek reszt aminokwasowych, których odległość po superpozycji jest mniejsza lub równa $d$,
- $d \in \{1, 2, 4, 8\}\ \text{Å}$.

Wartości GDT_TS mieszczą się w zakresie od 0 do 100, gdzie wyższe wartości oznaczają większe podobieństwo struktur.

---

## Verify3D

**Verify3D** jest narzędziem do oceny jakości modeli białkowych, które sprawdza zgodność pomiędzy sekwencją aminokwasową (1D) a jej kontekstem strukturalnym w modelu trójwymiarowym (3D). Metoda ta nie porównuje bezpośrednio dwóch struktur, lecz ocenia, czy środowisko strukturalne każdej reszty aminokwasowej jest zgodne z tym, czego oczekuje się na podstawie statystyk znanych, poprawnych struktur białkowych.

Każdej reszcie przypisywana jest klasa środowiska strukturalnego, uwzględniająca m.in. typ aminokwasu, jego dostępność rozpuszczalnikową oraz charakter otoczenia (np. helisa, β-struktura, pętla). Na tej podstawie obliczany jest wynik punktowy opisujący zgodność sekwencji z modelem 3D. Wysoki wynik Verify3D wskazuje na poprawną lokalną geometrię i realistyczne upakowanie reszt, natomiast niskie wartości mogą sugerować błędy modelu lub niepoprawne przypisanie środowisk strukturalnych.

Verify3D jest często stosowany jako metoda walidacyjna w procesie modelowania strukturalnego białek, szczególnie w połączeniu z innymi metrykami jakości, takimi jak RMSD, GDT czy TM-score.

**Źródło:**  
[Verify3D — DOE-MBI, UCLA](https://www.doe-mbi.ucla.edu/verify3d/)

---

## CheckMyMetal (CMM)

**CheckMyMetal (CMM)** jest narzędziem walidacyjnym służącym do oceny jakości i poprawności geometrycznej centrów metalicznych w strukturach biomolekularnych, w szczególności w strukturach białek zawierających jony metali. Metoda ta analizuje lokalne środowisko koordynacyjne jonów metali na podstawie parametrów geometrycznych oraz statystycznych pochodzących z wysokiej jakości struktur referencyjnych.

CheckMyMetal ocenia m.in. długości wiązań metal–ligand, kąty koordynacyjne, liczbę koordynacyjną, typy ligandów oraz stopień zgodności z oczekiwaną geometrią kompleksu metalicznego. Na tej podstawie generowany jest raport jakościowy, który pozwala zidentyfikować potencjalne błędy modelowania, takie jak nieprawidłowe przypisanie jonów, niefizyczne geometrie koordynacyjne lub brakujące ligandy.

Narzędzie to jest szczególnie przydatne w walidacji struktur wyznaczonych metodami krystalografii rentgenowskiej, kriomikroskopii elektronowej oraz modelowania strukturalnego, gdzie poprawna reprezentacja centrów metalicznych ma kluczowe znaczenie dla interpretacji funkcji biologicznej.

**Źródło:**  
[CheckMyMetal — Minor Lab](https://cmm.minorlab.org/)


### Interpretacja wyników CheckMyMetal

Raport generowany przez **CheckMyMetal** zawiera ocenę jakości centrów metalicznych na podstawie geometrii koordynacyjnej oraz statystyk referencyjnych. Interpretacja wyników opiera się głównie na analizie zgodności długości wiązań, kątów oraz liczby koordynacyjnej z wartościami obserwowanymi w wysokiej jakości strukturach eksperymentalnych.

Najważniejsze elementy interpretacji:
- **Brak ostrzeżeń (warnings)** sugeruje poprawnie zamodelowane centrum metaliczne.
- **Ostrzeżenia dotyczące długości wiązań lub kątów** mogą wskazywać na błędy geometrii, nieprawidłowe przypisanie jonów lub niewłaściwe restrykcje podczas modelowania.
- **Nietypowa liczba koordynacyjna** często sygnalizuje brakujące ligandy lub błędną identyfikację metalu.
- **Niska zgodność statystyczna** z danymi referencyjnymi sugeruje niefizyczną lub mało prawdopodobną konfigurację centrum metalicznego.

Wyniki CheckMyMetal należy interpretować łącznie z innymi metodami walidacyjnymi, ponieważ narzędzie to ocenia wyłącznie lokalne środowisko jonów metali, a nie globalną jakość struktury białkowej.

---

 # ZADANIA

 ---

 ## Zadanie 1.

### Ćwiczenie: Obliczanie RMSD struktur białkowych bez użycia PyMOL

#### Cel ćwiczenia
Celem ćwiczenia jest samodzielna implementacja obliczania **RMSD (Root Mean Square Deviation)** pomiędzy dwiema strukturami białkowymi na podstawie plików PDB, z wykorzystaniem wyłącznie biblioteki **NumPy**. Gotowy skrypt będzie odpowiednikiem użycia w PyMOL'u komend:

<code>load data/7qvb_A.pdb </code>

<code>load data/af2_pred.pdb </code>

<code>pair_fit n. CA and resid 5-158 and m. 7qvb_A and c. A, n. CA and resid 9-162 and m. af2_pred and c. A </code>


---

### Etap 1/5 — Parsowanie pliku PDB

Napisz funkcję `parse_pdb_file`, która wczyta plik PDB i wyodrębni informacje z linii rozpoczynających się od `ATOM` oraz `HETATM`.

Ekstraktowane pola (indeksy 1-based):
- X: pozycje 31–38
- Y: pozycje 39–46
- Z: pozycje 47–54
- AtomName: pozycje 13–16
- ResidueSeqNumber: pozycje 23–26
- ChainID: pozycja 22

Źródło formatu PDB:  
https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html

```python
def parse_pdb_file(file_path):
    atom_data = []

    # TODO:
    # - otwórz plik PDB
    # - iteruj po liniach zaczynających się od "ATOM" lub "HETATM"
    # - wyciągnij odpowiednie pola na podstawie pozycji znaków
    # - dodaj słownik atom_info do listy atom_data

    return atom_data

# użycie funkcji
reference_pdb_path = './data/7qvb_A.pdb'
model_pdb_path     = './data/af2_pred.pdb'

reference_data = parse_pdb_file(reference_pdb_path)
model_data     = parse_pdb_file(model_pdb_path)
```
---
### Etap 2/5 — Filtrowanie danych (CA + zakres reszt)

Napisz funkcję filtrującą dane atomowe:

- tylko atomy Cα
- tylko reszty z podanego zakresu

```python
def filter_atom_data(atom_data, residue_numbers, atom_name):
    filtered_atom_data = []

    # TODO:
    # - sprawdź numer reszty
    # - sprawdź nazwę atomu
    # - dodaj pasujące atomy do filtered_atom_data

    return filtered_atom_data

# użycie funkcji
atom_name_to_filter = 'CA'

filtered_reference_data = filter_atom_data(
    reference_data,
    list(range(5,159)),
    atom_name_to_filter
)

filtered_model_data = filter_atom_data(
    model_data,
    list(range(9,163)),
    atom_name_to_filter
)
```
 ---
 ### Etap 3/5 — Ekstrakcja współrzędnych XYZ

Napisz funkcję zwracającą współrzędne atomów w postaci tablicy `NumPy` o kształcie `(n_atoms, 3)`.

```python
import numpy as np

def extract_xyz_positions(atom_data):
    # TODO:
    # - wyciągnij współrzędne X, Y, Z
    # - zapisz je do tablicy NumPy

    return xyz_positions

# użycie funkcji
filtered_reference_data_xyz = extract_xyz_positions(filtered_reference_data)
filtered_model_data_xyz     = extract_xyz_positions(filtered_model_data)
```
---
### Etap 4/5 — Nałożenie struktur (superpozycja)

Zaimplementuj obliczanie optymalnej rotacji i translacji (algorytm Kabsha) wyłącznie z użyciem NumPy.

### Materiały pomocnicze

- [Nghia Ho — Optimal rotation & translation][ref-nghia]
- [Jason Yu — Derivation of Kabsch algorithm][ref-jason]

[ref-nghia]: https://nghiaho.com/?page_id=671
[ref-jason]: https://jasonblog.github.io/note/math/finding_optimal_rotation_and_translation_between_c.html


```python
def align_coordinates(xyz_moving_A, xyz_fixed_B):
    # TODO:
    # - oblicz środki masy obu zbiorów punktów
    # - przesuń punkty do środka
    # - wyznacz macierz kowariancji
    # - wykonaj SVD
    # - oblicz macierz rotacji R
    # - oblicz wektor translacji t

    return R, t

# użycie funkcji
R, t = align_coordinates(
    filtered_model_data_xyz,
    filtered_reference_data_xyz
)

filtered_model_data_xyz_fitted = filtered_model_data_xyz @ R.T + t
```
---
### Etap 5/5 — Obliczanie RMSD

Zaimplementuj funkcję obliczającą RMSD pomiędzy dwoma zbiorami punktów.
```python
def calculate_rmsd(xyz_A, xyz_B):
    # TODO:
    # - oblicz różnice wektorów
    # - policz średnią kwadratów odległości
    # - wyciągnij pierwiastek

    return rmsd

print(
    f"RMSD pre fit:  {calculate_rmsd(filtered_reference_data_xyz, filtered_model_data_xyz):.3f} Å"
)
print(
    f"RMSD post fit: {calculate_rmsd(filtered_reference_data_xyz, filtered_model_data_xyz_fitted):.3f} Å"
)

```
### Do oddania:

- Kompletny skrypt w Pythonie,

- Wartości RMSD przed i po superpozycji,

- Krótki komentarz (2–3 zdania), dlaczego RMSD po dopasowaniu jest mniejsze.



---
## Zadanie 2.

### Ocena podobieństwa struktur białkowych z użyciem TM-score

### Cel ćwiczenia
Celem ćwiczenia jest porównanie jakości modeli strukturalnych białka względem struktury eksperymentalnej przy użyciu metryki **TM-score**. Studenci uczą się interpretować wartości TM-score oraz porównywać różne modele predykcyjne pod kątem zgodności globalnego zwoju.

#### Narzędzie
Strona internetowa:
[TM-score — Zhang Group](https://zhanggroup.org/TM-score/)

#### Dane wejściowe

**Struktura eksperymentalna (native):**
- `data/7qvb_A.pdb`

**Modele do porównania:**
1. `data/af2_pred_truncated_aligned.pdb`
2. `data/I-TASSER_exclude_truncated_aligned.pdb`
3. `data/I-TASSER_100ident_truncated_aligned.pdb`

#### Instrukcja

1. Wejdź na stronę **TM-score**.
2. W polu *Structure 1* wgraj plik struktury eksperymentalnej (`7qvb_A.pdb`).
3. W polu *Structure 2* wgraj jeden z modeli predykcyjnych.
4. Uruchom obliczenia TM-score.
5. Zanotuj wartości:
   - TM-score,
   - RMSD,
   - liczbę dopasowanych reszt.
6. Powtórz kroki 3–5 dla wszystkich modeli.


#### Tabela do uzupełnienia

| Model | TM-score | RMSD [Å] | Liczba dopasowanych reszt |
|------|----------|----------|----------------------------|
| AF2 | 0.9166 | 2.086 | 214 | 
| I-TASSER (exclude) | 0.3340 | 15.734 | 214 | 
| I-TASSER (100% ident) | 0.9937 | 0.455 | 214 | 


#### Pytania do analizy

1. Który model wykazuje najwyższą wartość TM-score?
    - I-TASSER (100% ident)
2. Czy kolejność modeli według TM-score jest zgodna z kolejnością według RMSD?
    - Tak
3. Które modele przekraczają próg TM-score = 0.5 i co to oznacza?
    - Dwa modele: AF2 i I-TASSER (100% ident). Oznacza to, że te modele mają poprawnie odwzorowany globalny zwój.
4. Jak obecność lub brak homologów wpływa na jakość predykcji struktury?
    - Brak homologów znacząco obniżył jakość predykcji.

---

## Zadanie 3. 

TEGO ZADANIA NIE UDAŁO MI SIĘ ZROBIĆ :/

### Obliczanie wskaźnika GDT na podstawie superpozycji struktur białkowych

#### Cel 
Celem ćwiczenia jest samodzielne obliczenie wskaźnika **GDT (Global Distance Test)** dla modeli strukturalnych białka na podstawie superpozycji ze strukturą eksperymentalną oraz porównanie jakości dwóch modeli predykcyjnych.

#### Instrukcja
Uzupełnij przygotowany szablon skryptu w języku Python (PyMOL API) tak, aby:

1. Obliczyć wartości **GDT_P1, GDT_P2, GDT_P4, GDT_P8** na podstawie odległości pomiędzy atomami Cα odpowiadających sobie reszt.
2. Obliczyć końcowy wskaźnik **GDT_TS**.
3. Wykonać obliczenia osobno dla:
   - modelu **AlphaFold** (`data/af2_pred_truncated_aligned.pdb`),
   - modelu **I-TASSER (exclude)** (`data/I-TASSER_exclude.pdb`),
   - modelu **I-TASSER (100ident)** (`data/I-TASSER_100ident.pdb`),

#### Do oddania
- Uzupełniony skrypt obliczający GDT,
- Wartości **GDT_P1, GDT_P2, GDT_P4, GDT_P8** oraz **GDT_TS** dla wszystkich modeli

```python
# =========================
# GDT calculation in PyMOL
# =========================

#conda install conda-forge::pymol-open-source
#pip install pymol-open-source
import pymol
from pymol import cmd

cmd.delete('all')

#załadowanie struktur

# pymol.cmd.load('./data/7qvb_A.pdb', object="reference")
# pymol.cmd.load('./data/af2_pred.pdb', object="model_af")
# pymol.cmd.load('./data/I-TASSER_exclude.pdb', object="model_itasser_exclude")
# pymol.cmd.load('./data/I-TASSER_100ident.pdb', object="model__itasser_100ident")

# --- superposition ---
cmd.pair_fit(
    "n. CA and resid 9-162+173-226 and m. model_ and c. A",
    "n. CA and resid 5-158+169-222 and m. reference and c. A and not alt B"
)

# --- residue mapping ---
model_resids     = list(range(9,163))  + list(range(173,227))
reference_resids = list(range(5,159))  + list(range(169,223))

assert len(model_resids) == len(reference_resids)

# --- counters ---
n_1 = 0
n_2 = 0
n_4 = 0
n_8 = 0

n_total = len(reference_resids)

# TODO:
# 1. Przejdź pętlą po parach reszt (model_resids, reference_resids)
# 2. Zdefiniuj selekcje atomów CA dla modelu i referencji
# 3. Oblicz dystans między atomami CA za pomocą cmd.get_distance()
# 4. Zwiększ odpowiednie liczniki (1 Å, 2 Å, 4 Å, 8 Å)

# TODO:
# Oblicz GDT_P1, GDT_P2, GDT_P4, GDT_P8 (w procentach)

# TODO:
# Oblicz GDT_TS jako średnią z czterech progów

# print(GDT_P1, GDT_P2, GDT_P4, GDT_P8)
# print("GDT_TS = %.2f%%" % GDT_TS)
```
---

## Zadanie 4. 

 ### Walidacja jakości modeli strukturalnych z użyciem Verify3D

#### Cel ćwiczenia
Celem ćwiczenia jest ocena lokalnej jakości struktur białkowych przy użyciu narzędzia **Verify3D**, które bada zgodność sekwencji aminokwasowej (1D) z jej środowiskiem strukturalnym w modelu trójwymiarowym (3D). Studenci porównają strukturę eksperymentalną z modelami predykcyjnymi oraz nauczą się interpretować procent reszt spełniających kryterium jakości Verify3D.

---

#### Narzędzie
Strona internetowa:
- [Verify3D — DOE-MBI, UCLA](https://www.doe-mbi.ucla.edu/verify3d/)
- biblioteka `matplotlib`

---

#### Dane wejściowe

**Struktura eksperymentalna (referencja):**
- `data/7qvb_A.pdb`

**Modele predykcyjne:**
- `data/af2_pred.pdb` (AlphaFold2)
- `data/I-TASSER_exclude.pdb` (I-TASSER)


#### Instrukcja

1. Wejdź na stronę **Verify3D**.
2. Wgraj plik `data/7qvb_A.pdb` i uruchom analizę.
3. Zanotuj wartość:
   
   **X % of the residues have averaged 3D-1D score ≥ 0.1**
4. Powtórz analizę dla plików:
   - `data/af2_pred.pdb`
   - `data/I-TASSER_exclude.pdb`
5. Dla modelu **AlphaFold2** kliknij przycisk **“Save to data file”** i zapisz wygenerowany plik z wynikami.


#### Tabela do uzupełnienia

| Struktura | % reszt z 3D-1D score ≥ 0.1 |
|----------|-----------------------------|
| 7qvb_A.pdb (referencja) | 77.10% |
| af2_pred.pdb (AlphaFold2) | 71.91% |
| I-TASSER_exclude.pdb (I-TASSER) | 52.34% |


#### Analiza danych z Verify3D (AlphaFold2)

Na podstawie pliku zapisanego przy użyciu opcji **“Save to data file”**:

1. Wczytaj dane do wybranego narzędzia (np. Python)
2. Wartości *averaged 3D–1D score* podziel na trzy klasy jakości lokalnej struktury:
- **Klasa dobra (zielona):** score ≥ 0.2  
- **Klasa akceptowalna (żółta):** 0.0 ≤ score < 0.2  
- **Klasa zła (czerwona):** score < 0.0
3. Wygeneruj wykres przedstawiający:
   - numer reszty (oś X),
   - wartość *averaged 3D-1D score* (oś Y).
   - kolor reszt na wykresie odpowiadający przynależności do klasy
4. Wygeneruj wykres kołowy, przedstawiający procentowy udział trzech klas jakości  
   (ile reszt należy do klasy dobrej, akceptowalnej i złej).


#### Do oddania
- Uzupełniona tabela wyników,
- Wygenerowane wykresy dla modelu AlphaFold2,
- Krótki komentarz (3–5 zdań) interpretujący uzyskane wyniki.
    - Większość reszt w modelu AlphaFold znajduje się w klasie dobrej lub akceptowalnej, co świadczy o poprawnym dopasowaniu sekwencji do modelu strukturalnego. Obszary o ujemnych wynikach występują głównie na końcach łańcucha, ponieważ te fragmenty są trudniejsze do predykcji. Ogólnie wysoki udział reszt o pozytywnym wyniku potwierdza, że model jest wiarygodny.

---

## Zadanie 5. 

### Walidacja centrum metalicznego przy użyciu CheckMyMetal

#### Cel
Celem zadania jest sprawdzenie, czy narzędzie **CheckMyMetal** potrafi wykryć niezgodność pomiędzy typem jonu metalu a jego środowiskiem koordynacyjnym.

#### Materiały
- CMM: https://cmm.minorlab.org/

Instrukcje:

1. Wejdź na stronę CheckMyMetal
2. Załaduj oryginalny plik PDB (np. 3eef).
3. Uruchom walidację i zapisz raport dla wersji z oryginalnym metalem (Zn2+).
4. Zapisz zestawienie parametrów walidacyjnych
5. Przejdź do trybu MODEL.
6. Wybierz opcję "Replace Metal Ion".
7. Zastąp Zn2+ jonem Mg2+.
8. Uruchom walidację ponownie ("Change and refine") i zapisz raport dla wersji z Mg2+.
9. Zapisz zestawienie parametrów walidacyjnych
10. Wyeksportuj obrazy pokazujące miejsce wiązania dwóch różnych jonów metalu z nałożoną mapą gęstości elektronowej. 

Tabela do uzupełnienia:

| Parametr | Zn2+ (oryginał) | Mg2+ (MODEL) |
|----------|------------------|--------------|
| Occupancy| 0.5 | 0.5| 
| Bfactor | 44.3 (51.7) | 24.2 (60.5) | 
| Atomic contacts | 4 | 4 | 
| Valence | 1.4 | 1.5 | 
| nVECSUM | 0.17 | 0.2 | 
| Geometry | Tetrahedral | Tetrahedral | 
| gRMSD| 22.2 | 22.2 | 
| Vacancy | 0 | 0 | 
| Bidentate | 0.0 | 0.0 |

Pytania:
1. Czy CheckMyMetal zgłasza ostrzeżenia dla wersji z Mg2+? Jakie?
    - Tak, CMM niektóre elementy w raporcie zaznacza na czerwono, co może dać sygnał, że coś jest nie tak (np. za niski B-factor w porównaniu do otoczenia)
2. Które parametry geometrii uległy pogorszeniu?
    - Głównie B-factor oraz Valence, co oznacza złe dopasowanie wiązań
3. Czy geometria koordynacyjna jest zgodna z preferencjami Mg2+?
    - Nie. Wykryta geometria tetraedryczna, a magnez preferuje geometrię oktaedryczną
4. Jak mapa gęstości elektronowej wspiera lub podważa obecność Mg2+?
    - Tego niestety nie wiem
5. Na podstawie danych – który jon jest bardziej prawdopodobny?
    - Zn2+

*Załącz wyeksportowane grafiki*

