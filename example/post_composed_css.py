import requests 


# nb avec les meme variable en changeant juste le nom on peux deja faire pas mal de choses ...
url_prfx = "http://localhost:3000"
# filename = "((var>(if+var))+((var>for)+(var>for)))>if"
filename = "(attr+attr)>prop"
ext = "cssm"
api_path = f"/meta/{ext}/{filename}"

val0 = 'blue'
attr0 = 'background-color'
val1 = 'black'
attr1 = 'color'
prop0 = 'p'


# args = f"?ft0={fort}&fi0={fori}&li0={li0}&li1={o1}&op1={op}&ri1={o2}&ift1={f}&var0={var0}&val0={val0}&val1={val1}&var1={var1}&ift0={ift0}&val2={val2}&var2={var2}&ri0={ri0}&val3={val3}&var3={var3}&op0={op0}&ift2={ift2}&ri2={ri2}&li2={li2}&op2={op2}"
args = f"?val0={val0}&attr0={attr0}&prop0={prop0}&attr1={attr1}&val1={val1}"
address = f"{url_prfx}{api_path}{args}"

# print(address)
res = requests.get(address)
data = res.json()

if data["error_flag"] == True:
    print(data["message"])
    # print(data["message"],data["status"])
else :
    print(data["code"])