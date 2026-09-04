# api

need to run that script at code_api dir level

## routes


### example 

get via curl then post via python3 allow to write a script into the api by editing the code (or giving the name of the code as argument)

### get /code/ext/file.ext

note : should remove .ext

ext example : py , css ...
file is the filename

useful example (get the post.py script) :
curl http://localhost:3000/code/py/post.py/raw >> post.py

### post /code/ext/file

python3 post.py <filename>


## commands/usage example 

1. get post.py file => use it to post the code => remove post.py from the directory : 

    curl http://localhost:3000/code/py/post.py/raw >> post.py && python3 post.py test && rm post.py 

2. get test_composed_string_css.py => use it to generate css and get it , then put it into a file .
then execute it and redirect result into style.css then post style.css  

curl http://localhost:3000/code/py/test_composed_string_css.py/raw > test_composed_css.py && python3 test_composed_css.py
curl http://localhost:3000/code/py/test_composed_string_css.py/raw > test_composed_css.py && python3 test_composed_css.py | python3

3. get create_dot_dir tool => then execute it (for now doesn't handle sub dir) then push it to the code api. 
the whole directory is then stored as a single file into the api. 

    1. curl http://localhost:3000/code/py/create_dot_dir.py/raw | python3 

    2. python3 post code_cli_api dir

4. post meta code into meta dir then use the component

<command missing for now>


## notes

also the doc with the cli is complementary to the one that should be there....

space bug re sub(##, "",...) => does not include /n ??!


work well with single line is buggy multiline !!! (attr+attr)>var .cssm

create_dot dir is not functionnal yet issue with recursion

