import json


def get_requests_data(string_):
    #get_requests_data(string_=string_)
    #string_ = 
    '''
    i:"Top 10 College Dropouts."
    from:AUTO
    to:AUTO
    smartresult:dict
    client:fanyideskweb
    salt:15583685094363
    sign:6c267d0607194b4212bf38a5e254c848
    ts:1558368509436
    bv:d84d0ff898edfe1cca9937df34d371cd
    doctype:json
    version:2.1
    keyfrom:fanyi.web
    action:FY_BY_CLICKBUTTION
    '''
    '''
    {
        "i": "\"Top 10 College Dropouts.\"",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15583685094363",
        "sign": "6c267d0607194b4212bf38a5e254c848",
        "ts": "1558368509436",
        "bv": "d84d0ff898edfe1cca9937df34d371cd",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    } 
    '''
    dicts = {}
    for i in string_.split('\n'):
        if i == '':
            pass
        else:
            n = i.index(':')
            key = i[0:n]
            value = i[n+1:None]
            dic = {key:value}
            dicts.update(dic)
    json_dicts_formated_string = json.dumps(dicts,indent=4)
    print(json_dicts_formated_string)
    return dicts





string_ = '''

i:"Top 10 College Dropouts."
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:15583685094363
sign:6c267d0607194b4212bf38a5e254c848
ts:1558368509436
bv:d84d0ff898edfe1cca9937df34d371cd
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_CLICKBUTTION

'''
get_requests_data(string_)
