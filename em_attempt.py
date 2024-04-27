import re

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:     #reading in the file and saving to raw_data
    raw_data = f.read()
    
list1 = re.sub("\n|more|\t", '', str(raw_data))     #removing \n, \t, and "more"

pattern = re.compile(r'\w*可以\w*')       #output pattern
matches = pattern.finditer(list1)
#output_list = []        #initializing output_list

for i in matches:       #filling output_list with matched lists
    #output_list.append(i.group(0))
    with open("ke_yi_processed.txt", "a") as f:     #writing the output_list into a txt file named "ke_yi_processed.txt"
        print(i.group(0), file=f)
    