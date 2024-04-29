with open("ke_yi_raw.txt", "r", encoding = "utf-8") as f:    #讀檔
    List = f.readlines()
    List = List[1:]                      #刪除第一個字串，避免後面合併錯誤
    #print(List)    


import re
a = re.compile(r"more")
List = a.split(str(List))          #先用more, more當關鍵字合併為一句string，做成新List
#print(List)                        


keywords = ["'", "\\", ",", "t", "[", "n", " "]     #刪除影響合併的冗詞
str_list = List
new_list = []
for string in str_list:
    for keyword in keywords:
        string = string.replace(keyword, "")
    new_list.append(string)
new_list = [s for s in new_list if s.strip()]     #過濾空字串
#print(new_list)                                   #得到的新清單


def extract_with_punctuation(sentences, keyword):
    '''
    input => sentences: the list that you want to split.
             keyword: the word as reference point to find where the beginning and the end marks of the split string are.
                      Here, the beginning mark will be the punctuation mark before keyword "可以", and the end mark will be the one after keyword.
    output => 
    '''
    pattern = r'[。，；：、．]'                 #定義標點符號
    start_match = re.search(pattern, text[:text.find(keyword)])    #從keyword前的標點符號為起始點
    end_match = re.search(pattern, text[text.find(keyword):])      #到keyword後的標點符號為終點
    
    if start_match:
        start_index = start_match.end()      #起始點為標點符號後一個位置
    else:
        start_index = 0       #如果沒有找到標點符號，則起始點為0
        
    if end_match:
        end_index = text.find(end_match.group(), text.find(keyword))    #終點為下一個標點符號位置
        if end_index == -1:
            end_index = len(text)
    else:
        end_index = len(text)   #如果沒有找到終點標準符號，則終點為string結尾
    
    return text[start_index:end_index]

#split_string(str(new_list), "可以")      #呼叫函式

print(str(new_list))
        


    
    #每句換行
    #寫出生成.txt
    
    