# DAY 7. 선형 독립과 선형 변환

### From Matrix Equation to Vector Equation

- A **matrix equation** can be converted into a **vector equation.**



### Span

- `def`
  - the set of linear combinations of v1, ... vp



### 행렬의 곱 => vectors의 linear combination

$$
\begin{bmatrix}
60 & 5.5 & 1\\
65 & 5.0 & 0\\
55 & 6.0 & 1
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
= 
Ax =
\begin{bmatrix}
a_1 & a_2 & a_3
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
= 
a_1x_1 +a_2x_2 + a_3x_3
$$

### Uniqueness of Solutino for Ax = b

- linear independence
  - {v1, .., vp} 의 원소 vp가 다른 놈들의 linear combination으로 표현되지 않음
  - <-> **linear dependent**



### Subspace

- subset of $\mathbb {R}^n$ s.t **linear combination**에 닫혀있다.
- Span {} always a subspace



### Basis of a Subspace

- 아래 2가지 조건을 만족하는 a set of vectors
  - Fully spans the given subspace H
  - Linearly independent (i.e no redundancy)



### Dimension of Subspace

- Subspace H를 던져 주면, basis는 H에 대해 유일하다.
- basis 개수 = dimension



### Column Space of Matrix A

- `def`
  - is the **subspace** spanned by the columns of A
  - $rand(A) \coloneqq dim(column ~ space)$



