# February 5th

## 33. Show that $n^2 + 50n = O(n^2)$

Assume:
$0 \leq n^2 + 50n \leq cn^2$

$= 0 \leq n^2(1+50/n) \leq cn^2$

$= 0 \leq 1+50/n \leq c$ (Divide by n^2)

$1+50/n$ is greatest when $n=1$, meaning $c=2$. Therefore:

$= 0 \leq 1+50/n \leq 2$

$0 \leq \frac{1}{n_0}(n_0+50) \leq 2$

$0 \leq n_0+50 \leq 2n_0$

$0 \leq 50 \leq n_0$

Hence, $0 \leq n^2 + 50n \leq cn^2 \ \forall\ n \geq n_0$ where $n_0=50,c=2$.

## 34. Show that $n^2+n^2+n^2 = 3n^2 = O(n^3)$

Assume:
$0 \leq 3n^2 \leq cn^3$

$= 0 \leq 3/n \leq c$ (Divide by n^3)

$3/n$ is greatest when $n=1$, meaning $c=3$. Therefore:

$= 0 \leq 3/n \leq 3$

$0 \leq 3 \leq 3n$

$0 \leq 1 \leq n$

Hence, $0 \leq 3n^2 \leq cn^3 \ \forall\ n \geq n_0$ where $n_0=1,c=2$.

## 35. Prove that $n^3 \neq O(n^2)$.

Assume:
$0 \leq n^3 \leq cn^2$

$= 0 \leq n \leq c$

This is not possible because $n$ is not bounded by a constant (would go to infinity). Therefore, $n^3 \neq O(n^2)$.

## Question 10 of Multiple Choice

10. The running time complexity of a linear time algorithm is given as

(b) $O(n)$
