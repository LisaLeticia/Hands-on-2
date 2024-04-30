import re

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:     #read in file to raw_data
    raw_data = f.read()
    
input_str = re.sub("\n|more|\t", '', raw_data)       #remove \n, \t, and "more"

pattern = re.compile(r'\w*可以\w*')        #compile search pattern
matches = pattern.findall(input_str)        #output list: matches

with open("ke_yi_processed.txt", "w") as f:     #write matches into txt file named "ke_yi_processed.txt"
    for i in matches: 
        print(i, file=f)