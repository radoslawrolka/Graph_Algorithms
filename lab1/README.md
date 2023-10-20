## Zadanie
Dany jest graf nieskierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t.
Szukamy scieżki z s do t takiej, że najmniejsza waga krawędzi na tej ścieżce jest jak największa.
Należy zwrócić najmniejszą wagę krawędzi na znalezionej ścieżce.
(W praktyce ścieżki szukamy tylko koncepcyjnie.)

## Podejścia algorytmiczne:

1. wykorzystanie struktury find-union,
2. wyszukiwanie binarne + przegląd grafu metodami BFS/DFS,
3. algorytm a’la Dijkstra.
