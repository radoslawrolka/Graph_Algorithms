# Lab 5: Biblioteka NetworkX, planarność, przepływy oraz SAT-2CNF
Głównym celem laboratorium jest zapoznanie się z bilbioteką NetworkX, wspomagającą wykorzystanie algorytmów grafowych w języku Python. Najpierw wykorzystamy jej możliwości do testowania planarności grafów oraz obliczania maksymalnego przepływu, a następnie zajmiemy się algorytmem znajdującym wartościowania spełniające formuły logiczne postaci 2CNF.

## Zadanie 1 (testowanie planarności)
Wykorzystamy bibliotekę NetworkX do testowania, czy dany graf jest planarny. NetworkX ma wbudowany test planarności, więc przede wszystkim musimy wczytać odpowiedni graf, skonstruować go jako obiekt NetworkX i wywołać wbudowaną funkcję.
ń krawędzie z listy (iterowalnego kontenera)

### Testowanie planarności
Testowanie planarności sprowadza się do wywołania jednej funkcji:
```python
from networkx.algorithms.planarity import check_planarity

check_planarity(G)    # czy graf jest planarny? zwraca parę, której pierwszy element to odpowiedź
```
## Zadanie 2 (maksymalny przepływ)
W tym zadaniu wykorzystamy bibliotekę NetworkX do rozwiązania zadania z Lab 2, czyli do znalezienia maksymalnego przepływu w grafie.

### Znalezienie maksymalnego przepływu
Do znalezienia maksymalnego przepływu służy funkcja:
```python
from networkx.algorithms.flow import maximum_flow

maximum_flow( G, s, t )     # znajdź maksymalne przepływ między wierzchołkami s i t grafu G
                            # przepustowość krawędzi jest ustawiana jako jej atrybut 'capacity'
			    # zwraca parę (value,flow) gdzie value to wartość przepływu a
			    # flow to słownik mówiący ile przepływu płynie którą krawędzią

G[1][4]['capacity'] = 7     # ustaw atrybut `capacity` krawędzi (1,4) w grafie G
```
## Zadanie 3 (SAT-2CNF)
W tym zadaniu naszym celem jest zaimplementowanie algorytmu sprawdzającego czy dana formuła logiczna w postaci 2CNF (tj. w postacI koniunkcyjnej normalnej z najwyżej dwoma zmiennymi na klauzulę) jest spełnialna i wypisującego spełniające wartościowanie zmiennych (o ile istnieje).

## Problem SAT-2CNF
Formuła w postaci 2CNF składa się z koniunkcji klauzul, a każda klauzula to alternatywa dwóch literałów (czyli zmiennych lub ich negacji). Poniżej mamy przykładowe formuły F i G:
```python
F = (x or y) and (-x or z) and (-y or -z)
G = (x or y) and (-x or y) and (x or -y) and (-x or -y)
```
Formuła F jest spełnialna. Wystarczy przyjąć:
```python
x = True
y = False
y = True
```
Z kolei formuła G jest niespełnialna (co widać, gdyż zawiera wszystkie możliwe kombinacje negacji/braku negacji pary zmiennych x i y).

### Algorytm
Algorytm sprawdzający spełnialność formuły w postaci 2CNF działa następująco.

- Krok 1 (budowa grafu implikacji). Budujemy graf skierowany G, w którym wierzchołkami są literały (czyli zarówno zmienne jak ich negacje) a krawędzie odpowiadają klauzulom. Konkretnie, jeśli w formule jest klauzula (x or y), to w grafie dodajemy krawędzie skierowane z -x do y oraz z -y do x (odpowiadają one implikacjom (-x => y) oraz (-y => x), które są równoważne alternatywie (x or y)).

- Krok 2 (testowanie spełnialności). Obliczamy silnie spójne składowe grafu G. Jeśli jakaś zmienna x i jej negacja -x znajdują się w tej samej silnie spójnej składowej, to formuła jest niespełnialna. W przeciwnym razie formuła jest spełnialna.

- Krok 3 (konstrukcja wartościowania spełniającego). Jeśli formuła jest spełnialna, to budujemy graf H silnie spójnych składowych grafu G (tj. każda silnie spójna składowa grafu G jest wierzchołkiem grafu H; jeśli G zawiera krawędź z jakiegoś wierzchołka u w silnie spójnej składowej U do wierzchołka v w innej silnie spójnej składowej V, to we H mamy krawędź z U do V). Wiadomo, że H jest dagiem (acyklicznym grafem skierowanym). Sortujemy H topologicznie i przeglądamy spójne składowe w uzyskanym porządku i wykonujemy następującą operację:

  - zmienne/negacje zmiennych w rozważanej silnie spójnej składowej otrzymują wartość False (o ile już nie dostały wcześniej wartości True) (wiadomo, że dla każdej silnie spójnej składowej U istnieje silna spójna składowa -U, która zawiera dokładnie te same literały, ale zanegowane)

W efekcie powstaje wartościowanie zmiennych spełniające wejściową formułę.

### Weryfikacja wartościowania
Proszę zaimplementować sprawdzanie, że uzyskane wartościowanie faktycznie spełnia daną formułę.

### Testowanie rozwiązania
Proszę przetestować zaimplementowany algorytm na przykłądowych danych testowych (patrz niżej). Proszę także zaimplementować własną funkcję sprawdzającą, czy obliczone wartościowanie faktycznie spełnia formułę.
