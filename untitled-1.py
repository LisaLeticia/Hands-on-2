with open("ke_yi_raw.txt", "r", encoding = "utf-8") as f:
    List = f.readlines()
    #print(List)
    
    

import re
a = re.compile(r"more")
List1 = a.split(str(List))
print(List1)                        #先用more, more當關鍵字合併為一句string，做成新List
    
    
for i in range(len(List1)):

    if "可以" in List1:            #新List若有"可以"，則根據前後標點符號切出要的句子
     #   string = 
        
    
    
    #句子中不需要的(ex. \n, \t)刪掉
    
    #每句換行
    #寫出生成.txt
    
    
