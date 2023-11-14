# Lab 3: Spójność krawędziowa
W ramach laboratorium należy zaimplementować algorytmy obliczające spójność krawędziową grafu

## Zadanie 1
Dany jest graf nieskierowany G = (V,E). Spójnością krawędziową grafu G nazywamy minimalną liczbę krawędzi, po których usunięciu graf traci spójność. Przykładowo:

- spójność krawędziowa drzewa = 1
- spójność krawędziowa cyklu = 2
- spójność krawędziowa n-kliki = n-1
Opracuj i zaimplementuj algorytm obliczający spójność krawędziową zadanego grafu G, wykorzystując algorytm Forda-Fulkersona oraz następujący fakt:

(Tw. Mengera) Minimalna ilość krawędzi które należy usunąć by zadane wierzchołki s, t znalazły się w różnych komponentach spójnych jest równa ilości krawędziowo rozłącznych ścieżek pomiędzy s i t

Wskazówka: jak można zinterpretować ilość krawędziowo rozłącznych ścieżek jako problem maksymalnego przepływu? Proszę wykorzystać kod opracowany w ramach Laboratorium 2.

## Zadanie 2
Proszę zaimplementować program obliczający spójność krawędziową grafu nieskierowanego G przy użyciu algorytmu Stoera-Wagnera.

Algorytm stworzony w ramach zadania 1 nie jest optymalny (nie sprawdza się zbyt dobrze np. dla dużych klik). Głównym jego składnikiem jest algorytm Forda-Fulkersona zaprojektowany z myślą o znajdowaniu maksymalnych przepływów pomiędzy dwoma określonymi wierzchołkami. Problem znajdowania spójności krawędziowej sprowadza się natomiast do poszukiwania pary wierzchołków, pommiędzy którymi maksymalny przepływ jest najmniejszy, stąd używając algorytmu przeznaczonego do tego problemu dostaniemy rozwiązanie o mniejszej złożoności obliczeniowej.

### Implmentacja algorytmu Stoera-Wagnera
Dokładny opis algorytmu znajduje się na stronach powyżej. Tutaj przedstawiamy porady jak go implementować.

Algorytm Stoera-Wagnera opiera się na dwóch głównych operacjach:

- znajdowanie minimalnego przecięcia dla pewnych dwóch wierzchołków (algorytm podobny w działaniu do algorytmu Dijkstry)
- scalaniu wierzchołków
  
Scalanie wierzchołków:

Algorytm Stoera-Wagnera wykorzystuje operację łączenia wierzchołków. Jeśli łaczymy wierzchołek x z wierzchołkiem y to dla każdego wierzchołka z, który jest połączony krawędzią z przynajmniej jednym z nich, mamy teraz krawędż łączącą nowy wierzchołek xy z wierzchołkiem z o wadze będącej sumą wag krawędzi między x i z oraz między y i z. Jeśli występowała jakaś krawędź między x i y to znika.

Najprostszy sposób implementacji to stworzenie funkcji, która usuwa wszystkie krawędzie np. z wierzchołka y i dodaje je do x:
```python
def mergeVertices( G, x, y ):
  ...
```
Warto także w każdym aktywnym wierzchołku mieć informację jakie wierzchołki zostały z nim scalone (pozwala to odczytać optymalne przecięcie grafu).

Znajdowanie minimalnego przecięcia dla pewnych dwóch wierzchołków (MinimumCutPhase):

Podstawowa operajca w algorytmie Stoera-Wagnera to znalezienie pewnych dwóch wierzchołków s i t oraz takiego minimalnego przecięcia C = (S,T), że s należy do S a t należy do T.

Jest to realizowane przez następującą pętlę:
```python
def minimumCutPhase( G ):

  a = dowolny wierzcholek # może to zawsze być wierzchołek numer 1 (lub 0 po przenumerowaniu)
  S = {a}

  while S nie zawiera wszystkich wierzcholkow:
    znajdz taki wierzcholek v, ze suma wag krawedzi z v do
    wierzcholkow w S jest maksymalna

    dolacz v do S (zapamietujac kolejnosc dodawania)

  s = ostatni wierzcholek dodany do S
  t = przedostatni wierzcholek dodany do S

  # tworzone przecięcie jest postaci S = {s}, T = V - {s}
  zapamietaj sume wag krawedzi wychodzacych z s jako potencjalny_wynik

  mergeVertices(G,s,t)

  return potencjalny_wynik
```
Główny algorytm:

Główny algorytm sprowadza się do wykonywania funkcji minimumCutPhase aż zostanie tylko jeden wierzchołek. Jako rozwiązanie należy zwrócić minimalny z uzyskanych potencjalnych wyników.

Jeśli przechowujemy listę wierzchołków reprezentowanych przez dany wierzchołek, to możemy także odtworzyć minimalne przecięcie. Wykonanie minimumCutPhase, które daje minimalny wynik może w tym celu zwrócić wierzchołek s; minimalne przecięcie tworzą reprezentowane przez niego (w tym momencie) wierzchołki.
