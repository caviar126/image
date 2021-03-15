import json, glob


datas = glob.glob(r'信息字典\\*.json')

Data_List = []


f_mp4 = open('mp4.txt', 'w', encoding='utf-8')
f_img = open('img.txt', 'w', encoding='utf-8')


for data_file in datas:
    #### 读取data.json文件为python_data
    with open(data_file, 'r', encoding='utf-8') as f:
        dict_data = json.load(f) # list
    #print(dict_data)


    for key_mp4 in dict_data:
        key = key_mp4.split('/')[-1].split('.')[0]
        Data_List.append(key)
        f_mp4.write(key_mp4+'\n')
        f_img.write(dict_data[key_mp4][2]+'\n')

f_mp4.close()
f_img.close()


#### 将python_data写入data.json文件
with open('data_所有视频.json', 'w', encoding='utf-8') as f:
    json.dump(Data_List, f, sort_keys=True, indent=4, ensure_ascii=False)







"""#### 读取data.json文件为python_data
with open('data.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f) # list


"""