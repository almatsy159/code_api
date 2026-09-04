import requests
import os
import sys

# exec the code recieved from the api :

# usage : python3 exec_cli | python3

# could be replaced by curl

# to improve the api you should be able to get the list of available component !
# can't exec a whole dir !!!

component = "create_dot_dir"
ext = "py"

url_prfx = "http://localhost:3000"
api_path = f"/code/{ext}/{component}.{ext}"
address = f"{url_prfx}{api_path}"

res = requests.get(address)

# print(res)
data = res.json()

if not data["error"]:
    print(data["code"])