import re

with open('ke_yi_raw.txt', 'r', encoding = "utf-8") as file:       #讀檔
    inputLI = file.readlines()
    #print(inputLI)


more = re.compile(r'more')           #用more合併字串
combineLI = more.split(str(inputLI))      
#print (combineLI)


cleanedLI = [s for s in combineLI]
to_remove = ["n","t","\\","[", "'", ",", " "]     #刪除多餘的文字
for i, s in enumerate(combineLI):
    for x in to_remove:
        cleanedLI[i] = cleanedLI[i].replace(x, "")
#print(cleanedLI)


text = str(cleanedLI)               
nopuncLI = re.findall(r'\b\w+\b', text)      # 以\b(或說以標點符號為分隔但不要標點符號)分割每個字串中的句子，使其成為更小、以單句為單位的字串列表
#print(nopuncLI)


keyword = "可以"                        #若"可以"在字串中，保留字串形成新列表
new_list = []
for string in nopuncLI:
    if keyword in string:
        new_list.append(string)
#print(new_list)


new_list = set(new_list)     #將list轉成set避免句子被重複


with open("ke_yi_new_list.txt", 'w', encoding='utf-8') as file:
    for string in new_list:
        file.write(string +'\n')

print("檔案已保存到資料夾")