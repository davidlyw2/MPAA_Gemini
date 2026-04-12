# doc_string 의 """ 아랫줄과 """ 윗줄 사이에는 빈공간이 있으면 안된다.
doc_string = """
		테마명,tmname,tmname,char,36;
		평균등락율,avgdiff,avgdiff,float,6.2;
		테마코드,tmcode,tmcode,char,4;
"""

item = list()
item2 = list()
data  = doc_string.split('\n')[1:-1]
for idx in range(len(data)):
    res = data[idx].split(',')
    item.append(res[1].replace('\t', '').replace(' ', '').replace(';', ''))    
    item2.append(res[0].replace('\t', '').replace(' ', '').replace(';', ''))

print(item)    
print(item2)