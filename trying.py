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



def filter_sentences_with_keyword_in_list(text_list, keyword):
    '''
    '''
    punctuation = ['。', '，', '？', '！', ',', '.', '?', '!', '（', '）', '、', '：', '「', '」', '；']   #定義標點符號用於分割list中每個字串的句子
    
    # 初始化结果列表
    filtered_text_list = []
    
    # 遍历列表中的每个字符串
    for text in text_list:
        # 初始化当前句子
        current_sentence = ''
        # 初始化当前句子列表
        keyword_sentences = []
        
        # 遍历字符串中的每个字符
        for char in text:
            # 如果当前字符是标点符号，则将当前句子添加到句子列表中并重置当前句子
            if char in punctuation:
                if keyword in current_sentence:
                    keyword_sentences.append(current_sentence)
                current_sentence = ''
            # 否则将字符添加到当前句子中
            else:
                current_sentence += char
        
        # 检查最后一个句子
        if keyword in current_sentence:
            keyword_sentences.append(current_sentence)
        
        # 组合过滤后的句子为新的字符串，并加入结果列表
        filtered_text = ''.join(keyword_sentences)
        filtered_text_list.append(filtered_text)
    
    # 将列表中的每个元素以换行的形式呈现
    result = '\n• '.join(filtered_text_list)
    return result

# 示例文本列表和关键字
text_list = new_list
keyword = "可以"

# 使用函数保留含关键字的句子，并以换行的形式呈现
filtered_text = filter_sentences_with_keyword_in_list(text_list, keyword)

# 将结果写入文本文件
file_path = "filtered_text_ke_yi.txt"

with open(file_path, 'w', encoding='utf-8') as file:
    file.write('\n• ' + filtered_text)

print("文本已保存到文件:", file_path)