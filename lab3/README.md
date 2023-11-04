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
