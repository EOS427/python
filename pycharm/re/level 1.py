import random
import re
text="身高182，体重100，学号3202，密码123456,1234567"
text2="1351-445664,1343431651651,15436546-46468465,212-45"
text3="13456789101,18846579211,123"

# print(re.findall(r'123456',text))
# print(re.findall(r'\d',text))
# print(re.findall(r'\D',text))
# print(re.findall(r'\W',text))
# print(re.findall(r'[1-5]',text))
# print(re.findall(r'\d{1,4}',text))
# print(re.findall(r'\d{3}-\d{6}',text2))
# print(re.findall(r'\d{3}-\d{6}|d{13}',text2))
# print(re.findall(r'd{3,4}-\d{2,6}',text2))
# print(re.findall(r'188\d{8}',text3))
# print(re.findall(r'\d{8}101',text3))

# def generate_phone_num():
#     first='1'
#     second=str(random.randint(3,8))
#     third=''.join(random.choices("1234567890",k=9))
#     return first+second+third
#
# text_list=[generate_phone_num() for i in range(10000)]
# result_list=[re.findall(r'\d{10}3$',i) for i in text_list]
# print(result_list)

# text4="abcdefganvonoiafa"
# text5="abcabcabc,bcdbcd,cdecdf"
# print(re.findall(r'[^a-c]',text4))
# print(re.findall(r'[\b]',text4))
# print(re.findall(r'(\w{3})(\1)',text5))
#
# for match in re.finditer(r'(\w{3})(\1)',text5):
#     print(match.group())
#     print(match.groups())

# print(re.findall(r'(?<=密码)(?#qagajhfaiosd)\d*',text))
#
# text6="abc,ABC,Abc"
# print(re.findall(r'abc',text6,flags=re.I))

# print(re.search(r'\d+',text).group())
# m=re.sub(r'\d+',"***",text)
# n=re.subn(r'\d+',"***",text)
# print(m," ",n," ",text)

text7=" aga  /dafaf   ,fasgag . fAGF"
print(re.split(r'\s*[/,.]\s*',text7))
