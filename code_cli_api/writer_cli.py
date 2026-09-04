# import subprocess
import requests
import os
import sys


# write file inside dir as filename from test_component.css file 
component = "test_component"
ext = "css"
dir = "static/css"
filename = "style"

# arg not handled gracefully ...
if len(sys.argv)>4:
    ext = sys.argv[1]
    component = sys.argv[2]
    dir = sys.argv[3]
    filename = sys.argv[4]
elif len(sys.argv) == 1 :
    print("default setting")
else :
    print("this code need 4 args : extension , component to get , output dir and output file")
    raise NotImplementedError

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def handle_dir(path):
    dir_list = path.split("/")
    print(dir_list)
    for i in range(len(dir_list)):
        if i>0:
            create_dir("/".join(dir_list[0:i+1]))
        else:
            create_dir(dir_list[i])

handle_dir(dir)

url_prfx = "http://localhost:3000"
api_path = f"/code/{ext}/{component}.{ext}"
address = f"{url_prfx}{api_path}"

# subprocess.run(["curl",address])
res = requests.get(address)
# print(res.__dict__)
data = res.json()

print(data["error"])
print(data["code"])


if not data["error"]:
    with open(f"{dir}/{filename}.{ext}","w") as f:
        f.write(data["code"])
        


