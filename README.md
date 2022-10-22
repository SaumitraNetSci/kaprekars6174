# KAPREKAR'S 6174

## PROBLEM

In 1949, [D. R. Kaprekar](https://en.wikipedia.org/wiki/D._R._Kaprekar) discovered a procedure, now known as the [Kaprekar routine](https://en.wikipedia.org/wiki/Kaprekar%27s_routine), which quickly takes a 4-decimal-digit number (which has at least two distinct digits) to the number 6174 in at most 7 steps of his procedure. Applying this procedure to 6174 produces 6174. Numbers of the form dddd all go to 0 in one step. 

One step of the [Kaprekar routine](https://en.wikipedia.org/wiki/Kaprekar%27s_routine) goes this way: Choose any positive $k$-digit integer $n_1$ . If $n_1$ has fewer than $k$ digits, then take the leading digits to be 0 (i.e, consider 0s padded to $n_1$ where they don’t matter). Two integers ${n'}_1$ and ${n''}_1$ can be formed out of the $k$ digits of $n_1$; namely, by sorting the digits in ascending and descending orders. To get the next number $n_2$ in this sequence, take the difference of ${n'}_1$ and ${n''}_1$. That is, 

$n_2 = max({n'}_1, {n"}_1) − min({n'}_1, {n''}_1)$.

Now apply the same routine to $n_2$ to get $n_3$, and so on. Any positive integer base other than 10 can also be used.

A variant of the routine omits the zero-padding step above. Depending on $k$ and $b$, the two variants may show different behaviours.
