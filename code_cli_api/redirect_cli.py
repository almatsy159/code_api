import sys
import requests


# usage : example 1 plante le pc ... why ?...

# example1 :
# python3 test_composed_string.py > tmp/file && python3 redirect_cli.py tmp/file


url_prfx = "http://localhost:3000"
filename = "last_recieved"
ext = "py"
api_path = f"/code/{ext}/{filename}"
address = f"{url_prfx}{api_path}"

if len(sys.argv)>1:
    data = None
    try :
        with open(sys.argv[1],"r") as f:
            data = f.read()
    except :
        raise FileNotFoundError
    
    if data:
        payload = {"code":data}
        res = requests.post(url=address,json=payload)
        print(res)


# code_to_send = input()

# print(code_to_send)