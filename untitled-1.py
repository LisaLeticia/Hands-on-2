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


#for i in range(len(List)):

#i = 1
#while i < len(List):
#    if "可以" in List[i]:       #若"可以"在句中，與前一字串合併
#        List[i-1] += List[i]
#        del List[i]
#    else:
#        del List[i]
#print(List)
        
        
        #新List若有"可以"，則根據前後標點符號切出要的句子
         
        
    
    
    #句子中不需要的(ex. \n, \t)刪掉
    
    #每句換行
    #寫出生成.txt
    
    