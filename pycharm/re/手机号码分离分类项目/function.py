import re
import os
from pathlib import Path

class PhoneNumberAnalyzer:

    def __init__(self):
        self.__basic_criteria = re.compile(r'(?<!\d)1[3-9]\d{9}(?!\d)')
        self.__text = ""
        self.__phone_num_list = []
        self.__class_map = {}
        self.__key_name_list = []

    def read_file(self, absolute_path):
        path = os.path.normpath(absolute_path.strip().strip('"').strip("'"))
        try:
            with open(path, 'r', encoding='utf-8') as file:
                self.__text = file.read()

        except FileNotFoundError:
            print(" 文件不存在，请检查路径")

        except PermissionError:
            print(" 没有权限读取文件")

        except UnicodeDecodeError:
            print(" 文件编码不是 utf-8，读取失败")

        except Exception as e:
            print(f" 发生了未知错误：{e}")

        else:
            print("文件读取成功！")
            return self.__text

        return None

    def analyze_phone_number(self):
        self.__phone_num_list = self.__basic_criteria.findall(self.__text)
        self.__phone_num_list=list(set(self.__phone_num_list))
        return self.__phone_num_list

    def init_classify_map(self):
        basis_file_catalog = Path('classify_basis')
        for basis_text in basis_file_catalog.iterdir():
            lines = basis_text.read_text(encoding='utf-8').splitlines()
            for line in lines:
                word = line.split()
                if not word:
                    continue
                self.__key_name_list.append(word[0])
                for index in range(1, len(word)):
                    self.__class_map[word[index]] = word[0]

    def classify_phone_number(self):
        result = {}
        for phone_num in self.__phone_num_list:
            head = phone_num[:3]
            if head in self.__class_map:
                result.setdefault(self.__class_map[head], []).append(phone_num)
            else:
                result.setdefault('unknown', []).append(phone_num)
        for key in self.__key_name_list:
            os.makedirs(f'classified_result',exist_ok=True)
            with open(f'classified_result/{key}.txt', 'w', encoding='utf-8') as file:
                file.write(f"{key}运营商号码如下：\n")
                file.write(' '.join(result.get(key, [])) + '\n')
        os.makedirs(f'classified_result',exist_ok=True)
        with open(f'classified_result/unknown.txt', 'w', encoding='utf-8') as file:
            file.write("未知运营商号码如下：\n")
            file.write(' '.join(result.get('unknown', [])) + '\n')


def main():
    operator = PhoneNumberAnalyzer()
    absolute_path = input("请输入待处理文档绝对地址：")
    operator.read_file(absolute_path)
    operator.analyze_phone_number()
    operator.init_classify_map()
    operator.classify_phone_number()


if __name__ == "__main__":
    main()
