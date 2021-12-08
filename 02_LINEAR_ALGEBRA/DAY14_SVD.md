# DAY14. SVD

- A = $U \Sigma V^T$  (SVD)
  - SVD는 어떠한 행렬 A를 가져와도 항상 할 수 있는 decomposition이다.
  - where V는 $A^TA$의 eigenvectors
- A = $PDP^{-1}$ (eigen decomposition)
  - A는 정사각행렬이어야만 함



- A가 r개의 nonzero singular values를 갖는다고 하자.
  - => {$Av_1, Av_2, .., Av_r$} is an **orthogonal** basis for **col(A)** and rank(A) = r
  - singular value = $\sqrt \lambda$
  - $A^TA$라는 특별한 행렬의 nonzero eigenvalue의 개수를 구하면, col(A)의 dimension을 구할 수가 있다는 얘기





