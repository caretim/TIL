# [Gold III] Restauracje - 8561 

[문제 링크](https://www.acmicpc.net/problem/8561) 

### 성능 요약

메모리: 120592 KB, 시간: 300 ms

### 분류

데이크스트라, 그래프 이론

### 문제 설명

<p>Bajdonald postanowił uruchomić w Bajtocji sieć restauracji. Jego pragnieniem jest, żeby każdy mieszkaniec mógł choćby raz w tygodniu wybrać się do jednej z nich.</p>

<p>Wstępnie zaplanował już, w których miastach postawi swoje restauracje. Obawia się jednak, czy z każdego miasta będzie można w rozsądnym czasie dojechać do jakiejkolwiek z nich. Chciałby więc dowiedzieć się, jaką największą odległość trzeba pokonać, żeby dostać się do najbliższej restauracji. Jeśli ta odległość okaże się zbyt duża, będzie musiał zmienić swoje plany.</p>

<p>Miasta w Bajtocji są połączone siecią dwukierunkowych autostrad. Wiadomo, że z każdego miasta można dojechać do każdego innego, choć nie zawsze bezpośrednio. Mieszkańcy Bajtocji żyją tylko w miastach.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia mapę kraju oraz planowane miejsca budowy restauracji,</li>
	<li>wyznaczy maksymalną odległość jaką należy pokonać z pewnego miasta do najbliższej restauracji (to znaczy, spośród wszystkich odległości pomiędzy miastami a najbliższymi restauracjami, należy znaleźć tę największą),</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się trzy liczby całkowite <em>n</em>, <em>k</em> i <em>m</em>, 1 ≤ <em>n</em>, <em>k</em> ≤ 1 000, 1 ≤ <em>m</em> ≤ 30 000, oddzielone pojedynczymi odstępami, określające odpowiednio - liczbę miast w Bajtocji, liczbę planowanych restauracji oraz liczbę autostrad. Miasta są ponumerowane od 1 do <em>n</em>.</p>

<p>W każdym z kolejnych <em>k</em> wierszy znajduje się jedna liczba - numer miasta, w którym ma być zbudowana restauracja. W każdym z następnych <em>m</em> wierszy znajdują się trzy liczby całkowite <em>a</em>, <em>b</em> i <em>d</em>, oddzielone pojedynczymi odstępami. Liczby te opisują jedną autostradę - autostrada łączy miasta <em>a</em> i <em>b</em> (<em>a</em> ≠ <em>b</em>), a jej długość wynosi <em>d</em> km, 1 ≤ <em>d</em> ≤ 1 000.</p>

### 출력 

 <p>W jedynym wierszu standardowego wyjścia powinna zostać zapisana jedna liczba całkowita, równa maksymalnej odlegości (w kilometrach) pomiędzy pewnym miastem, a najbliżej położoną restauracją.</p>

