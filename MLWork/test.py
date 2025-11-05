# import requests

# url="https://api.siliconflow.cn/v1/chat/completions"
# headers={
#     "Content-Type": "application/json",
#     "Authorization": "Bearer sk-cumwktcvhnxyqbqnhqjsoiknoozfklowfcdglkqvikohtjsl"
# }

# payload = {
#     "model": "Qwen/QwQ-32B",
#     "messages": [
#         {
#             "role": "user",
#             "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
#         }
#     ]
# }

# response = requests.post(url, headers=headers, json=payload)
# print(response.status_code)
# print(response.json())


# lst=[10,20,3,7]
# print(sum(lst))
# sum=0
# for i in range(len(lst)):
#     sum += lst[i]
# print(f"sum is {sum}")



# def getValue(dict,keyStr):
#     if keyStr in dict.keys():
#         return dict[keyStr]
#     else:
#         return -1


# def getValue2(dict,keyStr):
#    dict.get(keyStr)
# dictory={"AI":1,"NLP":2}
# print(str(getValue(dictory,"AI")))


# l1=[1,2,3,4]
# l2=[5,6,7,8]

# dictory2={}
# sentence=['I','I','love','NLP','LLM','AI','AI']
# for word in  sentence:
#     if word in dictory2:
#         dictory2[word]+=1
#     else:
#         dictory2[word]=1
# print(dictory2)

# for word in  sentence:
#     dictory2[word]=dictory2.get(word,0)+1
# print(dictory2)


# str1="Hello World"
# str2 = str1.upper()
# lst_str = str2.split('')
# print(lst_str)
# help(lst_str.sort)

nums=[2,7,11,15,1,8]
target=9

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])    
# lst3=[[i,j] for i in range(len(nums)) for j in range(len(nums)) if i!=j and nums[i]+nums[j]==target]
# print(lst3)

# def twoSum(nums, target):
#     result = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 result.append([i,j])
#     return result

# print(twoSum(nums, target))

# nums=[0,1,0,3,12]
# def moveZeroes(nums):
#     j=0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[j]=nums[i]
#             j+=1
#     for k in range(j,len(nums)):
#         nums[k]=0
#     return nums
# print(moveZeroes(nums)) 


# import numpy as np

# a = np.array([[1,2,3],[4,5,6]])
# b = np.random.random([2,3])
# print(b)
# print(np.argmax(a))
# print(np.argmax(b))
# np.zeros((3,6))
# print(np.sum(a))
# print(np.sum(a,axis=0))
# print(np.sum(a,axis=1))


# import requests
# url='https://api.siliconflow.cn/v1/chat/completions'
# headers={
#     'Authorization': 'Bearer sk-cumwktcvhnxyqbqnhqjsoiknoozfklowfcdglkqvikohtjsl',
#     'Content-Type': 'application/json'
# }
# data ={
#   "model": "Qwen/QwQ-32B",
#   "messages": [
#     {
#       "role": "user",
#       "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
#     }
#   ]
# }
# response = requests.post(url,headers=headers,json=data)
# print (response.status_code)


# 1. 给定一个数值列表（向量），v = [10, 20, 3, 7]，请计算并返回列表中所有元素的总和。
# lst=[10, 20, 3, 7]
# print(sum(lst))
# sum = 0
# for i in lst:
#     sum += i  
# print(f"sum is {sum}")
# print(dir(lst))
# help(lst.pop)

# print(lst)
# 2. 给定一个词汇表 vocab 字典 vocab = {'AI': 1, 'NLP': 2} ，请实现一个函数，输入单词，返回其对应的 ID。如果单词不在词汇表中，返回 -1。
dictory = {
    'AI':1,
    'NLP': 2
}
#word = input("请输入一个单词")
# if word in dictory:
#     print(dictory[word])
# else:
#     print(-1)   
#print(dictory.get(word,-1))
# print(dir(dictory))
# help(dictory.update)
# dictory.update({'ML':3})
# print(dictory)
# dictory.update({'NLP':10})
# print(dictory)


# # 3. 给定两个相同长度的数值列表（向量）v1 = [1, 5, 9], v2 = [2, 3, 1]，请实现对应元素相加操作，并返回一个新的结果列表
# v1 = [1, 5, 9]
# v2 = [2, 3, 1]
# v3 = list()
# for i in range(len(v1)):
#     v3.append(v1[i] + v2[i])
# print(v3)

# v3 = [v1[i] + v2[i] for i in range(len(v1))]
# print(v3)

# 4. 给定一个已分词的句子列表 sentence = ['我', '爱', '学习', '我', '爱', 'NLP']，请统计每个词出现的次数，并以字典形式返回。
# dictory2=dict()
# sentence=['I','I','love','NLP','LLM','AI','AI']
# # for word in sentence:
# #     dictory2[word]=dictory2.get(word,0)+1
    
# for word in sentence:
#     if word in dictory2:
#        dictory2[word]+=1
#     else:
#         dictory2[word]=1
# print(dictory2)

# 5. 给定一个句子 text = "NLP Is Awesome" ，请将句子中的所有字母转换为小写，并将句子按照空格切分成一个列表（分词）。
# text = "NLP Is Awesome"
# text.lower().split(' ')

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

'''
# nums=[2,7,11,15,1,8]
# target=9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])    

# dictory4 ={}
# i=0;
# for item in nums:
#     dictory4[item]=i
#     i+=1
# print(dictory4)
# for i in range(len(nums)):
#     tareget_num=target - nums[i]
#     #print(tareget_num)
#     if tareget_num in dictory4 :
#         print([i,dictory4.get(tareget_num)])


##给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

##请注意 ，必须在不复制数组的情况下原地对数组进行操作。

# nums=[0,1,0,3,12]
# j=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[j]=nums[i]
#         j+=1
# for k in range(j,len(nums)):
#     nums[k]=0
# print(nums)


from collections import defaultdict
from collections import Counter

nums5=[0,1,0,1,12]
print(Counter(nums5))

default_dict=defaultdict(int)
for item in nums5:
    default_dict[item] += 1
print (default_dict)

default_dict2=defaultdict(list)
for item in nums5:
    default_dict2[item]=default_dict2.get(item,0)+1
print (default_dict2)