# documentation of meta file

## save a meta bloc of code

as <filename>.<ext>m

ex : <filename>.pym stand for .py(meta)

## handle injection 

the syntax to put inside a meta code for injection is  : $1_XXX  ($2_ not tested but shouldn't work)

## handle replacement

put inside meta code "## " ( /!\ with 'space character') followed by the unique (for all files) identifier following the example.

example : ## 6_m : string : description

regex used : <here look for the regex into code_api5>

*note* : 
1. type is not handled but must be present (to match the regex) 

then add '6_m ' where it should be used. followed by a space (because \n is not yet handled properly)
if adding a number should finish with an underscore (should be avoided not tested)

example : 

'''pym
import 6_m 
'''









