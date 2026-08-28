from datasets import load_dataset
# 加载数据
data = load_dataset("rotten_tomatoes")
# print(data)
# print(data["train"][0, -1])

from transformers import pipeline
# 我们的Hugging Face模型路径
model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
# 将模型加载到流水线中
pipe = pipeline(
model=model_path,
tokenizer=model_path,
return_all_scores=True,
device="cuda:0"
)

import numpy as np
from tqdm import tqdm
from transformers.pipelines.pt_utils import KeyDataset
# 运行推理
y_pred = []
for output in tqdm(pipe(KeyDataset(data["test"], "text")),
    total=len(data["test"])):
    negative_score = output[0]["score"]
    positive_score = output[2]["score"]
    assignment = np.argmax([negative_score, positive_score])
    y_pred.append(assignment)

from sklearn.metrics import classification_report
def evaluate_performance(y_true, y_pred):
    """创建并打印分类报告"""
    performance = classification_report(
    y_true, y_pred,
    target_names=["Negative Review", "Positive Review"]
    )
    print(performance)

evaluate_performance(data["test"]["label"], y_pred)