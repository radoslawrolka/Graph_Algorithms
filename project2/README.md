# Treść zadania
Książe Bitkacy nie szczędzi czasu i zawartości królewskiego skarbca na swoją pasję - archeologię. Tym razem niemałym kosztem udało mu się wejść w posiadanie ekscytującego znaleziska.

W ręce księcia trafił papirus stanowiący relację z ostatnich dni życia Al-Gorima, rabusia grobowców ze starożytnego orientalnego państwa Grafaara. Al-Gorim postanowił zbadać miejsce spoczynku wysokiej rangi oficjela. Grafaarskie grobowce zorganizowane były jako zestaw komnat połączonych korytarzami, z jednym wejściem. Ze względów religijnych, od wejścia do każdej komnaty prowadziła dokładnie jedna droga. W pewnym momencie eksploracji Al-Gorim stracił poczucie orientacji, i postanowił od tej pory oznaczać swoją drogę, a także sporządzać notatki opisujące trasę, którą się przemieszcza. Za każdym razem, gdy wchodził w nowy, niezbadany jeszcze korytarz, zapisywał na papirusie znak +. Gdy szedł korytarzem, który już wcześnej przeszedł w kierunku przeciwnym do pierwszego przejścia (tj. gdy się nim cofał), oznaczał to jako ^. Gdy natomiast ponownie wkraczał w zbadany już korytarz w kierunku zgodnym z pierwszym przejściem, zapisywał liczbę oznaczającą ile innych korytarzy wychodzących z danej komnaty zbadał, zanim pierwszy raz wszedł do tego. Niestety, ostatnie zapiski sugerują, że mimo starannych notatek nie udało się znaleźć wyjścia z grobowca, nim zabrakło sił i zapasów wody.

Książe Bitkacy zapragnął odnaleźć miejsce wiecznego spoczynku Al-Gorima i podążając jego śladami zwiedzić opisany w papirusie grobowiec. Problem w tym, że na przestrzeni kilku tysiącleci, pod piaskami pustyń Grafaary tego typu grobowców powstało wiele. Dzięki pracy archeologów i nowoczesnym technikom obrazowania, dysponujemy dokładnymi informacjami dotyczącymi rozkładu pomieszczeń we wszystkich odnalezionych grobowcach. Twoim zadaniem jest odpowiedzieć na pytanie, które z nich dopuszczają trasę opisaną w papirusie.

## Dane wejściowe
Do zaimplementowanej funkcji przekazane zostaną następujące argumenty:

- N - ilość komnat w grobowcu
- numer komnaty zawierającej wyjście na zewnątrz
- lista korytarzy, zawierająca krotki postaci (a, b), gdzie a, b to numery komnat
- string zawierający oddzielone pojedynczymi spacjami notatki opisujące drogę

Komnaty są indeksowane od 1, tj. mają indeksy 1, 2, …, N.
