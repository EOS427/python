import os
import torch
from transformers import BertTokenizer, BertForMaskedLM
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"  # 关掉符号链接警告
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"   # 用国内镜像加速下载

from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = AutoModelForMaskedLM.from_pretrained("bert-base-chinese")

sentences = [
    "中国的首都是[MASK]京。",
    "我爱北京天安[MASK]。",
    "人工智能正在改变我们的[MASK]活。",
]

for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = outputs.logits

    mask_position = (inputs.input_ids[0] == 103).nonzero(as_tuple=True)[0]

    mask_predictions = predictions[0, mask_position, :]

    top5_token_ids = torch.topk(mask_predictions, 5, dim=-1).indices[0].tolist()
    top5_words = tokenizer.convert_ids_to_tokens(top5_token_ids)

    print(f"原句: {sentence}")
    print(f"预测: {top5_words}")
    print("-" * 50)

