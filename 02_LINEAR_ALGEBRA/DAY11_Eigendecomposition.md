# Day11. Eigendecomposition

## Eigenvectors, Eigenvalues

- Square matrix에서 따지는 개념
- def
  - $Ax = \lambda x$
  - x : eigenvector
  - $\lambda$ : eigenvalue
- 특성방정식으로 eigenvector, eigenvalue 찾을 수 있음



## 대수적 중복도, 기하적 중복도

- 두 개념 모두 '행렬 A에 대한 대수적 중복도' 이런개념이 아니라 **eigenvalue $\lambda$의 기하적 중복도** 이렇게 말하는 개념임
  - 대수적 중복도
    - 단순히 중근이 몇개 나오는지
  - 기하적 중복도
    - 주어진 $\lambda$에 대하여, $\lambda$가 만드는 선형독립 eigenvector들이 몇개인지.



## Null space

- def
  - Ax = 0 인 vector x들 다 모은거
- null space는 $\mathbb R^{n}$ **subspace**임.
- **rank(A) + nullity(A) = n**
  - n차원을 $A$랑 $A^c$ 가 노나먹는 느낌
- col(A)와 수직인 벡터들의 모임



## Diagonalization, Eigendecomposition

- $D = V^{-1}AV$ where $V$ : eigenvector로 만든 행렬
- Eigendecomposition : $A = VDV^{-1}$
- $\begin {bmatrix} 2 & 6 \\ 5 & 3 \end {bmatrix}$$\begin {bmatrix} 1 \\ 1 \end {bmatrix}$ = $8 \begin {bmatrix} 1 \\ 1 \end {bmatrix}$ 에서 $\begin {bmatrix} 1 \\ 1 \end {bmatrix}$ 은 eigenvector여서 계산상의 이득을 가져다준다고 하면, 그냥 임의의 벡터 $\begin {bmatrix} 3 \\ 4\end {bmatrix}$는 계산상의 이득을 못보는거 아닌가?
  - 그것을 eigendecomposition을 통해 이뤄낼 수 있다는 말
- $Ax = VDV^{-1}x$의 의미 (HW5 참조)
  - $y = V^{-1}x$ 
    - **Change of Basis {ev1, ev2}**
  - $x = 2v_1 + 1v_2$로 eigenvector들의 선형결합으로 표현해놓으면, 
  - $z=Dy$의 의미
    - **Element-wise Scaling**
  - $Vz$의 의미
    - **Back to Original Basis**



