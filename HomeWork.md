Mathematica HomeWork (#
30 GB A¥-F1~30)

m@ 1. Basic Calculations
Read the Mathematica as a Calculator section of the
Tour of Mathematica and then attempt the following
exercises. If it is not already open, you may find the
Basic Input palette helpful. For more information on
palettes see Using Palettes.

§ 1.1.1 Getting Started
You can use Mathematica as an enhanced scientific
calculator. Let's start with a simple example.

45 +78

123
The first line here is what you type in. The second line is

the result.

1. Use the Basic Input palette to type in the
expression 3! below this cell. Hit together
to evaluate this expression. Note that you should get

the exact answer. [1 Mark)

A, You can position the cursor anywhere on the line for
expression evaluation to work. Alternatively you can
select the cell-bracket (or a range of cell brackets) that
contains an expression (s) and select Evaluate Cells
under the Kernel/Evaluation menu.

2. Select your input line above (either by selecting its

Computational Biophysics
2 HomeWork.nb

cell bracket or by scrolling over the expression with
the mouse clicked) and make a copy using Copy

under the Edit menu. Paste your expression below
this box. Change the 100 to 1000 and evaluate the

result.(1 mark)

You should have just evaluated 310.

An easy way to select an expression is to click on it as
many times as is necessary to select the entire expression
(this is a type of scoping).

3. To get the result in the form you might get on a
calculator, try N[%]. [1 Mar)

A. % indicates the previous expression. Similarly %%
indicates the second-last expression and % n refers to
Out[n]. Alternatively, expressions can be named using
assignment (denoted using =).

4. Enter pi = N[z, 200] below this cell and evaluate
it. [1 Mark}

You should get the value of z to two hundred decimal
places.

5. Enter e > below this cell and evaluate it. What

is special about this number? [2 Marks)

Answer:

6. z has a run of six consecutive 9's in the first 1000
digits. Can you see where they are located? (One way
to find the location is to convert the number to a

Computational Biophysics
HomeWork.nb

string [using ToString], drop the leading 3. [using
StringDrop] and locating the position of the string
"999999" [using StringPosition]). (3 Marks)

Answer:

Mf 1.1.2 More Functions
Mathematica knows about a big collection of
mathematical functions — nearly all those you will find
in any book of mathematical tables.

7. Compute sin(13 x), log(2.1), and e’” by copying

these expressions below this cell and entering them.)
Marks]

A, Note that e denotes the exponential e and i denotes y-1.
You can these objects using the Basic Input palette.

8. Lookup cos in the on-line help and determine
closed-form expressions for cos(%). (2 Marks!

Answer:
Mathematica can do many kinds of exact computations
with integers.

9. Evaluate FactorInteger[70 612 139 395 722 186].
What is the meaning of this output? (2 Marks)

ANSWET:  Factorinteger produces a set of pairs of numbers which are

10. Recombine the numbers in the above output to
show how they form 70 612 139 395 722 186. (2 Marks)

Computational Biophysics
4 HomeWork.nb

§ 1.1.3 Simple Expressions
Mathematica can deal with mathematical formulas in
algebraic form.

11. Enter the expression (x? + 2.x + 1). Expand this
expression using Expand[%]. Factor the expanded

result.(3 Marks]

12. Re-do the steps in the above computation using
the Basic Calculations palette. (3 Marks)

13. Evaluate

TrigReduce[sin(x) cos(y) - cos(x) sin(y)] and apply
TrigExpand to the result. What can you say about
the relationship between these functions? (2 marks]

Answer:

Hf 1.1.4 Basic Plots
The above sections have guided you through each
calculation. Now you are expected to use palettes such
as the Basic Calculations palette or on-line help to work
out how to achieve each of the following tasks.

14. Produce a plot of sin(x”) over x € [0, 5]. 1 mag

15. Produce a phase-space plot of cos(x) versus
sin(3 x) for over x € [0, 2 2]. Hint: lookup

ParametricPlot. Do you recognise this figure? (2 marks)
Answer:

16. Produce a contour plot and density plot of xe”

Computational Biophysics
HomeWork.nb

for-l <x<land-1l <y<1. pars)

@ 1.1.5 Calculus
You can do calculus. Try a simple integral:

17. Compute f 7 dx. Check by differentiating the
resulting expression with respect to x and then using
Simplify. (3 marks)

You can also get exact solutions to many definite
integrals.

00 cip2 3
18. Compute f sine) cos") AX. [1 Mark]

Many integrals do not have a simple closed form. If you
try such a definite integral it will be returned
unevaluated. You can still use N to get a numerical
answer.

19. Try f sin(sin(x)) dx. Compute the numerical
value of this expression using N[%]. (2 Marks)

A, Note that Mathematica can find a closed form for
iM sin(sin(x)) dx. Try it.
§ 1.1.6 Solving Equations

20. Use Solve to obtain the roots of the quadratic
equation ax? + bx +c == 0, and call the set of
solutions s. Check the solutions by back-substitution
using the syntax ax’? +bx+ce/.s. You will need to
Simplify the result. (3 marks)

Computational Biophysics
6 HomeWork.nb

A Note that == denotes equality, not assignment (which is

=),

21. Solve the cubic equation x? - x + 1 == 0. Evaluate
this expression numerically using N. Does your
answer satisfy the requirement that roots of equations
with real coefficients must come in conjugate pairs
(a conjugate pair is a set of two numbers of the form
a+ bi)? [3 Marks)

Answer:
@ 1.1.7 Matrices

= Entering matrices
Matrices can be entered using List brackets ({}).
Alternatively, they can be entered using the Basic Input
palette or from the Create Table /Matrix/Palette...
entry under the Input menu.

22. In anew cell, enter the 2 x 2 matrix,
3.5 7.2

-2.4 6.4
eigenvalues of ma: — you should be able to guess the

names of the appropriate Mathematica commands. 2
Marks]

mat = ( ). Compute the inverse and

= Linear algebra
Mathematica also does linear algebra on symbolic
matrices.

abe
23. Entermat=(d e f ). This overwrites your
ghi

Computational Biophysics
HomeWork.nb

previous value for the matrix mat. Compute the
inverse of mat and assign (using =) the result to
minv. Compute minv.mat and simplify the result. (3
Marks]

A The. (i.e., Dot) in a.b indicates that the usual dot product
and is used both for vectors and matrices. This makes
sense because each element in the resulting matrix is
formed by dot product multiplication of rows of a with
columns of b. Without the Dot one gets the direct (Z.e.,
element-by-element) product. The direct product is
useful for general matrix operations such as masking and
convolution.

24. Generate a random real 3 x 3 matrix and call it
rand (Hint: use Random and Table). Replace the

{2, 2} entry of rand with the symbolic parameter x
(Hint: look-up Part). Compute the (symbolic)
inverse of rand and determine the numerical value of
the inverse when x > 1. [4 Marks}

® 1.1.8 Curve Fitting

25. Use the command Table[i!, {i, 1, 10}] to
compute the first 10 values of the factorial function

and assign the answer to the variable called is. (2 marks)

We could plot this table but the dynamic range is so large
that it would be difficult to produce a meaningful plot.
Let us take the logarithm of these values.

26. Take the log of values using log(is) and

Computational Biophysics
HomeWork.nb

numerically evaluate the result. Save this result as a
named variable called data.ji mark)

Now that we have a table of values we can plot it using
the ListPlot command.

27. Use ListPlot to plot data and save your graphic
as a named variable called, e.g., py. (1 Mark)

28. Compute the best (least-squares) third-order

polynomial fit to this data using Fit. Obtain a plot of
this fit and call it pz. You need to choose and
appropriate range for the Plot command (see
PlotRange). Show p; and p2 superimposed using

Show. [3 marks]

A, You can, in fact, do fits using any linear combination of
functions but Fit presently does not allow exponent
optimization — you need to use the
Statistics NonlinearFit~ package for this.

29. Plot animations of 2 D Curve and 3 D Surface.

30. Processing an image.

Computational Biophysics
