## Treść zadania
Królestwo Bajtycji przygotowuje się do obchodów 100-nej rocznicy zakończenia wieloletniej wojny z sąsiednim Księstwem Qubicji. Z tej okazji Król Bajtoklecjan postanowił zorganizować paradę wojskową ulicami stolicy Królestwa - Bajtogrodu. Twoim zadaniem będzie wyznaczenie trasy parady.

Defilada maszerować będzie przez rozmaite place Bitogrodu, połączone ze sobą ulicami. Wyjątkowe znaczenie dla mieszkańców stolicy mają place nazywawne tranzytowymi - są to te place, które leżą na każdej drodze pomiędzy pewnymi dwoma sąsiadującymi z nimi placami. Po wojnie wybudowano na każdym z nich łuk tryumfalny, by uczcić pamięć przechodzących tamtędy, zmierzających na front żołnierzy. Łuki te ustawione są w taki sposób, że aby przez nie przejść, trzeba podążać ścieżką łączącą pewne dwa sąsiadujące place o wspomnianej wyżej własności (tj. aby przejść przez łuk tryumfalny na placu tranzytowym A należy przyjść z sąsiedniego placu B i kierować się do innego sąsiedniego placu C takich, że każda ścieżka mięzy B i C prowadzi przez plac A).

Z uwagi na ich prestiżową rolę, parada musi przejść przez największą możliwą liczbę łuków tryumfalnych. Trasa nie może prowadzić przez żaden z placów więcej niż jeden raz. Z uwagi na nadchodzącą falę upałów, w trosce o zdrowie swoich żołnierzy, Król pragnie również by czas trwania uroczystości był jak najmniejszy, przy zachowaniu tych warunków.

## Dane wejściowe
Do zaimplementowanej funkcji przekazane zostaną następujące argumenty:

- N - ilość placów w Bitogrodzie
- lista zawierająca krotki postaci (a, b, t), gdzie a, b to numery placów, a t to czas potrzebny na przejście ulicą łączącą place a i b Place są indeksowane od 1, tj. mają indeksy 1, 2, …, N.

Przykładowe wywołanie może wyglądać następująco:
```python
solve(7, [
  (1, 2, 2),
  (2, 3, 3),
  (3, 4, 5),
  (4, 6, 1),
  (4, 5, 2),
  (4, 7, 3),
])
```
Funkcja solve powinna wyznaczać optymalną według opisanych wyżej kryteriów trasę, a następnie zwracać parę liczb - ilość łukótw tryumfalnych, przez które przejdzie parada, oraz całkowity czas jej trwania.

Dla powyższych danych place tranzytowe to 2, 3 i 4. Możliwe jest przejście przez wszystkie z nich, a najkrótsza możliwa droga to np. 1, 2, 3, 4, 6 o łącznym czasie 2 + 3 + 5 + 1 = 11 (aby przejść przez łuk tryumfalny, nie wystarczy wejść na jego plac - nie można zatem pominąć pierwszego i ostatniego placu powyższej trasy).

Można przyjąć, że grafy w zadaniu są spójne i zawierają co najmniej jeden plac tranzytowy.
