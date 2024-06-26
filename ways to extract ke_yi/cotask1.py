import re

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:        # read the text from the file
    raw = f.readlines()

def eliminate(s):
    pattern = re.compile(r'more')
    result = [pattern.sub('\n', x) for x in s]  #replace all the 'more' with \n
    return result

def split_sentence(s):
    p = eliminate(s)                      #input the text from eliminate(S)
    pattern = r'可以\t'                   #split the sentence with the pattern "可以"
    sentences = []                         #create an empty list
    for text in p:
        sentences.extend(re.split(pattern, text))       #extend the sentence to the splited text
    return sentences


sen = split_sentence(raw)             # split the sen. fron the function split_sentence()

with open("Yas.txt", "w", encoding="utf-8") as f:           #write into the new file'Yas'
    for i in sen:
        #f.write(i.strip() + "\n")



#Revised:



import re

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:
    raw = f.read()

def eliminate(raw):
    pattern = re.compile(r'more')
    return pattern.sub('\n', raw)


def split_sentences(raw_text):
    sentences = re.findall(r'(?:.*?可以.*?[。！？；])|(?:可以.*?[。！？；])', raw_text)
    return sentences

sentences = split_sentences(raw)

with open("Yas.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        f.write(sentence.strip() + '\n')  # Write each sentence into the file, followed by a newline character
