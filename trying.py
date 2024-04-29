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
print(new_list)                                   #得到的新清單

import re
def extract_sentences_without_punctuation(text, keyword):
    # 定义标点符号，用于分割和清除
    punctuation_pattern = r'[，。？！,.?!。，；：、．]'
    
    # 使用标点符号分割文本为句子
    sentences = re.split(punctuation_pattern, text)
    
    # 过滤出包含关键字的句子
    keyword_sentences = [sentence for sentence in sentences if keyword in sentence]
    
    # 清除句子中的所有标点符号
    cleaned_sentences = [re.sub(punctuation_pattern, '', sentence) for sentence in keyword_sentences]
    
    return cleaned_sentences

# 示例文本和关键字
text = new_list
keyword = "可以"

# 使用函数提取含关键字的句子
extracted_sentences = extract_sentences_without_punctuation(text, keyword)
print(extracted_sentences)



#def extract_with_punctuation(sentences, keyword):
    #'''
    #input => 
    #output => 
    #'''
    #punctuation = r'[。，；：、．]'                 #定義標點符號
    #results = []
    
    #for sentence in sentences:
        #for match in re.finditer(keyword, sentence):
            #start_index = match.start()
            #end_index = match.end()
            
            ##向前找到第一個標點符號
            #pre_sub = sentence[:start_index]
            #pre_matches = list(re.finditer(punctuation, pre_sub))
            #start = pre_matches[0].end() if pre_matches else 0
            
            #post_sub = sentence[end_index:]
            #post_match = re.search(punctuation, post_sub)
            #end = end_index + post_match.start() if post_match else len(sentence)
            
            #results.append(sentences[start:end])
    
    #return results


#sentences = new_list
#keyword = "可以"
#extracted_parts = extract_with_punctuation(sentences, keyword)
#print(extracted_parts)


    
    #每句換行
    #寫出生成.txt
    
    