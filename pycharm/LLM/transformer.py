import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
model = AutoModelForCausalLM.from_pretrained(
"microsoft/Phi-3-mini-4k-instruct",
device_map="cuda",
torch_dtype="auto",
trust_remote_code=True,
)
# 创建流水线
generator = pipeline(
"text-generation",
model=model,
tokenizer=tokenizer,
return_full_text=False,
max_new_tokens=50,
do_sample=False,
)

prompt = "Write an email apologizing to Sarah for the tragic gardening mishap.Explain how it happened."
output = generator(prompt)
print(output[0]['generated_text'])