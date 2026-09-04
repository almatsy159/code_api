
import os

cwd = os.getcwd()
dirs = {os.getcwd():{}}


### {code_cli_api:{static:{css:{}},templates:{},tmp:{}}}

def get_dirs(path):
    lst_file = os.listdir(path)
    lst_dir = []

    for f in lst_file:
        if os.path.isdir(f"{path}/{f}"):
            lst_dir.append(f)
    return lst_dir


def get_all_dirs(path=None):
    if path == None:
        path = os.getcwd()
    # print(path)
    res = {}
    dirs = get_dirs(path)
    # print("dirs : ",dirs)
    for d in dirs:
        res[f"{path}/{d}"] = get_all_dirs(f"{path}/{d}")
    # print(res)
    return res



def get_lst_dirs(dirs):
    res = []
    for k,v in dirs.items():
        res.append(k)
        if v != {}:
            tmp = get_lst_dirs(v)
            res += tmp
    return res
        
# print(get_lst_dirs(get_all_dirs()))
        


            