# import copy
# import random
# # a=random.randint(1,10)
# # list=[1,5,94,52,4,5,11,5,4,43,468,4,16,4]
# # list2=copy.deepcopy(list
#
# oho=[1,2,3,4,5]
# oho=[i*2 for i in oho]
# print(f"{oho}")

strList=["Excellent","Fast","False","Brilliant","Fantastic"]
strList=[it for it in strList if it[0]=='F']
print(strList)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flattenMatrix=[it2 for it in matrix for it2 in it]
print(flattenMatrix)

