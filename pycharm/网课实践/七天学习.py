condition=True
time=0
while condition and time<7:
    condition=input("今日学习情况:")
    if condition.lower()=="false":
        print("坚持成功")
        break
    time+=1
else:print("坚持成功")
