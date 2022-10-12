import requests
import string 

def _get_data(link:str) -> dict:
    return requests.get(link).json()["packages"]

def _all_packages(arg:dict) -> list:
    ret = []
    for _ in arg:
        ret.append(_["name"])
    return ret

def _arch_divide(arg:dict) -> list:
    """
    bugfix to make it separate data by architecture
    Also removes excess data
    """
    ret = []
    for _ in arg:
        ret.append({
            'arch' : _["arch"],
            'name' : _["name"],
            'version' : _["version"]
        })
    return ret

def _fromstring(arg:str) -> int:
    """
    creates an integer from version string
    example
    0.1b.123 -> 1123
    """
    blacklist = ["0", ".", "'", "_"] + [_ for _ in string.ascii_letters]
    for _ in blacklist:
        arg = arg.replace(_, '')
    if arg == '':
        return 0
    return int (arg)

def get_list(arg:str) -> list:
    """
    Combines _get_data and _all_packages
    """
    link = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{arg}"
    return _arch_divide ( _get_data(link) ) 

def substraction(arg:list, realtime = True) -> list:
    """
    Analogue to python's set substraction
    proceeding might take a bit long, so its made realtime by default
    NB that it analyses verions too
    """
    ret = []
    data = get_list(arg[1])
    for _ in get_list(arg[0]):
        if _ not in data:
            if realtime:
                print(_)
            else:
                ret.append(_)
    return ret

def check_versions(arg:list) -> dict:
    """
    Creates --versions functionality. Based on an idea of both arrays are sorted by default
    Checked: it works
    """
    ret = {}
    data1 = _arch_divide (get_list(arg[0]))
    data2 = _arch_divide (get_list(arg[1]))
    for _ in range(0, len(data2)):
        if _fromstring (data1[_]["version"]) > _fromstring (data2[_]["version"]):
            ret.update(data1[_])
    return ret
