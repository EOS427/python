from pathlib import Path
import os

text_address=input()
path = os.path.normpath(text_address.strip().strip('"').strip("'"))
with open(path,'r',encoding='utf-8') as file:
    print(file.read())
