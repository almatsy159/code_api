# code api


# notes


let go .dir for now....

this project is the client for code api that need to be running 

*note :* what i think is beautiful about this project is you can get the cli code via curl and use it directly so you don't need other installation than python (example) and curl to run the script... 

need to recode handle file treatment in code_cli.api  it is closely related to create dot_dir
handle creation of existing files and .dir reliquat
static is buggy because there is only dir within it...
templates is buggy don't know why but the name need fix (handle file logic)

this project would need a huge cleanup and refacto ...

should be completed with a bash , if the api is running at launch the tool can then be used everywhere if the bash is in bin.

## writer_cli.py

is used to create file (css,html) within a project from a service (example flask) that provide the code directly.

example :

    create the test_component.html file at templates dir from test_component.html of the service

    '''bash
    python3 writer_cli.py html test_component templates test_component
    '''

    create the test_component.css file at static/css dir from test_component.css of the service

    '''bash
    python3 writer_cli.py css test_component static/css style
    '''

## test_code_post.py

is used to post a file

'''python

import requests
url_prfx = "http://localhost:3000"
api_path = "/code/css/test_write"
address = f"{url_prfx}{api_path}"

payload = {"classname":{"background":"red"},"classname2":{"display":"flex"}}

requests.post(url=address,json=payload)

'''

## post_dot_dir.py /!\ not implemented dot.dir yet

is used to send specifically a .dir file generated with the create dot dir but is similar to test_code_post.py 

## exec_cli.py 

can be easily replace by a curl and probably should (so it doesn't need external program to run !)
exec_cli.py | python3

## create_dot_dir.py /!\ not implemented dot.dir yet

pretty messy/buggy but synthetise a directory into one single file and can then be send directly to the api (or could be used in another project to check delta within dirs (which project ?))


## test_composed_string.py

handle parenthesis , > (injection) and + (concatenation) of code

### example of usage 

generate code and execute it locally : python3 test_composed_string.py | python3
generate code and write it : python3 test_composed_string.py > file_to_write
send the generated code to the api : test_post.py

## redirect_cli.py 

can be usefull but seem qiet dangerous/buggy ...

## api-cli.py

simple flask api that run on the client side to test the imported code may have some other usages ...

