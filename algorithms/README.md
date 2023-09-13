## Quine McCluskey method
- method to find minimum solution using minterm expansion input
- In Quine-McCluskey method, the minterms are represented in binary notation.
Then the binary minterms are sorted into groups which are divided along the numbers of ‘1’ for each group.
Then the prime implicants are determined. To minimize the function, which is in sum of prime implicants, prime implicant chart is introduced.
There could be multiple minimum SOP(Sum Of Products) solutions.
Otherwise, we can implement Petrick’s method, which is to assume P as the multiplication of each column in the prime implication chart and then multiplying out each term by ordinary distributive law, and then eliminating the redundant terms from P.
- 5 steps created to solve the method
  1. recieve input of minterm expression
  2. convert inputs into binary number
  3. determine the prime implicants
  4. determine prime implicant chart
  5. determine minimum solution using Petrick's method
  * step 4 and step 5 not done
