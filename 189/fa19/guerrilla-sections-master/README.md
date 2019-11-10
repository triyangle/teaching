# Guerrilla Section Repository

This repository's primary purpose is to make document generation easier for course staff.

Created by [Alvin Wan](http://alvinwan.com) and [Sinho Chewi](http://chewisinho.github.io)

Modified by [Soroush Nasiriany](http://snasiriany.me)

# Installation

Clone the repository and change into the directory.

```
git clone https://github.com/BerkeleyML/guerrilla-sections.git
cd guerrilla-sections
```

## Creating Documents

We now support a workflow which produces the `.tex` files from templates. The templates are located at `src/gs/template.tex` and `src/gs/template-sol.tex`. In order to make the actual documents, the only documents you need to edit are: a base `.base.tex` file containing the input problems, and the `.tex` files for the problems themselves.

Here, we will create a new document of the form `gs[num]`.

First, navigate to `src/gs/`, and make a file called `gs0.base.tex`.

```
cd src/gs
touch gs0.base.tex
```

Open up `gs0.base.tex` using a text editor of your choice. Here is an example:

```
\input{modulararithmetic/text/introduction.tex}
\input{modulararithmetic/divisible-or-not.tex}
```

This file should only contain a list of `\input{...}`, each on its own line, referencing a problem or a text blurb. Browse through problems in `src/problems/`, and add problems above.

## Adding Questions

The file starts with the command `\Question`. You are free to include whatever you want afterwards, and the solution should be wrapped in the `solution` environment. Example:

```
\Question{Compute This}


\begin{Parts}


\Part
Suppose you had a program A…
\begin{solution}
The program A can indeed be computed by...
\end{solution}

\Part
Suppose you had a program B…
\begin{solution}
The program B can indeed be computed by...
\end{solution}


\end{Parts}

\newpage
```

## Rendering Document

First, navigate to the root directory of this repo. In other words `pwd` should end with `/materials`.

Then, to render an assignment, use `make gs n=[number]`.

For example, to make gs worksheet 1, use

```
make gs n=1
```

This will create two PDF files:

- `rendered/GS0/GS0.pdf`
- `rendered/GS0/GS0-sol.pdf`

## Generating Image Files

After running `make gs n=[number]` as above, the command `make img n=[number]` will generate PNG image files, also in the `rendered` directory. To use this feature, you must have ImageMagick installed (see the requirements above).
