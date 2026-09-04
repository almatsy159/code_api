import requests

# post a file recevied as : /code/{ext}/{file_to_post}.{ext} => writed in /{ext}/file_to_post.{ext} 
url_prfx = "http://localhost:3000"
filename = "style"
ext = "css"
api_path = f"/code/static/{ext}/{filename}"
address = f"{url_prfx}{api_path}"

payload = {"classname":{"background":"blue"},"classname2":{"display":"flex"}}

res = requests.post(url=address,json=payload)
print(res)