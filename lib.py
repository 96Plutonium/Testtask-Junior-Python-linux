import requests
import string 

def _get_data(link:str) -> dict:
    return requests.get(link).json()["packages"]

def _all_packages(arg:dict) -> list:
    ret = []
    for _ in arg:
        ret.append(_["name"])
    return ret
"""
bugfix to make it divide data by architecture 
"""
def _arch_divide(arg:dict) -> list:
    ret = []
    for _ in arg:
        ret.append({
            'arch' : _["arch"],
            'name' : _["name"],
            'version' : _["version"]
        })
    return ret

"""
creates an integer from version string
example
0.1.123 -> 1123
"""
def _fromstring(arg:str) -> int:
    blacklist = ["0", ".", "'", "_"] + [_ for _ in string.ascii_letters]
    for _ in blacklist:
        arg = arg.replace(_, '')
    if arg == '':
        return 0
    return int (arg)
"""
Combines _get_data and _all_packages 
"""
def get_list(arg:str) -> list:
    link = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{arg}"
    return _arch_divide ( _get_data(link) ) 

"""
proceeding might take a bit long, so i made it realtime
"""
def substraction(b1:str, b2:str, realtime = True) -> list:
    ret = []
    data = get_list(b2)
    for _ in get_list(b1):
        if _ not in data:
            if realtime:
                print(_)
            else:
                ret.append(_)
    return ret

def check_versions(b1:str, b2:str) -> dict:
    ret = {}
    data1 = _arch_divide (get_list(b1))
    data2 = _arch_divide (get_list(b2))
    for _ in range(0, len(data2)):
        if _fromstring (data1[_]["version"]) > _fromstring (data2[_]["version"]):
            ret.update(data1[_])
    return ret
