# 선형 대수
1. 선형이란 어떤 함수의 임의로 두 개 값 x1, x2에 대해서 a(x1 + x2) = ax1 + ax2가 성립하면, 즉 x1, x2을 더한 후, 함수 연산을 한 것과, x1, x2 각각 함수 연산 후, 더한 것이 같으면 선형이다 (linear하다)라고 표현한다. 선형 함수는 x1, x2의 값을 알았을 때, x1 + x2의 값을 예측할 수 있어 계산에 용이하여 선형 함수에 대해서 공부하는 것이다. 하지만 선형 함수도 어렵다.

## 배울 내용
1. 벡터 스페이스
2. 선형 함수(사상, mapping): 하나의 벡터 스페이스를 다른 벡터 스페이스로 옮겨 주는 함수 (행렬이라고 함)
3. 연립 방정식: 1, 2를 이용하여 연립 방정식을 풀이함.
4. 대각화 특성다항식
5. 내적
6. 분해 정리 (Jordan Canonical Form)

## 1강 벡터 스페이스
1. 벡터 스페이스는 벡터들이 모여 있는 공간을 의미한다.
2. 벡터는 길이(크기)가 있고 방향이 있는 화살표이다. 
3. 위치, 속도, 가속도 힘등을 벡터로 표현할 수 있다.
4. 벡터를 원점에서부터 끝점으로 가는 위치를 표시하는 화살표로 생각하고 이야기 진행하겠다.
5. 벡터의 뎃셈 (A + B = B + A = C)
- 위치가 벡터 A에서 벡터 B는 벡터 A의 끝점에서 시작해서 이동하여 벡터 C의 위치에 갔다면, A + B = C로 표현할 수 있다. (벡터의 뎃셈): A에서 B로 경유하였으나, 결론적으로 벡터 C의 위치에 있음.
- 벡터 A와 벡터 B의 원점이 같다면 평행사변형의 원리를 이용해 덧셈을 할 수 있으며, 이를 통해 뎃셈은 벡터 A와 벡터 B의 순서와 상관 없음을 알 수 있다.
6. 벡터의 상수배(스칼라 곱): 길이 조정하거나 방향 바꾸기
- 3A = A + A + A 이다.
- 0 * A = 0 (영벡터이다.영벡터는 방향이 없다.)
7. 벡터는 좌표계 위에 기하학적으로 표현이 가능하며, 각 성분으로 분해할 수 있으며, 덧셈과 상수곱이 성립함을 증명할 수 있다. A = (Ax, Ay)
7. 벡터는 어떤 좌표계를 사용하느냐에 따라 (Ax, Ay) (A'x, A'y)등 여러 개의 좌표계로 표현할 수 있다. 마치 같은 대상을 가지고 다른 언어로 말하면 번역기가 필요한 것처럼 이 두 벡터도 변환이라는 것이 필요하다.
8. 벡터를 계산하기 위해서 같은 좌표계에서 처리되어야 한다.
9. 벡터 스페이스V는 무수히 많은 원소(벡터)를 가지고 있는 집합이다. 벡터는 소문자, 벡터 스페이스는 대문자로 표현한다. 벡터 스페이스는 뎃셈의 4가지 성질과 상수곱의 4가지 성질이 존재한다. 
뎃셈
- (v + u) + w = v + (u + w) - 결합 법칙
- v + u = u + v - 교환 법칙
- 0이 V에 존재한다면(E거꾸로) s.t(such that) 모든 v에 대해서(A거꾸로) 0 + v = v + 0 (영벡터) - (항등원)
- 모든 v에 대해서 -v가 존재한다면, v + (-v) = 0 가 된다. (역원)
상수곱
- (ab)v = a(bv)
- (a + b)v = av + bv (분배 법칙)
- a(w + v) = aw + av (분배 법칙)
- 1v = v
10. 상수는 Q(유리수), R(실수), C(허수)와 같이 덧셈, 뺄셈, 곱셈, 나눔셈이 모두 가능한 Field(체)여야 한다.
11. 벡터 스페이스도 집합이므로 부분집합을 가질 수 있는데, 이 부분집합이 벡터 스페이스가 되려면, 아래를 만족하여야 한다. W가 V의 sub space가 되려면...
- W의 w1, w2가 있다면 w1 + w2 가 W의 원소인가?
- w가 W의 원소라면, cw도 W의 원소인가?