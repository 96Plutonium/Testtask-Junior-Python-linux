import requests

def _get_data(link:str) -> dict:
    return requests.get(link).json()["packages"]

def _all_packages(arg:dict) -> list:
    ret = []
    for _ in arg:
        ret.append(_["name"])
    return ret
"""
Combines _get_data and _all_packages 
"""
def get_list(arg:str) -> list:
    link = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{arg}"
    return _all_packages( _get_data ( link ) )
