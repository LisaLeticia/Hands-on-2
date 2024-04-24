import re

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:
    S = f.readlines()

def eliminate(S):
    a = re.compile(r'more')
    result = [a.sub('\t', x) for x in S]  #[] creates a new list for tha string eliminated all the "more"
    #sub() method of a compiled regular expression to replace occurrences of the pattern specified in the regular expression with the replacement string
    return result

result = eliminate(S)
for x in result:
    print(x)
    
def find_words(S):
    b = re.compile(r'可以')
    rule = b.findall(str(S))
    return rule

rule = find_words(S)
print(rule)
