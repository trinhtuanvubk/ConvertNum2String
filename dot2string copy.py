import re 
import unicodedata

# normalize text data 
def norm_text(text):
    return unicodedata.normalize('NFC', text)

#  replace "." by "chấm"
def one_dot_replace(string:str):
    num = re.split('\.',string)
    return num[0] + " chấm " + num[1]

#  remove multiple '.' or ','
def multi_dot_removal(string:str):
    num = re.split('\.|\,',string)
    return ''.join(num)

def dot2string(paragraph:str):
    text = norm_text(paragraph)
    text = text.lower()
    # remove space 
    text = re.sub('\s{2,}', ' ', text)
    #  + one or limited, * zero or limited, [] list of char, {} times, 
    # dot_re2 = r"([0-9]+[\.|\,]{1}[0-9]+[0-9\.|\,]+)" # regex for multiple '.' 
    dot_re2 = r"([0-9]+[\.|\,]{1}[0-9]+[\,|\.0-9]+)"
    dot_re1 = r"([\s][0-9]+[.]{1}[0-9]+[\s])" # regex for one '.'

    # dot_tokens2 = re.findall(dot_re2,text)
    dot_tokens1 = re.findall(dot_re1,text)
    # print(dot_tokens1)
    for token in dot_tokens1:
        new_token = one_dot_replace(token)
        text = text.replace(token, new_token)

    dot_tokens2 = re.findall(dot_re2,text)
    # print(dot_tokens2)
    if len(dot_tokens2)>0:
        for token in dot_tokens2:
            new_token = multi_dot_removal(token)
            text = text.replace(token, new_token)
    
    return text 


if __name__=='__main__':
    ex = 'hôm nay là 40.5 độ C.   Có số tiền là 345,322,000 và 1.000.000'
    text = dot2string(ex)
    print(text)