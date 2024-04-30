with open('ke_yi_raw.txt', 'r', encoding = "utf-8") as file:       #讀檔
    List = file.readlines()
    #print(List)


import re
a = re.compile(r'more')           #用more合併字串
List1 = a.split(str(List))      
#print (List1)


List2 = [s for s in List1]
to_remove = ["n","t","\\","[", "'", ",", " "]     #刪除多餘的文字
for i, s in enumerate(List1):
    for x in to_remove:
        List2[i] = List2[i].replace(x, "")
#print(List2)


text = str(List2)               # Define your string with punctuation
List3 = re.findall(r'\b\w+\b', text)             # Split the string using regular expression to exclude punctuation
#print(List3)


keyword = "可以"                        #若"可以"在字串中，保留字串形成新列表
new_list = []
for string in List3:
    if keyword in string:
        new_list.append(string)
#print(new_list)

with open("ke_yi_new_list.txt", 'w', encoding='utf-8') as file:
    for string in new_list:
        file.write(string +'\n')

print("檔案已保存到資料夾")