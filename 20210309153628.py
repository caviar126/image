import json

python_data = [
{'姓名': '张三', '年龄': '22', '住址': '广州', '职业': '程序员'},
{'姓名': '李四', '年龄': '23', '住址': '宁波', '职业': '工程师'},
{'姓名': '王二', '年龄': '25', '住址': '杭州', '职业': '工程师'},
{'姓名': '麻子', '年龄': '21', '住址': '', '职业': '教师'},
]


string_data = """[{'姓名': '张三', '年龄': '22', '住址': '广州', '职业': '程序员'}, {'姓名': '李四', '年龄': '23', '住址': '宁波', '职业': '工程师'}, {'姓名': '王二', '年龄': '25', '住址': '杭州', '职业': '工程师'}, {'姓名': '麻子', '年龄': '21', '住址': '', '职业': '教师'}]"""



#### 将转python_data写入.json文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(python_data, f, sort_keys=True, indent=4, ensure_ascii=False)

#### 读取'data.json'为python_data
with open('data.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f) # list


#### 将python_data转为string_formated
string_formated_1 = json.dumps(python_data, sort_keys=True, indent=4, ensure_ascii=False)
#print(string_formated_1)



string_data = '''"[{'住址': '广州', '姓名': '张三', '年龄': '22', '职业': '程序员'}, {'住址': '宁波', '姓名': '李四', '年龄': '23', '职业': '工程师'}, {'住址': '杭州', '姓名': '王二', '年龄': '25', '职业': '工程师'}, {'住址': '', '姓名': '麻子', '年龄': '21', '职业': '教师'}]"'''
string_formated_2 = json.loads(string_data)


print(type(string_formated_2))
#rint(string_formated_2)

"""
# json.dumps();  ensure_ascii=False, 转为非ascii编码(即转为指定编码字符串)
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dumps(string_formated, ensure_ascii=False)

"""




# 
# json.dumps();  ensure_ascii=False, 转为非ascii编码(即转为指定编码字符串)

# json.load() 将包含json格式数据的文件对象读取并识别为python_data，返回json类型
# json.loads() 将string转为python_data，返回json类型

# json.load()
#with open('data.json', 'r', encoding='utf-8') as f:
 #   python_data_ = json.load(f)
#print(type(python_data_))
    #json.loads()
#python_data_ = json.loads(string)



