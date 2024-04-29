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
    punctuation = r'[。，；：、．]'                 #定義標點符號
    results = []
    
    for sentence in sentences:
        start_index = sentence.find(keyword)
        if start_index != -1:       #從關鍵字位置向前搜索標點符號
            pre_sub = sentence[:start_index]
            pre_match = re.search(punctuation + r'[^' + punctuation + r']$', pre_sub)
            if pre_match:
                start = pre_match.start() + 1
            else:
                start = 0     #如果沒有找到標點符號，則從句子開始處提取
            
            post_sub = sentence[start_index + len(keyword):]
            post_match = re.search(punctuation, post_sub)
            if post_match:
                end = start_index + len(keyword) + post_match.end()
            else:
                end = len(sentence)
                
            
            results.append(sentence[start:end])
    return results


sentences = new_list
keyword = "可以"
extracted_sentences = extract_with_punctuation(sentences, keyword)
print(extracted_sentences)


    
    #每句換行
    #寫出生成.txt
    
    