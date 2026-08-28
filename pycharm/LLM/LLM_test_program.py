# from transformers import AutoModelForCausalLM
#
#
# model = AutoModelForCausalLM.from_pretrained(
#     "microsoft/Phi-3-mini-4k-instruct",
#     device_map="auto",
#     torch_dtype="auto",
#     trust_remote_code=True
# )

import torch
print(torch.__version__)