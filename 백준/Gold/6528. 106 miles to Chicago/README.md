# [Gold IV] 106 miles to Chicago - 6528 

[문제 링크](https://www.acmicpc.net/problem/6528) 

### 성능 요약

메모리: 117672 KB, 시간: 264 ms

### 분류

데이크스트라, 그래프 이론

### 문제 설명

<p>In the movie "Blues Brothers", the orphanage where Elwood and Jake were raised may be sold to the Board of Education if they do not pay 5000 dollars in taxes at the Cook County Assessor's Office in Chicago. After playing a gig in the Palace Hotel ballroom to earn these 5000 dollars, they have to find a way to Chicago. However, this is not so easy as it sounds, since they are chased by the Police, a country band and a group of Nazis. Moreover, it is 106 miles to Chicago, it is dark and they are wearing sunglasses.</p>

<p>As they are on a mission from God, you should help them find the safest way to Chicago. In this problem, the safest way is considered to be the route which maximises the probability that they are not caught.</p>

### 입력 

 <p>The input file contains several test cases.</p>

<p>Each test case starts with two integers <em>n</em> and <em>m</em> (<em>2 ≤ n ≤ 100</em> , <em>1 ≤ m ≤ n*(n-1)/2</em>). <em>n</em> is the number of intersections, <em>m</em> is the number of streets to be considered.</p>

<p>The next <em>m</em> lines contain the description of the streets. Each street is described by a line containing 3 integers <em>a</em>, <em>b</em> and <em>p</em> (<em>1 ≤ a, b ≤ n</em> , <em>a ≠ b</em>, <em>1 ≤ p ≤ 100</em>): <em>a</em> and <em>b</em> are the two end points of the street and <em>p</em> is the probability in percent that the Blues Brothers will manage to use this street without being caught. Each street can be used in both directions. You may assume that there is at most one street between two end points.</p>

<p>The last test case is followed by a zero.</p>

### 출력 

 <p>For each test case, calculate the probability of the safest path from intersection <em>1</em> (the Palace Hotel) to intersection <em>n</em> (the Honorable Richard J. Daley Plaza in Chicago). You can assume that there is at least one path between intersection <em>1</em> and <em>n</em>.</p>

<p>Print the probability as a percentage with exactly 6 digits after the decimal point. The percentage value is considered correct if it differs by at most 10<sup>-6</sup> from the judge output. Adhere to the format shown below and print one line for each test case.</p>

