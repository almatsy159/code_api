from flask import Flask,render_template,url_for,jsonify,request
import os
import re

app = Flask(__name__)
cur_dir = cd =  os.getcwd()

ext_dir = {"doc":f"{cd}/docs","html":f"{cd}/templates","css":f"{cd}/static/css",
           "md":f"{cd}/mds","py":f"{cd}/prog/python","ts":f"{cd}/prog/typescript",
           "txt":f"{cd}/docs/txt","data":f"{cd}/data","tmp":f"{cd}/tmp","pym":f"{cd}/meta","sh":f"{cd}/prog/shell"}
meta_dir = f"{cd}/meta"

@app.route("/")
def home():

    # htmls = os.listdir("./templates")
    # data = {}
    # for i,file in enumerate(htmls):
    #     name = re.match(r"(.*)\.html",file)
    #     if name :
    #         data[i] = {}
    #         for ext,dir in ext_dir.items():
    #             url = f"{dir}/{name[1]}.{ext}"
    #             data[i][ext] = url
    
    prog_dirs = os.listdir(f"{cd}/prog")
    data = {}
    data["progs"] = {}
    
    for pl in prog_dirs:
        progs = os.listdir(f"{cd}/prog/{pl}")
        data[pl] = progs
        doc = ""
        doc_available = False
        for p in progs:
            path= f"{cd}/mds/{pl}/{p.split('.')[0]}.md"
            # print(os.path.exists(path))
            if os.path.exists(path):
               doc_available = True
            else:
                doc_available = False
                doc = "No doc for this file"
            data["progs"][p] = {"doc":doc,"pl":pl,"doc_available":doc_available,"link":f"{cd}/prog/{pl}/{p}","ext":p.split('.')[1],"name":p.split('.')[0]}

    return render_template("home.html",data=data)

@app.route("/md/<string:ext>/<string:file>")
def get_doc_file(ext,file):
    return render_template("doc.html",name=f"{file}.{ext}")
    return ""

# curl http://localhost:3000/py/test.py/raw 
@app.route("/code/<string:ext>/<string:file>/raw",methods=["GET"])
def get_code_component_raw(file,ext):
    res = ""
    error = False
    try :

        with open(f"{ext_dir[ext]}/{file}") as f:
            res = f.read()
        print("res : ",res)
    except Exception as e :
        print(e)
        res = f"{e}"
        error = True
        
        
    print(res)
    return res


@app.route("/code/<string:ext>/<string:file>",methods=["GET"])
def get_code_component(file,ext):
    res = ""
    message = ""
    status = 200
    error_flag = False
    try :

        with open(f"{ext_dir[ext]}/{ext}/{file}.{ext}") as f:
            res = f.read()
        print("res : ",res)
    except Exception as e :
        print(e)
        message = f"{e}"
        status = 400
        error_flag = True
        
    print(res)
    return jsonify({"code":res,"message":message,"error_flag":error_flag,"status":status})


def write_css(data):
    to_write = ""
    print("data : ",data)

    for name,dic in data.items():
        to_write += f".{name}" + "{\n"
        for prop,args in dic.items():
            to_write += f"\t{prop}:{args};\n"
        to_write += "}\n\n"
    return to_write
            
    

@app.route("/code/<string:ext>/<string:file>",methods=["POST"])
def post_code_component(file,ext):
    
    # need to track change within this function
    flag_error = False
    error = ""
    to_write = ""
    status = 200
    
    if ext in ext_dir.keys():
        data = request.get_json()
        if ext == "css":
            to_write = write_css(data)
        elif ext == "py":
            if "code" in data.keys():
                
                # to_write += f"#writing date : {datetime.datetime.ctime}"
                to_write += data["code"]
                print(to_write)
            else :
                status = 400
                flag_error = True
                error = "expect a code key in json data"
                print("error : ",error)
        elif ext == "ts":
                    if "code" in data.keys():
                        
                        # to_write += f"#writing date : {datetime.datetime.ctime}"
                        to_write += data["code"]
                        print(to_write)
                    else :
                        status = 400
                        flag_error = True
                        error = "expect a code key in json data"
                        print("error : ",error)
        elif ext == "txt":
                    if "code" in data.keys():
                        
                        # to_write += f"#writing date : {datetime.datetime.ctime}"
                        to_write += data["code"]
                        print(to_write)
                    else :
                        status = 400
                        flag_error = True
                        error = "expect a code key in json data"
                        print("error : ",error)
        elif ext == "sh":
                    if "code" in data.keys():
                        
                        # to_write += f"#writing date : {datetime.datetime.ctime}"
                        to_write += data["code"]
                        print(to_write)
                    else :
                        status = 400
                        flag_error = True
                        error = "expect a code key in json data"
                        print("error : ",error)
        else :
            status = 400
            flag_error =True
            error = "extension not handled but mapped in ext dir"
            print(error)


        with open(f"{ext_dir[ext]}/{file}.{ext}","w") as f:
            print(f"writing in {ext_dir[ext]} as {file}.{ext}")
            # print(data)
            f.write(to_write)
    else :
        error = "extension is not writable"
        flag_error = True
        status = 400
        print("error : ",error)
    
    return jsonify({"status":status,"flag_error":flag_error,"error":error})



class ComposedMetaFile:
    symbols = ["+",">","(",")"]
    def __init__(self,my_str,ext,meta_dir=None):
        self.my_str = my_str
        self.ext = ext
        if meta_dir != None:
            self.meta_dir = meta_dir
        else :
            self.meta_dir = f"meta/{ext}"
        self.names = []
        self.dict_id_name = {}

        self.content = ""
        self.expected_var = {}


    def get_args_from_meta(self,file):
        expected_var = {}
        res = re.findall(r"## (\d*)_(.*) : (.*) : (.*)",self.content)
        for var in res:
            print("var : ",var)

            expected_var[var[0]] = {"name":var[1],"type":var[2],"desc":var[3],"idx":var[0]}
        self.expected_var = expected_var
        
    
    def get_list_args(self):
        lst_arg = []
        res = re.findall(r"## (\d*)_(.*) : (.*) : (.*)",self.content)
        # print("res : ",res)
        for var in res:
            print("var : ",var)
            if var[1] not in lst_arg:
                lst_arg.append(var[1])
        return lst_arg



def get_pos_operator(my_str):
    symbol = [">","+","(",")"]
    map_pos = {}
 
    for s in symbol:
        map_pos[s] = []
        for i,c in enumerate(my_str):
            if s == c:
                map_pos[s].append(i)
    return map_pos

def define_order_parenthesis(map_pos):
    # global ?
    # symbol = [">","+","(",")"]
    
    lst_entry_parenthesis = map_pos["("]
    lst_end_parenthesis = map_pos[")"]
    entry_end_dict = {}
    
    # get pos of corresponding entry/close parenthesis
    lst_entry_parenthesis.reverse()
    for idx,i in enumerate(lst_entry_parenthesis):
        cpt = 0
        while lst_end_parenthesis[cpt] < i:
            cpt+=1
        entry_end_dict[i] = lst_end_parenthesis[cpt]
        lst_end_parenthesis.pop(cpt)
        
    cpt =0
    
    return entry_end_dict

def split(my_str):

    files = my_str.split(">")
    final_files = []
    for file in files :
        f = file.split("+")
        final_files += f

    files_count = {}
    for f in final_files :
        if f not in files_count.keys():
            files_count[f] = 1
        else :
            files_count[f] += 1

    return final_files

def get_file_content(final_files,ext):
    current_count = {}
    file_content = {}
    
    # read each files from the string
    for f in final_files:
        with open(f"{meta_dir}/{ext}/{f}.{ext}","r") as tf:
            tmp_file = tf.read()
        if f not in current_count.keys():
            current_count[f] = 1
        else :
            current_count[f] += 1
        file_content[(f,current_count[f])] = tmp_file
    return file_content
        

def parse_meta(expected_var,content):

    print("expected var :",expected_var)
    file = content
    file = re.sub(r"##.*","",file)
    file = file.strip()

    for idx,dic in expected_var.items():

        all_occurence_of_var =re.findall(f"{expected_var[idx]['idx']}_{expected_var[idx]['name']}",file)

        for i in range(len(all_occurence_of_var)):
            match_occurence = re.search(f"{expected_var[idx]['idx']}_{expected_var[idx]['name']}",file)
            if match_occurence:
                file = file[0:match_occurence.span()[0]] + f"{expected_var[idx]['name']}{i}"  + file[match_occurence.span()[1]:]
    parsed_content = file.strip()

    return parsed_content 
    

def parse_code(dict_args,meta,lst_arg):

    key_error = None

    for arg in lst_arg:
        cpt = 0
        for m in re.findall(f"{arg}",meta):
            try : 
                print(f"replacing {arg}{cpt} by {dict_args[f'{arg}{cpt}']}")
                meta = re.sub(f"{arg}{cpt}",dict_args[f'{arg}{cpt}'],meta)
                
            except :
                key_error = f"{arg}{cpt}"
            cpt +=1

    return meta,key_error
        
    

def get_operators(my_str):
    symbol = [">","+","(",")"]
    operators = []

    for s in symbol:
        for i,c in enumerate(my_str):
            if s == c:
                operators.append(s)
    return operators

def treatment_str(my_str,cpt,ext):   
     
    map_pos = get_pos_operator(my_str)
    entry_end_dict = define_order_parenthesis(map_pos)

    for k,v in entry_end_dict.items():
        tmp = my_str[k+1:v]
        final_files = split(tmp)
        file_content = get_file_content(final_files,ext)
        pos_operator = get_operators(tmp)
        
        bloc = handle_operator(file_content,pos_operator,final_files,ext)
        with open(f"meta/{ext}/bloc_{cpt}.{ext}","w") as f:
            f.write(bloc)
        my_str = my_str[0:k] + f"bloc_{cpt}" + my_str[v+1:]
        
        return my_str
    

def handle_operator(files_content,pos_operator,final_files,ext):
    # can remove with open and replace it by string storage !
    res = ""
    for i,tpl in enumerate(files_content.keys()):
        tmp = ""
        if i != 0:
            file_content2 = files_content[tpl]
            if pos_operator[i-1] == ">":
                with open(f"tmp/res","r") as f:
                    file_content1 = f.readlines()

                tmp = insert_content_f1_into_f2(file_content1,file_content2)

            elif pos_operator[i-1] =="+":
                with open(f"tmp/res","r") as f:
                    file_content1 = f.read()

  
                tmp = concat_content(file_content1,file_content2)

        else :

            tmp = files_content[tpl]
        with open("tmp/res","w") as f:
                f.write(tmp)

        res = tmp
    return res



def insert_content_f1_into_f2(file1:list,file2:str):
    matches = re.search(r"( *)(\$1_.*)",file2)
    res = file2
    if matches:

        for i,l in enumerate(file1):
            if i == 0:
                res = re.sub(r"\$1_.*",l,file2)
            else :
                res+= f"{matches.groups()[0]}{l}"
    return res

def concat_content(file1,file2):

    return file1 + "\n" + file2 + "\n"

@app.route("/meta/<string:ext>/<string:files>")
def meta_code3_object(ext,files):
    code = ""
    error_flag = False
    message = ""
    status = 200
    
    
    my_str = files
    cpt = 0
    # extract the biggest parenthesis bloc
    res = re.match(r".*\(.*\).*",files)

    if res:
        while res is not None:
            my_str= treatment_str(my_str,cpt,ext)
            if isinstance(my_str,str):
                res = re.match(r".*\(.*\).*",my_str)
            else : 
                print("else shouldn't occur")
                res = None
            cpt +=1    
            
            
    cmf = ComposedMetaFile(my_str,ext)
    final_files = split(my_str)
    print(final_files)
    pos_operator = get_operators(my_str)
    files_content = get_file_content(final_files,ext)
    
    concatenated_file = handle_operator(files_content,pos_operator,final_files,ext)
    cmf.content = concatenated_file
    
    print("concatenated file : \n",concatenated_file)
    cmf.get_args_from_meta(concatenated_file)
    dict_args = dict(request.args)
    print("dict args : ",dict_args)
    

    lst_arg = cmf.get_list_args()
    meta = parse_meta(cmf.expected_var,cmf.content)
    print('meta :\n',meta)
    
    code,key_error = parse_code(dict_args,meta,lst_arg)
    
    if key_error :
        print("key error : ",key_error)
        error_flag = True
        message = f"key error : {key_error}"
        status = 400
        return jsonify({"error_flag":error_flag,"code":"","status":status,"message":message})
    
    print("code : ",code)
    

    return jsonify({"error_flag":error_flag,"code":code,"status":status,"message":message})


if __name__ == "__main__" :
    app.run(host="localhost",port=3000)