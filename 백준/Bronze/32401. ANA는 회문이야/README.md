# [Bronze II] ANA는 회문이야 - 32401 

[문제 링크](https://www.acmicpc.net/problem/32401) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2025년 5월 29일 17:32:24

### 문제 설명

<p>민용이는 ANA의 광신도라서 방학에도 하루 종일 동아리방에서 공부한다. 민용이가 ANA를 좋아하는 이유는 <span style="color:#e74c3c;"><code>ANA</code></span>라는 문자열이 회문이기 때문이다. 회문이란 앞에서부터 읽으나 뒤에서부터 읽으나 똑같은 문자열을 의미한다. 민용이는 <span style="color:#e74c3c;"><code>ANA</code></span>라는 문자열을 너무 좋아한 나머지 <strong>유사 ANA 문자열</strong>이라는 것을 다음과 같이 정의했다.</p>

<ul>
	<li><strong>유사 ANA 문자열</strong>은 영어 대문자로 이루어진 길이가 $3$ 이상인 문자열이다.</li>
	<li><strong>유사 ANA 문자열</strong>은 영어 대문자 <span style="color:#e74c3c;"><code>A</code></span>로 시작해서 <span style="color:#e74c3c;"><code>A</code></span>로 끝나며, 문자열의 다른 위치에서 <span style="color:#e74c3c;"><code>A</code></span>가 등장하지 않는다.</li>
	<li><strong>유사 ANA 문자열</strong>은 영어 대문자 <span style="color:#e74c3c;"><code>N</code></span>을 한 개만 포함한다.</li>
</ul>

<p>예를 들어 <span style="color:#e74c3c;"><code>ARENA</code></span>, <span style="color:#e74c3c;"><code>AGENDA</code></span>는 <strong>유사 ANA 문자열</strong>이다. 하지만 <span style="color:#e74c3c;"><code>ANACONDA</code></span>는 그렇지 않다. <span style="color:#e74c3c;"><code>A</code></span>를 세 개 포함하고 있고, <span style="color:#e74c3c;"><code>N</code></span>도 두 개 포함하고 있기 때문이다.</p>

<p>민용이는 어떤 문자열 $S$가 <strong>유사 ANA 문자열</strong>이 아닐 수도 있는 것에 슬퍼했다. 그래서 민용이는 $S$의 부분 문자열 중에서 <strong>유사 ANA 문자열</strong>을 찾으려고 한다. 문자열 $S$가 주어질 때, $S$의 부분 문자열 중에 <strong>유사 ANA 문자열</strong>이 몇 개인지 구해보자.</p>

### 입력 

 <p>첫째 줄에 문자열 $S$의 길이 $N(3\le N\le 100)$이 주어진다.</p>

<p>둘째 줄에 길이가 $N$인 문자열 $S$가 주어진다. $S$는 영어 대문자로 이루어져 있다.</p>

### 출력 

 <p>$S$의 부분 문자열 중 <strong>유사 ANA 문자열</strong>의 개수를 출력한다.</p>

