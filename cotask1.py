import re            #import the regular expression

with open("ke_yi_raw.txt", "r", encoding="utf-8") as f:
    S = f.readlines()

def eliminate(S):                           #create a function for eliminating 'more' and spliting the strings depending on the positions where 'more' used to stay at...
    a = re.compile(r'more')
    result = [a.sub('\t', x) for x in S]  #[] creates a new list for tha string eliminated all the "more"
    #sub() method in order to replace occurrences of the pattern specified in the regular expression with the replacement string
    return result

result = eliminate(S)
for x in result:
    print(x)
    
def find_words(S):            #create a finding all the '可以' functions for extracting from the string(S)
    b = re.compile(r'可以')
    rule = b.findall(str(S))
    return rule

rule = find_words(S)
print(rule)

# and then we're gonna save this as a txt. file... im out of ideas now...dunno wot to do:(
