mathgen
=======

Work in progress (WIP). 

To-do: 

1. Put a title in the final pdf/png. sth like "X Y's academic genealogy"
1. Put a note in the final pdf/png which says "Generated from the Math Genealogy
project using <this-repo>"
1. Make the final output (pdf/png) so that it can be printed in a readible
format. Right now, the whole tree is fit into a single page, which makes the
fonts too small, unreadable. 

A simple Python script for crawling the Mathematics Genealogy Project:

http://genealogy.math.ndsu.nodak.edu/

Invoke it with an id of a mathematician as an argument and it will print out the complete genealogy tree of the desired mathematician.

Example: mathgen.py 108295

Output: Pierre-Simon Laplace (a student of Jean Le Rond d'Alembert)
