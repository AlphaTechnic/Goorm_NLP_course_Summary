# DAY 8. Least Squares (1)

## Linear Transformation

- Ax = b
  - 함수 역할로서 A를 생각해 본다는 관점
- **Linear Transformation** 
  - T(cu + dv) = cT(u) + dT(v)를 만족하는 Transformation
- 유용한 Trick
  - x -> 2x + 1
    - $\mathbb R^1$ ->$\mathbb R^1$ 으로 보면 linear가 아님
  - $\begin{bmatrix}
    1\\
    x\\
    \end{bmatrix}
    ->
    \begin{bmatrix}
    1 & 2\\
    \end{bmatrix}
    \begin{bmatrix}
    1 \\
    x \\
    \end{bmatrix}$
    - $\mathbb R^2$ ->$\mathbb R^1$으로 보면 linear가 됨
    - 이런식으로 선형 모델로 처리 가능



## Onto, 1-1

- Ex1 ) T(x) = Ax = $\begin{bmatrix}
  60 & 5.5 & 1\\
  65 & 5.0 & 0\\
  55 & 6.0 & 1
  \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$
  - Is T 1:1 ?
  - Does T $\mathbb R^2$ onto $\mathbb R^3$ ? 
  - Yes / No
- Ex2 ) T(x) = Ax = $\begin{bmatrix}
  1 & 4 & 5\\
  2 & 3 & 6\\
  \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\x_3 \end{bmatrix}$
  - Is T 1:1 ?
  - Does T $\mathbb R^3$ onto $\mathbb R^2$ ? 
  - No / Yes



## Over-determined Linear Transformation

- 표본이 100개여서 $\mathbb R^3$ -> $\mathbb R^{100}$ 매핑을 해야된다면,
  - 3차원이 100차원을 다 못 덮기 때문에, 해가 없을 가능성 농후하다.
  - 이 때, x를 어떻게 근사해줄 것인가?
  - => SSE가 least인 방향으로 해준다.
- $\hat x = arg~min_x ||b-Ax||$
  - b : 찐 n차원
  - Ax : n차원 안에서 2차원 같은 느낌. 공간에 떠있는 평면같은 느낌



## Least Square의 기하학적인 해석

- col(A)를 구성하는 vector모두 (b - Ax)와 수직이어야 함
- 즉, $A^T \dotproduct (b - A \hat x) = 0$

### Normal equation

- $A^TA \hat x= A^T b $
  - $\hat x = (A^TA)^{-1}A^Tb$
- $\hat x = arg~min_x ||b-Ax||$ = $arg~min_x ||b-Ax||^2$  = $arg~min_x (b-Ax)^T \dotproduct (b-Ax)$ 
  - 위 식을 전개하고 미분 = 0 인 식을 유도해도 위와 같은 normal equation이 유도됨
  - 이 때, transpose와 미분에 대한 아래와 같은 성질만 알고 있으면 됨
    - $a^Tb$ 
      - 미분 시 : $a$
    - $x^Ta$
      - 미분 시 : $a$
    - $x^TAx$
      - 미분 시 : $(A + A^T)x$

