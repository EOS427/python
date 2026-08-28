from transformers import AutoModelForCausalLM, AutoTokenizer
# 加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(
"microsoft/Phi-3-mini-4k-instruct",
device_map="cuda",
torch_dtype="auto",
trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# from transformers import pipeline
# # 创建流水线
# generator = pipeline(
# "text-generation",
# model=model,
# tokenizer=tokenizer,
# return_full_text=False,
# max_new_tokens=500,
# do_sample=False
# )
# messages = [
# {"role": "user", "content": "Create a funny joke about chickens."}
# ]
# # 生成输出
# output = generator(messages)
# print(output[0]["generated_text"])

prompt = "Write an email apologizing to Sarah for the tragic gardening mishap.Explain how it happened.<|assistant|>"
# 对输入提示词进行分词
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
# 生成文本
generation_output = model.generate(input_ids=input_ids,max_new_tokens=20)
# 打印输出
# print(tokenizer.decode(generation_output[0]))
# print(input_ids)

# for it in input_ids:
#     print(tokenizer.decode(it))
#
# print(tokenizer.decode(input_ids[0]))
# print(generation_output[0])
# print(tokenizer.decode(generation_output[0]))
# print(tokenizer.decode(3323))
# print(tokenizer.decode(622))
# print(tokenizer.decode([3323, 622]))
# print(tokenizer.decode(29901))


from transformers import AutoModel, AutoTokenizer
# 加载分词器
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-base")
# 加载语言模型
model = AutoModel.from_pretrained("microsoft/deberta-v3-xsmall")
# 对句子进行分词
tokens = tokenizer('Hello world', return_tensors='pt')
# 处理词元
output = model(**tokens)[0]

# for token in tokens['input_ids'][0]:
#     print(tokenizer.decode(token))
#
# print(output)

import gensim.downloader as api
# 下载嵌入（66 MB，glove，训练数据来自维基百科，向量大小：50）
# 其他选项包括"word2vec-google-news-300"
# 更多选项请访问gensim-data的GitHub仓库
model = api.load("glove-wiki-gigaword-50")
# print(model.most_similar([model['king']], topn=11))

from sentence_transformers import SentenceTransformer
# 加载模型
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
# 将文本转换为文本嵌入
vector = model.encode("Best movie ever!")
# print(vector.shape)


import pandas as pd
from urllib import request
# 获取播放列表数据集文件
data = request.urlopen('https://storage.googleapis.com/maps-premium/dataset/yes_complete/train.txt')
# 解析播放列表数据集文件。跳过前两行，因为它们只包含元数据
lines = data.read().decode("utf-8").split('\n')[2:]
# 删除只有一首歌的播放列表
playlists = [s.rstrip().split() for s in lines if len(s.split()) > 1]
# 加载歌曲元数据
songs_file = request.urlopen('https://storage.googleapis.com/maps-premium/dataset/yes_complete/song_hash.txt')
songs_file = songs_file.read().decode("utf-8").split('\n')
songs = [s.rstrip().split('\t') for s in songs_file]
songs_df = pd.DataFrame(data=songs, columns = ['id', 'title', 'artist'])
songs_df = songs_df.set_index('id')

print( 'Playlist #1:\n ', playlists[0], '\n')
print( 'Playlist #2:\n ', playlists[1])

from gensim.models import Word2Vec
# 训练我们的word2vec模型
model = Word2Vec(
playlists, vector_size=32, window=20, negative=50, min_count=1, workers=4
)
song_id = 2172
# 让模型找出与歌曲2172相似的歌曲
print(model.wv.most_similar(positive=str(song_id)))
print(songs_df.iloc[2172])

import numpy as np
def print_recommendations(song_id):
    similar_songs = np.array(
    model.wv.most_similar(positive=str(song_id),topn=5))[:,0]
    return songs_df.iloc[similar_songs]

print_recommendations(2172)