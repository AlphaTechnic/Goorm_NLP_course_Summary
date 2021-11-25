# Day9. Least Squares (2)

 ## Least square

- $A^TA$가 not invertible하면 어떻게 될 것인가?
  - b의 수선의 발은 무적권 유일하게 하나로 결정이 됨
  - 그럼에도 불구하고 $A^TA$가 not invertible인 경우가 있다.
    - $columns~of~A$가 linearly dependant하다는 얘기
    - 이는 $\hat b$를 결정하는 x가 무수히 많다는 얘기
    - 그러나 sample이 줫네 많고, 하면 각 column이 linearly dependant할 가능성은 거의 없어지게 된다.



## Orthogonal projection on col(A)

- $\hat b = f(b) = A \hat x = A(A^T A)^{-1}A^Tb = Cb$
  - where $A(A^T A)^{-1}A^T = C$
- orthogonal projection 또한 linear transformation의 형태이다.
- b를 col(A)에 projection을 원한다?? => vector에 C를 곱하면 끝이라는 얘기
- 이걸 굉장히 쉽게 구하기에, Gram-Schmit orthogonalization이 가능해짐



## Gram-Schmit orthogonalization

- span{col(A)} = span{col(U)}인 orthonormal basis를 가지는 U가 존재한다.
- 이를 바꿔주는 방법이 Gram-Schmit
- 꽤 간단한 알고리즘 과정이다. (normalization 생략)
  - v2 => {v1}에 수선의 발 v2' => v2 - v2' 해서 {u1}에 수직인 방향 구함 => u2 구함
  - v3 => {v1, v2}에 수선의 발 v3' => v3 - v3' 해서 {u1, u2}에 수직인 방향 구함 => u3 구함
  - (반복)

## QR factorization

- 결국 A라는 linear transformation을 A = QR로 인수분해 하는 것이 가능한 셈이다.
  - where Q는 orthnormal basis