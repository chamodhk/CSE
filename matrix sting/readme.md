Develop a Python program that takes a string S and an integer N as input from a file and outputs S after transforming it into a matrix form based on N. The string S and N are such that, 1≤ len(S) ≤ 1000 and 1 ≤ N ≤ 1000. S contains only English characters and N represents the number of rows in the matrix. You must define and use at least one function in your code.


String transformation:

Given the string S and N, read the characters in S left-to-right one-by-one to fill a matrix with N rows. Fill the matrix column-wise, top-to-bottom, starting with the leftmost column and continuing to fill other columns left-to-right until all characters are used. If the string S does not perfectly fit into the matrix, fill the remaining elements of the last column with the character '*' to make a complete matrix. Once the matrix is created, read the characters row-wise, left-to-right, starting from the top row and continuing downward, to produce the final transformed string that will be output.


Example: Suppose, S= “THISISAMATRIX” and N= 3; then the matrix would be:



Then reading this matrix row-wise will produce the transformed string "TSATXHIMR*ISAI*" which will be the output.

Input:
The input file will contain a single line with:

String S (1 ≤ len(S) ≤ 1000) consisting of English characters.

Integer N (1 ≤ N ≤ 1000), the number of rows in the matrix.

Output:

The final transformed string.


Example 1:

Input (from file P68_input_1.txt):

HELLOTHERE 3

For this, the matrix would look like:




Output: HLHEEOE*LTR*


Explanation: S=HELLOTHERE and N=3.

So let's start with the character H and then until it reaches 3 rows we should add characters to column 1 of the matrix as follows.
H
E
L

After reaching the last row of column 1, we continue to fill the next column.
H L
E O
L T

We continue until we finish our letters in S.
H L H E
E O E
L T R

Now all the characters are added to the matrix but it is an incomplete matrix; so we fill the remaining elements with ‘*’.

H L H E
E O E *
L T R *

Next we read this matrix row-wise to produce the transformed string “HLHEEOE*LTR*”.


Example 2:

Input(from file P68_input_2.txt):

EXAMPLESINPUT 4

For this input the matrix would look like



Output: EPITXLN*AEP*MSU*
Answer:(penalty regime: 0 %)
